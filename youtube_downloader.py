from pytube import YouTube

# menu
menu = """
[1] Video with Audio
[2] Audio Only
[q] Quit
"""


# choice
def choice():
    return str(input("Your Choice: "))


# get video url
def get_url():
    return str(input("Link of the video: "))


if __name__ == "__main__":
    print(menu)
    choice = choice()
    if choice == "1":
        y_link = YouTube(get_url())
        print("Title: ", y_link.title)                      # check if video right
        y_video = y_link.streams.get_highest_resolution()   # get highest res
        y_video.download()                                  # download to folder
    elif choice == "2":
        y_link = YouTube(get_url())
        print("Title: ", y_link.title)                      # check if video right
        y_audio = y_link.streams.get_audio_only()           # get audio
        y_audio.download()                                  # download to folder
    elif choice == "q" or choice == "Q":
        quit()
    else:
        input("Invalid entry. Press any button to quit.")
        quit()

