import subprocess
import sys
import os

def download_video(url, output_dir="."):
    try:
        output_template = os.path.join(output_dir, "%(title)s.%(ext)s")
        command = [
            "yt-dlp",
            "-f", "bestvideo+bestaudio",
            "-o", output_template,
            url
        ]
        subprocess.run(command, check=True)
        print("✅ Download complete.")
    except subprocess.CalledProcessError as e:
        print(f"❌ yt-dlp failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_youtube_video.py <YouTube_URL>")
    else:
        download_video(sys.argv[1])
