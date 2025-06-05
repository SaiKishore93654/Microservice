FROM python:3.9-slim

WORKDIR /app
COPY order.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5003

CMD ["python", "order.py"]
