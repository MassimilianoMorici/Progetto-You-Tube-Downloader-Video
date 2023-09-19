from pytube import YouTube
import sys

link = sys.argv[1]

try:
    yt = YouTube(link)
    print("\nTitolo: ", yt.title)
    

    yd = yt.streams.get_highest_resolution()

    # Usa un percorso valido per la tua cartella di destinazione
    destination_folder = r'C:\Users\Max\Videos'

    yd.download(destination_folder)
    print("\nDownload completato!\n")

except Exception as e:
    print("\nSi è verificato un errore:", str(e))
