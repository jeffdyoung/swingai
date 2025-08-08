FROM python:3.12-slim

WORKDIR /app]

COPY requirements.txt .

# Upgrade pip before installing dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
    
COPY . .

RUN apt-get update && apt-get install -y ffmpeg libgl1-mesa-glx && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
