FROM python:3.7.16

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888

CMD ["jupyter-lab", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]