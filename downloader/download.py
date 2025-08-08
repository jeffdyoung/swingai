from yt_dlp import YoutubeDL
import sys

def download_video(url, output_dir="/downloads"):
    ydl_opts = {
        # Get highest resolution video with MP4 + M4A if available
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'cachedir': f'{output_dir}/.cache',
        'noplaylist': True,
        'quiet': False,
        'no_warnings': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download.py <YouTube_URL>")
    else:
        download_video(sys.argv[1])
