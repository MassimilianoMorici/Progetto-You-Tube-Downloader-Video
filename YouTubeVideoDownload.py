from pytube import YouTube
import sys

link = sys.argv[1]

try:
    yt = YouTube(link)
    print("Titolo: ", yt.title)
    print("Visualizzazioni: ", yt.views)

    yd = yt.streams.get_highest_resolution()

    # Usa un percorso valido per la tua cartella di destinazione
    destination_folder = r'C:\Users\Max\Videos'

    yd.download(destination_folder)
    print("\nDownload completato!")

except Exception as e:
    print("\nSi è verificato un errore:", str(e))
