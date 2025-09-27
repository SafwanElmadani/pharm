# pharm

# Prerequisite:
- docker 
    - https://docs.docker.com/engine/install/
- docker-compose
    - https://docs.docker.com/compose/install/standalone/

# Steps
1. clone this repo:
    - `git clone https://github.com/SafwanElmadani/pharm.git`
2. `cd pharm`
3. run: `docker-compose up -d`
    - this will start the postgres db and the pgadmin gui
    - to stop the containers, run: `docker-compose down`
4. to connect to postgres db gui, open the this link in the browser: `http://localhost:8080/`
    - check the docker-compose.yml file for credentials.


