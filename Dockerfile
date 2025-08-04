FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY process.py .
ENTRYPOINT ["python", "process.py"]