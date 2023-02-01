FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install --upgrade pip && \
pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py","uvicorn main:app --reload"]