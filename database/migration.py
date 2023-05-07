'''
#########################
Please go to the path server/app.py for all the CRUD calls
#########################
'''

import psycopg2, os, uuid

# DB connection
conn = psycopg2.connect(
    host=os.environ["db_host"],
    database=os.environ["db_name"],
    user=os.environ["db_user"],
    password=os.environ["db_pwd"])

# ================ Integrity ==============

def create_cve_table():
    with conn.cursor() as cursor:
        cursor.execute("""
                CREATE TABLE cve (
                id VARCHAR(32) PRIMARY KEY,
                types VARCHAR(50) NOT NULL,
                cve VARCHAR(20) NOT NULL,
                severity VARCHAR(10) NOT NULL (severity IN (low, medium, high, critical)),
                score INT NOT NULL,
                remediation BOOLEAN NOT NULL,
                FOREIGN KEY (remediation) REFERENCES remediation (fixable))
                );
                """)

def alter_cve_table():
    with conn.cursor() as cursor:
        cursor.execute("""
                ALTER TABLE cve
                ADD COLUMN description TEXT;
                """)
        
def drop_cve_table():
    with conn.cursor() as cursor:
        cursor.execute("""
                DROP TABLE IF EXISTS cve;
                """)

def create_team_table():
    with conn.cursor() as cursor:
        cursor.execute("""
                CREATE TABLE teams (
                id VARCHAR(32) PRIMARY KEY,
                team_id VARCHAR(6) NOT NULL,
                assigned VARCHAR(20) NOT NULL,
                priority VARCHAR(10) NOT NULL (priority IN (low, medium, high, critical)),
                FOREIGN KEY (team_id) REFERENCES team (id))
                );
                """)
        
def drop_team_table():
    with conn.cursor() as cursor:
        cursor.execute("""
                DROP TABLE IF EXISTS teams;
                """)

def create_container_table():
    with conn.cursor() as cursor:
        cursor.execute("""
                CREATE TABLE containers (
                id VARCHAR(45) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                image VARCHAR(255) NOT NULL,
                created DATE NOT NULL,
                deployed DATE NOT NULL
                );
                """)

def alter_container_table():
    with conn.cursor() as cursor:
        cursor.execute("""
                ALTER TABLE containers
                ADD COLUMN description TEXT;
                """)
        
def drop_container_table():
    with conn.cursor() as cursor:
        cursor.execute("""
                DROP TABLE IF EXISTS containers;
                """)

# ================ Views ===================

def create_view_assign_team():
    with conn.cursor() as cursor:
        query = """CREATE VIEW assignment_per_team AS
                select id, teamName, count(*) cnt from teams t inner join
                assignment a on t.id = a.teamsID"""
        cursor.execute(query)
        conn.commit()


def create_view_container_ticket():
    with conn.cursor() as cursor:
        query = """CREATE VIEW ticket_per_container AS
                select id, teamName, count(*) cnt from teams t inner join
                assignment a on t.id = a.teamsID"""
        cursor.execute(query)
        conn.commit()

# ================ Functions ===================

def host_vuln_count():
    with conn.cursor() as cursor:
        query = """CREATE FUNCTION hostvulns(hostid char(45), severity char(5)) returns int
                BEGIN
                  declare lhostvulns int;
                  set lhostvulns = (SELECT count(*) from tickets where host_id = hostid, cve_severity = severity);
                  return lhostvulns;
                END;"""
        cursor.execute(query)
        conn.commit()

def container_vuln_count():
    with conn.cursor() as cursor:
        query = """CREATE FUNCTION containervulns(containerid char(45), severity char(5)) returns int
                BEGIN
                  declare lcontainervulns int;
                  set lcontainervulns = (SELECT count(*) from tickets where container_id = containerid, cve_severity = severity);
                  return lcontainervulns;
                END;"""
        cursor.execute(query)
        conn.commit()

# ================ Procedures ===================

def host_procedure():
    with conn.cursor() as cursor:
        query = f"""CREATE PROCEDURE escalatehost(IN hostid (char45), IN severity char(5), OUT urgency varchar(255))
                BEGIN
                  SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
                  if hostvulns(hostid, severity) > 5 THEN
                    INSERT INTO tickets(id, status, hostID)
                      VALUES({uuid.uuid4().hex}, 'urgent', hostid)
                      SET urgency = "High";
                  else
                      SET urgency = "Low";
                  end if;
                END;"""
        cursor.execute(query)
        conn.commit()
    

def container_procedure():
    with conn.cursor() as cursor:
        query = f"""CREATE PROCEDURE escalatecontainer(IN containerid (char45), IN severity char(5), OUT urgency varchar(255))
                BEGIN
                  SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
                  if containervulns(containerid, severity) > 5 THEN
                    INSERT INTO tickets(id, status, containerID)
                      VALUES({uuid.uuid4().hex}, 'urgent', containerid)
                      SET urgency = "High";
                  else
                      SET urgency = "Low";
                  end if;
                  commit;
                END;"""
        cursor.execute(query)
        conn.commit()

# ================ Triggers ===================

def cve_trigger():
    host_id = "mongodb-023-production"
    with conn.cursor() as cursor:
        query = f"""CREATE TRIGGER update_cve
                AFTER INSERT OR UPDATE OF severity, score ON cve
                FOR EACH ROW
                EXECUTE FUNCTION host_vuln_count({host_id},new.severity)"""
        cursor.execute(query)
        conn.commit()
    

def team_trigger():
    with conn.cursor() as cursor:
        query = f"""CREATE TRIGGER update_cve
                AFTER INSERT OR UPDATE ON teams
                FOR EACH ROW
                BEGIN
                  insert into team_audit (id, old_email) VALUES (old.id, old.email)
                END;"""
        cursor.execute(query)
        conn.commit()

def main():
    create_view_assign_team()

if __name__ == '__main__':
    main()

'''
#########################
Please go to the path server/app.py for all the CRUD calls
#########################
'''