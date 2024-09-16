#
# docker build -t fastapi-redis .
# docker run --name fastapi-redis -p 8000:8000 fastapi-redis
#
FROM python:3.12

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]