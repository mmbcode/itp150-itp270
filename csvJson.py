import json
import os 

def readJson ():
    if os.path.isfile("songs.json"):
        filePointer = open("songs.json","r")
        catalog = json.load(filePointer)
        songs = catalog.get("songlist")
        return songs
    else:
        return False

def selectSong (catalog):
    playlist = []
    while True:
        print(f"Here are your song options:\n")
        count = 1
        
        for song in catalog:
            title = song.get("title")
            artist = song.get("artist")
            print (f"{count}. {title} by {artist}\n")
            count+=1

        while True:
            choice = input(f"Choose a song to add to your playlist:(1-{count-1}): ")
            if choice.isdigit() and int(choice) > 0 and int(choice) < count:
                choice = int(choice) -1
                break
            else:
                print("Invalid selection, please try agian.")
        
        selected = catalog[choice]
        addSong = [selected.get("artist"),selected.get("title"),selected.get("year")]
        playlist.append(addSong)

        addMore = input("Press Y to add more songs or return to continue: ").upper()
        if addMore != "Y":
            break
    return playlist

def writeCSV(songs):
    outputCSV = open("playlist.csv","w")
    outputCSV.write(f"Artist,Title,Year\n")
    for song in songs:
        outputCSV.write(f"{song[0]},{song[1]},{song[2]}\n")
    outputCSV.close()

def main ():
    songs = readJson()
    if songs != False:
        playList = selectSong(songs)
        writeCSV(playList)
    else:
        print("JSON input file doesn't exist, quiting\n\n")
main()
