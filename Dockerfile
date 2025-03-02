FROM python:3.9-alpine3.18 AS builder

RUN apk add --no-cache \
    build-base \
    gcc \
    python3-dev \
    musl-dev

WORKDIR /home/data/

COPY requirements.txt .

RUN python -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt


FROM python:3.9-alpine3.18

WORKDIR /home/data/

COPY --from=builder /venv /venv

COPY scripts.py .
COPY IF-1.txt AlwaysRememberUsThisWay-1.txt .

ENV PATH="/venv/bin:$PATH"

EXPOSE 5000

CMD ["python","scripts.py"]
