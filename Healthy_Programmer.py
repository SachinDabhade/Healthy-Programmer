# ******************************* Healthy Programmers Exercise *****************************************

# Importing Libraries
from pygame import mixer
from datetime import datetime
from time import sleep

# Welcome Screen
print("\nWelcome to HEALTHY PROGRAMME by Sachin Dabhade\n")
sleep(1)
name = input("Enter your name: ")
print("Hello " + name.capitalize() + "! Best of Luck for your coding practice!")
sleep(1)
print("\nI will take care of your health...!\n Let's start programming!")

# This is the music loop
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        a = input("\nPress any key to stop the alarm:\nEnter \"Quit\" to stop the programme:")
        if a.capitalize() == stopper:
            quit()
        else:
            mixer.music.stop()
        break

# This will record all the login of the user on perticular datetime
def login(msg):
    global name
    with open("record.txt", "a") as f:
        f.write(f"{name.capitalize()} has {msg} on {datetime.now()}\n")

# This will record all the activities done by the user on perticular datetime
def log_now(msg):
    global name
    with open("record.txt", "a") as f:
        f.write(f"{name} has done {msg} on {datetime.now()}\n")

# This will sleep the programme for some seconde
def sleep_programme():
    sleep(60 * 30)

if __name__ == '__main__':
    login("started coding")

    while True:
        sleep_programme()
        print("\n\nEye Exercise Time...")
        musiconloop("C:\\Water.mp3", "Quit")
        log_now("Eye Exercise")

        sleep_programme()
        print("\n\nWater Drinking Time...")
        musiconloop('C:\\Water.mp3', 'Quit')
        log_now("Water Drink")

        sleep_programme()
        print("\n\nEye Exercise Time...")
        musiconloop("C:\\Water.mp3", "Quit")
        log_now("Eye Exercise")

        sleep_programme()
        print("\n\nPhysical Exercise Time...")
        musiconloop("C:\\Water.mp3", "Quit")
        log_now("Physical Exercise")
        continue
