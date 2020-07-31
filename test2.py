from tkinter import *
import pygame


root = Tk()
root.title("Tuturu")
root.geometry("500x300")

pygame.mixer.init()




def play():
    pygame.mixer.music.load('D:\\Python code\\meme_data\\tuturu\\qq.mp3')
    pygame.mixer.music.play()





btn = Button(text="Tuturu ",          # текст кнопки
             background="#c3c11c",     # фоновый цвет кнопки
             foreground="#0047ff",     # цвет текста
             padx="75",             # отступ от границ до содержимого по горизонтали
             pady="50",
             font="Arial 60",
             command = play
             )

btn.pack()
root.mainloop()
