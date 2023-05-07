'''
#########################
Please go to the path database/migration.py for all database related queries
#########################
'''

from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid, psycopg2, os

# DB connection / save creds in secure locally
conn = psycopg2.connect(
    host=os.environ["db_host"],
    database=os.environ["db_name"],
    user=os.environ["db_user"],
    password=os.environ["db_pwd"]
)

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# ====================== CVE ===========================

@app.route('/api/cve', methods=['GET', 'POST'])
def all_cves():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        with conn.cursor() as cursor:
            query = """INSERT INTO cve(id,
                types, cve, severity, score, remediation)
                VALUES (%s,%s,%s,%s,%s)"""
            values = (uuid.uuid4().hex,
                    post_data.get('types'),
                    post_data.get('cve'),
                    post_data.get('severity'),
                    post_data.get('score'),
                    post_data.get('remediation'))
            cursor.execute(query, values)
            conn.commit()
        response_object['message'] = 'CVE added!'
    else:
        with conn.cursor() as cursor:
            query = "SELECT * FROM cve"
            cursor.execute(query)
        response_object['VulnerabilityCVE'] = cursor.fetchall()
    return jsonify(response_object)

@app.route('/api/cve/<cve_id>', methods=['PUT', 'DELETE'])
def single_cve(cve_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        query = f""" UPDATE cve SET 
                types = {post_data.get('types')},
                cve = {post_data.get('cve')},
                severity = {post_data.get('severity')},
                score = {post_data.get('score')},
                remediation ={post_data.get('remediation')}
                WHERE vendor_id = {post_data.get('id')}"""
        cursor.execute(query)
        conn.commit()
        response_object['message'] = 'CVE updated!'
    if request.method == 'DELETE':
        with conn.cursor() as cursor:
            query = f"DELETE FROM cve WHERE id = {cve_id}"
            cursor.execute(query)
            conn.commit()
        response_object['message'] = 'CVE removed!'
    return jsonify(response_object)

# ====================== Teams ===========================

@app.route('/api/teams', methods=['GET', 'POST'])
def all_teams():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        with conn.cursor() as cursor:
            query = """INSERT INTO teams(id, name, email)
                VALUES (%s,%s,%s)"""
            values = (uuid.uuid4().hex,
                    post_data.get('teamName'),
                    post_data.get('email'))
            cursor.execute(query, values)
            conn.commit()
        response_object['message'] = 'Team added!'
    else:
        with conn.cursor() as cursor:
            query = "SELECT * FROM teams"
            cursor.execute(query)
        response_object['VulnerabilityTeams'] = cursor.fetchall()
    return jsonify(response_object)

@app.route('/api/teams/<team_id>', methods=['PUT', 'DELETE'])
def single_team(team_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        query = f"""UPDATE team SET 
                teamName = {post_data.get('teamName')},
                email = {post_data.get('email')}"""
        cursor.execute(query)
        conn.commit()
        response_object['message'] = 'Team updated!'
    if request.method == 'DELETE':
        with conn.cursor() as cursor:
            query = f"DELETE FROM team WHERE id = {team_id}"
            cursor.execute(query)
            conn.commit()
        response_object['message'] = 'Team removed!'
    return jsonify(response_object)

# ====================== Assignment ===========================

@app.route('/api/assignment', methods=['GET', 'POST'])
def all_assignments():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        with conn.cursor() as cursor:
            query = """INSERT INTO assignment(id,
                teamID, assignedDate, priority)
                VALUES (%s,%s,%s)"""
            values = (uuid.uuid4().hex,
                    post_data.get('teamID'),
                    post_data.get('assignedDate'),
                    post_data.get('priority'))
            cursor.execute(query, values)
            conn.commit()
        response_object['message'] = 'Assignment added!'
    else:
        with conn.cursor() as cursor:
            query = "SELECT * FROM assignment"
            cursor.execute(query)
        response_object['VulnerabilityAssignment'] = cursor.fetchall()
    return jsonify(response_object)

@app.route('/api/assignment/<assignment_id>', methods=['PUT', 'DELETE'])
def single_assingment(assingment_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        query = f""" UPDATE assignment SET 
                assignedDate = {post_data.get('assignedDate')},
                priority = {post_data.get('priority')}"""
        cursor.execute(query)
        conn.commit()
        response_object['message'] = 'Assignment updated!'
    if request.method == 'DELETE':
        with conn.cursor() as cursor:
            query = f"DELETE FROM assignment WHERE id = {assingment_id}"
            cursor.execute(query)
            conn.commit()
        response_object['message'] = 'Assignment removed!'
    return jsonify(response_object)

# ====================== Vulnerability Tickets ===========================

@app.route('/api/tickets', methods=['GET', 'POST'])
def all_tickets():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        with conn.cursor() as cursor:
            query = """INSERT INTO tickets(id,
                status, scannedDate)
                VALUES (%s,%s,%s)"""
            values = (uuid.uuid4().hex,
                    post_data.get('status'),
                    post_data.get('scannedDate'))
            cursor.execute(query, values)
            conn.commit()
        response_object['message'] = 'Ticket added!'
    else:
        with conn.cursor() as cursor:
            query = "SELECT * FROM tickets"
            cursor.execute(query)
        response_object['VulnerabilityTickets'] = cursor.fetchall()
    return jsonify(response_object)

@app.route('/api/tickets/<ticket_id>', methods=['PUT', 'DELETE'])
def single_ticket(ticket_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        query = f""" UPDATE tickets SET 
                status = {post_data.get('status')},
                scannedDate = {post_data.get('scannedDate')}"""
        cursor.execute(query)
        conn.commit()
        response_object['message'] = 'Ticket updated!'
    if request.method == 'DELETE':
        with conn.cursor() as cursor:
            query = f"DELETE FROM tickets WHERE id = {ticket_id}"
            cursor.execute(query)
            conn.commit()
        response_object['message'] = 'Ticket removed!'
    return jsonify(response_object)

# ====================== Remediations ===========================

@app.route('/api/remediations', methods=['GET', 'POST'])
def all_remediations():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        with conn.cursor() as cursor:
            query = """INSERT INTO remediations(id,
                instructions, fixable)
                VALUES (%s,%s)"""
            values = (uuid.uuid4().hex,
                    post_data.get('instructions'),
                    post_data.get('fixable'))
            cursor.execute(query, values)
            conn.commit()
        response_object['message'] = 'Remediation added!'
    else:
        with conn.cursor() as cursor:
            query = "SELECT * FROM remediations"
            cursor.execute(query)
        response_object['VulnerabilityRemediations'] = cursor.fetchall()
    return jsonify(response_object)

@app.route('/api/remediations/<remediation_id>', methods=['PUT', 'DELETE'])
def single_remediation(remediation_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        query = f""" UPDATE remediations SET 
                instruction = {post_data.get('instruction')},
                fixable = {post_data.get('fixable')}"""
        cursor.execute(query)
        conn.commit()
        response_object['message'] = 'Remediation updated!'
    if request.method == 'DELETE':
        with conn.cursor() as cursor:
            query = f"DELETE FROM remediations WHERE id = {remediation_id}"
            cursor.execute(query)
            conn.commit()
        response_object['message'] = 'Remediation removed!'
    return jsonify(response_object)

# ====================== Containers ===========================

@app.route('/api/containers', methods=['GET', 'POST'])
def all_containers():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        with conn.cursor() as cursor:
            query = """INSERT INTO containers(id,
                name, image, createdDate, lastDeployed)
                VALUES (%s,%s,%s,%s,%s)"""
            values = (uuid.uuid4().hex,
                    post_data.get('name'),
                    post_data.get('image'),
                    post_data.get('createdDate'),
                    post_data.get('lastDeployed'))
            cursor.execute(query, values)
            conn.commit()
        response_object['message'] = 'Container added!'
    else:
        with conn.cursor() as cursor:
            query = "SELECT * FROM containers"
            cursor.execute(query)
        response_object['VulnerabilityContainers'] = cursor.fetchall()
    return jsonify(response_object)

@app.route('/api/containers/<container_id>', methods=['PUT', 'DELETE'])
def single_container(container_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        query = f""" UPDATE containers SET 
                name = {post_data.get('name')},
                image = {post_data.get('image')},
                createdDate = {post_data.get('createdDate')},
                lastDeployed = {post_data.get('lastDeployed')}"""
        cursor.execute(query)
        conn.commit()
        response_object['message'] = 'Container updated!'
    if request.method == 'DELETE':
        with conn.cursor() as cursor:
            query = f"DELETE FROM containers WHERE id = {container_id}"
            cursor.execute(query)
            conn.commit()
        response_object['message'] = 'Container removed!'
    return jsonify(response_object)

# ====================== Hosts ===========================

@app.route('/api/hosts', methods=['GET', 'POST'])
def all_hosts():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        with conn.cursor() as cursor:
            query = """INSERT INTO hosts(id,
                name, os, createdDate, lastDeployed)
                VALUES (%s,%s,%s,%s,%s)"""
            values = (uuid.uuid4().hex,
                    post_data.get('name'),
                    post_data.get('os'),
                    post_data.get('createdDate'),
                    post_data.get('lastRestarted'))
            cursor.execute(query, values)
            conn.commit()
        response_object['message'] = 'Host added!'
    else:
        with conn.cursor() as cursor:
            query = "SELECT * FROM hosts"
            cursor.execute(query)
        response_object['VulnerabilityHosts'] = cursor.fetchall()
    return jsonify(response_object)

@app.route('/api/hosts/<host_id>', methods=['PUT', 'DELETE'])
def single_host(host_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        query = f""" UPDATE hosts SET 
                name = {post_data.get('name')},
                image = {post_data.get('os')},
                createdDate = {post_data.get('createdDate')},
                lastDeployed = {post_data.get('lastRestarted')}"""
        cursor.execute(query)
        conn.commit()
        response_object['message'] = 'Host updated!'
    if request.method == 'DELETE':
        with conn.cursor() as cursor:
            query = f"DELETE FROM hosts WHERE id = {host_id}"
            cursor.execute(query)
            conn.commit()
        response_object['message'] = 'Host removed!'
    return jsonify(response_object)

@app.route('/api/cve_report', methods=['GET'])
def fixable_cves_report():
    response_object = {'status': 'success'}
    with conn.cursor() as cursor:
        query = f"""
            SELECT COUNT(*) AS num_fixable_cves
            FROM cve
            INNER JOIN remediation ON cve.id = remediation.id
            WHERE remediation.fixable = TRUE"""
        cursor.execute(query)
        conn.commit()
        response_object['cveReport'] = cursor.fetchall()
    return jsonify(response_object)

@app.route('/api/critical_assignment_report', methods=['GET'])
def critical_assignment_report():
    response_object = {'status': 'success'}
    with conn.cursor() as cursor:
        query = f"""
            SELECT COUNT(*) AS num_assignments
            FROM assignment
            INNER JOIN teams ON assignments.teamID = teams.id
            WHERE assignment.priority = critical"""
        cursor.execute(query)
        conn.commit()
        response_object['assignedReport'] = cursor.fetchall()
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="5000")

'''
#########################
Please go to the path database/migration.py for all database related queries
#########################
'''