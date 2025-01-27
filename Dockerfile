FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python deBERTa_classification.py

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "9000"]