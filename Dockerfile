# Gunakan image dasar Python
FROM python:3.11-slim

# Set working directory di dalam container
WORKDIR /app

# Salin requirements.txt ke dalam container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin isi folder 'app/' ke dalam /app/ di container
COPY app/ /app/

# Jalankan aplikasi
CMD ["python", "bot.py"]
