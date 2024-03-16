FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY app ./app

EXPOSE 5000

CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]
