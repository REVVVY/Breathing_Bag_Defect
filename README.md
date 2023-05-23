
## Breathing Bag Defect Detection
AI-based quality assurance system for breathing bag defect detection using Mask RCNN, Tensorflow 2.4.1 and python 3.8.16.

### Anaconda Environment

Create anaconda environment from predefined enviroment from repo (env.yml)

```

conda env create -n envname -f envfile.yml python=3.8.16

```

Activate anaconda environment

```

conda activate environmentname

```

  
  

### Docker

Build Docker image (remove sudo to run on windows)

```

sudo docker build -t bbdefect .

```

Run built image with GPU

```

sudo docker run --gpus=all -it -p 8888:8888 -v "$(pwd):/usr/app" --rm --name bbdefect bbdefect

```

Conainer status

```

docker container ls

```

Composer command

  

Rebuild docker service and run container

```

docker compose up --no-deps --build bb

```

  

### Lambdalabs Cloud GPU Instance

Steps 3 and 4 only needed for private github repository.

1. Create SSH and store public key

  

2. Launch instance with stored key

  

3. Change directory into .ssh Copy cloud key to cloud terminal (id_rsa, id_rsa.pub)

  

- Create `id_rsa`, Create `id_rsa.pub`

  

```

nano id_rsa

```

```

nano id_rsa.pub

```

4. Change permission of `id_rsa` file to 400 to restrict access to the owner only and prevent unauthorized access.

```

sudo chmod 400 id_rsa

```

### Secure Copy Protocol (File Transfer)

Dataset and weights are not stored on github. Needs manual transfer.

  

SCP command using -r to include all of the content (files and subfolders)

```

scp -r <source> <destination>

```

SCP example for transfering folder from local machine onto cloud instance.

```

scp -r localpath ubuntu@cloudaddress:cloudpath

```