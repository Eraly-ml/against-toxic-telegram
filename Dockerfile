FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r --no-cache-dir requirements.txt
COPY script.py .
CMD ["python", "./script.py"]
