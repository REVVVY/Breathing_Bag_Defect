
Build Docker image

```
docker build -t bbdefect .
```

run build image

```
docker run -it --rm --name bbdefect
```

Conainer status

```
docker container ls
```

Rebuild docker service and run container

```
docker compose up --no-deps --build bb
```