import yt_dlp
from moviepy.editor import AudioFileClip
import os

# Path to the text file containing YouTube URLs
urls_file_path = 'list.txt'

# Directory where audio files will be saved
output_dir = 'audio_files'
os.makedirs(output_dir, exist_ok=True)

def download_audio(url, output_dir):
    try:
        # Download the video
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_dir, 'temp.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '1080',
            }],
        }

        print(f"Downloading {url}...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Rename file to the video title
        video_info = yt_dlp.YoutubeDL().extract_info(url, download=False)
        audio_path = os.path.join(output_dir, video_info['title'] + '.mp3')
        temp_file = os.path.join(output_dir, 'temp.mp3')

        os.rename(temp_file, audio_path)
        print(f"Audio extracted and saved as {audio_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls

# Read URLs from the text file
video_urls = read_urls_from_file(urls_file_path)

# Download audio for each URL in the list
for url in video_urls:
    download_audio(url, output_dir)






