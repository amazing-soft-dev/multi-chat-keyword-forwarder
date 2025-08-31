FROM python:3.11-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libsqlite3-0 \
    libsqlite3-dev \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

RUN mkdir -p logs

# Запуск бота
CMD ["python", "main.py"]

