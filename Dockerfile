FROM python:3.11.1-alpine

WORKDIR /app
COPY . .
RUN addgroup app && \
    adduser -D -h /app -s /bin/sh -G app app && \
    pip3 install --no-cache -r requirements.txt && \
    apk add tini --no-cache

ENV PYTHONUNBUFFERED=TRUE
CMD ["/sbin/tini", "--", "su", "app", "-c", "python3 -u fake.py"]
