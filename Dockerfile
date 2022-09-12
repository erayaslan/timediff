FROM python:3.10-alpine

EXPOSE 5000/tcp

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY templates ./templates
COPY app.py .

USER nobody

CMD [ "python", "./app.py" ]