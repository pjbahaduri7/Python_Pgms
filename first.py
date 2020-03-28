from pytube import YouTube
link = input("Enter the link: \n")
YouTube(link).streams.first().download()