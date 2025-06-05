FROM python:3.9-slim

WORKDIR /app

COPY prod.py .
RUN pip install flask
EXPOSE 5001

CMD ["python","prod.py"]