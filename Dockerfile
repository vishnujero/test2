FROM python:3-alpine
COPY welcome.py /app/
WORKDIR /app

CMD [ "python", "welcome.py" ]