FROM python:3.10.7

WORKDIR /app
COPY /requirements.txt .
COPY README.md ./
RUN pip install -r requirements.txt
COPY . .