FROM python:3.9-slim

WORKDIR /app
COPY order.py .
RUN pip install flask
EXPOSE 5003

CMD ["python", "order.py"]
