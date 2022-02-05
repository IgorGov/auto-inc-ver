FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

RUN pip install --target=/app -r requirements.txt

FROM gcr.io/distroless/python3
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]