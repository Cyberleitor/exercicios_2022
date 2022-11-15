#!/usr/bin/env python3.9

from pytube import YouTube

def download_audio():
	audio = YouTube(input("Insira a URL do vídeo de que deseja efetuar o download do aúdio: "))
	print(f"Downloading: {audio.title}")
	audio.streams.filter(only_audio=True).get_audio_only().download()
	print("Download concluído.")

download_audio()

