from tkinter import *
from pygame import mixer
import os
class Player:
    def __init__(self, root):
        self.root = root
        self.root.title("Music player")
        self.root.geometry("500x200")
        self.play_btn_img = PhotoImage(file="img\\play-button.png")
        self.pause_btn_img = PhotoImage(file="img\\pause-button.png")
        self.song_play_btn_img = PhotoImage(file="img\\play-button (1).png")
        self.backward_btn_img = PhotoImage(file="img\\back-backward-button.png")
        self.forward_btn_img = PhotoImage(file="img\\fast-forward-button.png")
        self.player_img = PhotoImage(file="img\\music.png")
        self.x = 0
        mixer.init()

        self.button_frame = Frame(root, bd=1, relief=GROOVE)
        self.button_frame.place(x=0, y=0, width=200, height=200)
        song_frame = Frame(root,bd=5,relief=GROOVE)
        song_frame.place(x=200, y=0, width=300, height=200)
        scroll = Scrollbar(song_frame, orient=VERTICAL)
        self.playlist = Listbox(song_frame, yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        self.playlist.pack(fill=BOTH)

        os.chdir("C:\\Users\\maashree\\Music")
        self.song_track = os.listdir()

        for i in self.song_track:
            self.playlist.insert(END, i)

        self.play(self.x)
        self.img_label = Label(self.button_frame, image=self.player_img).place(x=0, y=0)
        self.play_btn = Button(self.button_frame, image=self.pause_btn_img, command=self.pause)
        self.play_btn.place(x=70, y=130)
        self.backward_btn = Button(self.button_frame, image=self.backward_btn_img, command=self.backward)
        self.backward_btn.place(x=10, y=130)
        self.forward_btn = Button(self.button_frame, image=self.forward_btn_img, command=self.forward)
        self.forward_btn.place(x=130, y=130)

    def forward(self):
        self.x += 1
        self.play(self.x)

    def backward(self):
        self.x -= 1
        self.play(self.x)

    def play(self, x):
        mixer.music.load(self.song_track[x])
        mixer.music.play()
        Label(self.button_frame, font=("arial",10), fg="blue",text=self.song_track[x]).place(x=70, y=30)

    def pause(self):
        if self.play_btn["image"]==str(self.pause_btn_img):
            mixer.music.pause()
            self.play_btn.config(image=self.play_btn_img)
        elif self.play_btn["image"]==str(self.play_btn_img):
            mixer.music.unpause()
            self.play_btn.config(image=self.pause_btn_img)

root = Tk()
obj = Player(root)
mainloop()