# bad apple
import sys, time, os
import pygame


# check os
if os.name == "posix":
    run_on = "linux"
else:
    run_on = "windows"


def player():
    "reads txt file and when it gets 'S', perform a clear sceen command"

    with open('data/badapple.txt', 'r') as file:
        while True:
            video_file = file.read(1)
            if not video_file:
                break

            # print 1 char
            print(video_file, end="")

            # if char is S, wait and clear the screen
            if video_file == "S":
                time.sleep(.0858)
                if run_on == "linux":
                    os.system('clear')  # if mac/linux
                else:
                    os.system('cls')  # if windows


def music():
    "plays music"
    
    if run_on == "linux":
        pygame.init()  # if mac/linux only

    pygame.mixer.init()
    pygame.mixer.music.load('data/badapple.ogg')
    pygame.mixer.music.play()


# set terminal window to 101x29 chars (works on mac/linux only)
sys.stdout.write("\x1b[8;29;101t")

music()
player()
print("Finished")
