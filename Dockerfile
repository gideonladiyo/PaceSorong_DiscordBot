# Gunakan image dasar untuk Python
FROM python:3.11-slim

# Set working directory di dalam container
WORKDIR /app

# Salin requirements.txt ke dalam container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin folder app ke dalam container
COPY app/ ./app/

# Set working directory ke dalam app/
WORKDIR /app/app

# Jalankan bot.py
CMD ["python", "bot.py"]
