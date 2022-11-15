#!/usr/bin/env python3

from pytube import YouTube

def download_playlist():
	video = YouTube(input("Insira a URL do vídeo de que deseja efetuar o download: "))
	print(f"Downloading: {video.title}")
	video.streams.filter(file_extension="mp4").first().download()
	print("Download concluído.")

download_playlist()

