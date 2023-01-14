FROM python:3.11.1-alpine

WORKDIR /app
COPY . .
RUN addgroup app && \
    adduser -D -h /app -s /bin/sh -G app app && \
    pip3 install --no-cache -r requirements.txt

CMD ["su", "app", "-c", "gunicorn -b 0.0.0.0:8080 fake:app"]
