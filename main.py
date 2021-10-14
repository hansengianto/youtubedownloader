from pytube import YouTube

outputpath = "D:/"

intro = f"""========================================
Youtube Video Downloader
Source : github.com/hansengianto
Download Path : {outputpath}
(Edit main.py to change the path)
========================================"""


def main():
	print(intro)
	link = input("Input Youtube Link To Download : ")

	video = YouTube(link)
	stream = video.streams.get_highest_resolution()
	stream.download(output_path = outputpath)
	print(f"Success Download Video In {outputpath} Folder\n\n\n\n\n")

while True:
	main()
