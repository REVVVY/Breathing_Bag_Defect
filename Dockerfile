FROM python:3.6

WORKDIR /usr/app

#RUN apt-get update && apt-get install -y python3-opencv libgl1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888

CMD ["jupyter-lab", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]