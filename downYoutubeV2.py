from yt_dlp import YoutubeDL
import os
destino="/storage/emulated/0/Download/videosEmusicasTube"
url = input("digite a url do video: ")
while True:
	print("(1) video (2) audio (3) sair")
	choice=input("escolha a opção: ")
	def baixarvideo(choice):
	        			if choice=="1":
	        				options = {
	        				'format': 'best',
	        				'outtmpl':os.path.join(destino, '%(title)s.%(ext)s'),
	        				}
	        				with YoutubeDL(options) as ydl:
	        					ydl.download([url])
	        			elif choice=="2":
	        				options = {
	        				'format': 'bestaudio',  # Melhor qualidade de áudio
	        				'outtmpl': os.path.join(destino, '%(title)s.mp3'),
	        				}
	        				with YoutubeDL(options) as ydl:
	        					info=ydl.extract_info(url, download=True)
	if choice=="3":
	    break
	baixarvideo(choice)
	