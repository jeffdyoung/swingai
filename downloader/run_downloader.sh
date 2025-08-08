#!/bin/bash

# Shell script to build and run the YouTube downloader container

IMAGE_NAME="youtube-downloader"
#YT_URL="https://www.youtube.com/watch?v=6sD5asBLNrw"
#YT_URL="https://www.youtube.com/watch?v=pccwKQsEeO4"
YT_URL="https://www.youtube.com/watch?v=DXAG9p9h6G0"
echo "🔧 Building Docker image: $IMAGE_NAME"
podman build -t $IMAGE_NAME .

echo ""
#read -p "📥 Enter YouTube URL to download: " YT_URL

if [ -z "$YT_URL" ]; then
  echo "❌ No URL provided. Exiting."
  exit 1
fi

echo "preparing downloads dir"
mkdir -p ./downloads
chmod 777 ./downloads
chcon -Rt svirt_sandbox_file_t ./downloads
ls -shal downloads

echo ""
echo "Downloading video to: $PWD"
podman run --rm \
  -v "$PWD:/downloads:Z" \
  $IMAGE_NAME "$YT_URL"
