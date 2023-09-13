# App Template

## Environment Setup

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
