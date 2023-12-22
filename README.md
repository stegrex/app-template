# App Template

## Environment Setup

### Quick Setup
- Download and then install Docker Desktop. No need to create a Docker account. Feel free to skip that step. Run Docker Desktop. https://www.docker.com/products/docker-desktop/
- Download project code via git. Make sure the name of the project is retained. For example:
```
/path/to/project/app-template
```
- Navigate to the project from the terminal:
```
cd /path/to/project/app-template
```
- In this directory, run docker compose in order to build and run the BE code in one step:
```
docker compose up --build -d
```
- Then run the DB database and table creation script to ensure the DB is set up properly. You only need to run this any time there are schema changes to the DB.
```
docker exec -it app-template-db-1 /app/startup.sh
```
- Once the build is complete, open a browser and navigate to `http://127.0.0.1:8666/docs`
- If there are any build issues, a quick teardown and rebuild may fix those issues.
```
docker compose down
docker compose up --build -d
```

### Docker Commands

#### Compose
```
docker compose up --build -d
docker compose build --no-cache
docker compose down

docker exec -it app-template-1 bash

docker compose down --remove-orphans
```

#### Update DB Schemas
```
docker exec -it app-template-db-1 /app/startup.sh
```

#### Build Individual Components (If Needed)
```
docker build -t app-template:dev .
docker run --name=app-dev -dt app-template:dev
docker ps -a
docker exec -it app-dev /bin/sh
docker stop app-dev
docker rm app-dev
```

#### Cleanup
```
docker image prune -af
docker builder prune
docker rmi <image name (Repository[:Tag])>
```

### Maintenance

#### Running Tests
Run in Docker Backend container in /app folder
```
python3 -m unittest -v
```
