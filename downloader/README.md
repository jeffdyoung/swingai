# YouTube Downloader (Dockerized)

This project provides a simple, containerized tool for downloading YouTube videos using yt-dlp, the modern fork of youtube-dl.

It’s perfect for:
- Pulling down golf swing reference videos
- Automating downloads for AI/ML analysis
- Running in clean, portable environments via Docker

## Features

- Downloads highest-quality video and audio
- Containerized with Python 3.12 and yt-dlp
- Output saved to your local directory
- Works with any public YouTube video

## How to Build the Docker Image

    git clone https://github.com/your-username/youtube-downloader.git
    cd youtube-downloader
    podman build -t youtube-downloader .

## How to Run the Downloader

Run the following command in your terminal:

    podman run --rm -v "$PWD:/downloads" youtube-downloader "<YouTube_URL>"

- Replace <YouTube_URL> with the actual video link.
- Downloads will appear in your current working directory.

Example:

    podman run --rm -v "$PWD:/downloads" youtube-downloader "https://www.youtube.com/watch?v=6sD5asBLNrw"

## Sample Golf Swing Videos

Use these public YouTube videos to test your downloader or analyze professional swings:

Grant Waite (slow motion):
https://www.youtube.com/watch?v=6sD5asBLNrw

Tiger Woods (Driver):
https://www.youtube.com/watch?v=AJzU3NjDikY

Adam Scott (Face-on):
https://www.youtube.com/watch?v=kJYd5ljwN9o

Justin Thomas (High-Speed):
https://www.youtube.com/watch?v=VTde1nxd-vE

Collin Morikawa (Iron):
https://www.youtube.com/watch?v=6n42bbYcNbA

## Folder Structure

    youtube-downloader/
    ├── Dockerfile
    ├── download.py
    └── README.md

## Notes

- Make sure Docker is installed and running on your system.
- Downloads are saved into the /downloads volume inside the container and mapped to your local folder.
- YouTube Shorts and private videos may not work unless they are publicly accessible.
- This container uses the Python yt-dlp library (not the CLI tool), so no need to configure system paths.

## License

MIT License. Use responsibly and follow YouTube’s Terms of Service: https://www.youtube.com/t/terms
