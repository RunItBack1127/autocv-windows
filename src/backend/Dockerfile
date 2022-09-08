FROM python:3.11-rc-alpine

WORKDIR /app

COPY requirements .

RUN pip3 install -r requirements

CMD ["gunicorn", "--bind", "0.0.0.0.5000", "server:app"]