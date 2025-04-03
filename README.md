# Sussex Mews

## Overview
This is project manages the Sussex Mews [website](https://sussexmews.co.uk) (work in progress), along with the various homelab services that runs on a Linux server (Ubuntu Server).

## Public Website
- **Description**: A public facing website mainly to be used to learn frontend technologies.
- **Tech Stack**: HTML for now. TODO: learn CSS, Typescript + React to make a nicer looking website.
- **Deployment**: AWS S3 static website sat behind a cloudfront distribution. Using a Route53 registered domain + ACM for access over HTTPS.

## Homelab
Utilising an old computer I built years ago and left to collect dust, I run Ubuntu Server 24 to host a range of services mainly to play around with technologies that interest me. Some examples are listed under the `Services` secion. All services run inside docker containers defined in the various docker compose files in this repo.

### Services

#### Homebridge Instance
- **Purpose**: To consolidate all smart home devices into a single Apple Homekit control panel.

#### Postgres Database
- **Purpose**: It's a database. It stores data.

#### Airflow
- **Purpose**: To run cron scripts for various processes needed in the home.

#### API
- **Purpose**: A basic FastAPI service used to integrate various services together. For example, updating the URLs for a dashboard located in the kitchen.

### Libraries

## Database
- **Purpose**: To provide `SQLAlchemy` ORMs for the hosted database. Also utilises `alelbic` for schema migrations.
