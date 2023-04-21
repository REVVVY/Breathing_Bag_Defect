
Build Docker image

```
docker build -t bbdefect .
```

run build image

```
docker run --gpus=all -it -p 8888:8888 -v ".:/usr/app" --rm --name bbdefect
```

Conainer status

```
docker container ls
```

Composer commands

Rebuild docker service and run container

```
docker compose up --no-deps --build bb
```

