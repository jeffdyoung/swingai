FROM python:3.12-slim

# Install ffmpeg and yt-dlp
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install --no-cache-dir yt-dlp && \
    rm -rf /var/lib/apt/lists/*

# Create output dir
RUN mkdir /downloads
WORKDIR /app

# Copy script into image
COPY download.py .

# Default command
ENTRYPOINT ["python", "download.py"]
