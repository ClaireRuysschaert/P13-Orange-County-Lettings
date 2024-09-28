FROM  --platform=linux/amd64 python:3.8.3-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input

EXPOSE 8080

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080"]