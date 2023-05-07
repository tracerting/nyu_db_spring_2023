# My Docker Compose Setup

This repository contains a Docker Compose setup for running my application in a local development environment. The setup consists of two containers: one for the application itself and one for the database it uses.

## Requirements

Before you can use this Docker Compose setup, you must have the following tools installed on your system:

- Docker
- Docker Compose

## Installation

To install and run the application, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the root directory of the repository.
3. Open a terminal window and run the following command:
`docker-compose up --build`

This will download the necessary Docker images, build the containers, and start them up.

4. Once the containers are running, you can access the application by opening a web browser and navigating to `http://localhost:80`.

## Usage

With the Docker Compose setup running, you can make changes to the application code and see them reflected in real time. Simply edit the files in the `src/` directory, save your changes, and refresh your web browser to see the updated application.

## Configuration

The Docker Compose setup uses environment variables to configure the application and the database. These variables are defined in the `.env` file, which is included in this repository. You can modify these variables to customize the application's behavior.

## Cleanup

To stop the Docker Compose setup and remove the containers, run the following command:


This will stop the containers and remove them, but it will not remove any data that was stored in the database container. If you want to remove the database data as well, you can use the following command:


This will stop the containers, remove them, and also remove any data that was stored in the database container.
