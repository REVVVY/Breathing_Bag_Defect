FROM tensorflow/tensorflow:1.5.0-gpu-py3

WORKDIR /usr/app

RUN apt-get update && apt-get install -y --fix-missing libsm6 libxext6 libxrender1


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888

CMD ["jupyter", "notebook", "--allow-root"]