from tkinter import *
import pygame

pygame.mixer.init()

root = Tk()
root.title("Simple Music Player")
root.geometry("300x200")

pygame.mixer.music.load("song.mp3")

# Functions
def play_music():
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

# Buttons
Button(root, text="Play", command=play_music).pack(pady=5)
Button(root, text="Pause", command=pause_music).pack(pady=5)
Button(root, text="Resume", command=resume_music).pack(pady=5)
Button(root, text="Stop", command=stop_music).pack(pady=5)

root.mainloop()
