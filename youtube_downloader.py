from pytube import YouTube, Playlist

# menu
menu = """
[1] Video with Audio
[2] Audio Only
[3] Video Playlist
[4] Audio Playlist
[q] Quit
"""


# choice
def choice():
    return str(input("Your Choice: "))


# get video url
def get_url():
    return str(input("Link: "))


if __name__ == "__main__":
    print(menu)
    choice = choice()
    if choice == "1":
        y_link = YouTube(get_url())                         # gets link
        print("Title: ", y_link.title)                      # check if video right
        y_video = y_link.streams.get_by_itag(22)            # get highest res
        y_video.download()                                  # download to current folder
    elif choice == "2":
        y_link = YouTube(get_url())                         # gets link
        print("Title: ", y_link.title)                      # check if audio right
        y_audio = y_link.streams.get_by_itag(140)           # get audio
        y_audio.download()                                  # download to current folder
    elif choice == "3":
        y_link = Playlist(get_url())                        # gets link
        print("Title: ", y_link.title)                      # check if video right
        for video in y_link.videos:                         # download to current folder
            video.streams.get_by_itag(22).download()
    elif choice == "4":
        y_link = Playlist(get_url())                        # gets link
        print("Title: ", y_link.title)                      # check if audio right
        for video in y_link.videos:                         # download to current folder
            video.streams.get_by_itag(140).download()
    elif choice == "q" or choice == "Q":
        quit()
    else:
        input("Invalid entry. Press any button to quit.")
        quit()

