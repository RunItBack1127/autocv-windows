FROM python:3.8-rc-buster

WORKDIR /app

COPY requirements .

RUN pip3 install -r requirements

COPY . .

CMD ["python3", "server.py"]