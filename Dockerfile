FROM tensorflow/tensorflow:2.4.1-gpu

WORKDIR /usr/app

#docker run --gpus=all -it -p 8888:8888 -v "$(pwd):/usr/app" --rm --name bbdefect bbdefect

#RUN apt-get clean && apt-get update && apt-get install -y --no-install-recommends \
 #   libsm6 \
  #  libxext6 \
   # libxrender-dev \
    #&& rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888

CMD ["jupyter-lab", "--allow-root", "--ip", "0.0.0.0"]