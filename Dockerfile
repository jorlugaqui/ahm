FROM python:3.7-alpine

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["flask", "run", "--host=0.0.0.0"]