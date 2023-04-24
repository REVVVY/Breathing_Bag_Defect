## Docker 
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

## Cloud Usage

  1. Create instance
  2. Copy cloud key to cloud terminal (id_rsa, id_rsa.pub)
    - Create `id_rsa`
```sh
nano id_rsa
```

    - Create `id_rsa.pub`

```
nano id_rsa.pub
```

    - Change `id_rsa` permission with¨
```
sudo chmod 400 id_rsa
```

