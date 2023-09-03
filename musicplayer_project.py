import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
import pygame
import os
from PIL import Image, ImageTk

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Music Player")

        self.playlist = []
        self.current_index = 0


        pygame.mixer.init()

        
        self.create_gui()

    def create_gui(self):
        
        self.playlist_box = tk.Listbox(self.root, selectmode=tk.SINGLE, bg="black", fg="white", selectbackground="blue")
        self.playlist_box.pack(fill=tk.BOTH, expand=True)

        
        controls_frame = tk.Frame(self.root)
        controls_frame.pack()

        self.play_button = tk.Button(controls_frame, text="Play", command=self.play_music)
        self.pause_button = tk.Button(controls_frame, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(controls_frame, text="Stop", command=self.stop_music)
        self.next_button = tk.Button(controls_frame, text="Next", command=self.next_song)
        self.prev_button = tk.Button(controls_frame, text="Previous", command=self.prev_song)

        self.play_button.grid(row=0, column=0, padx=10)
        self.pause_button.grid(row=0, column=1, padx=10)
        self.stop_button.grid(row=0, column=2, padx=10)
        self.prev_button.grid(row=0, column=3, padx=10)
        self.next_button.grid(row=0, column=4, padx=10)

        
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.add_music)

    def add_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")])
        if file_path:
            self.playlist.append(file_path)
            song_name = os.path.basename(file_path)
            self.playlist_box.insert(tk.END, song_name)

    def play_music(self):
        if self.playlist:
            current_song = self.playlist[self.current_index]
            pygame.mixer.music.load(current_song)
            pygame.mixer.music.play()

            
            image_path = 'Varsham.jpg'  
            self.display_image('Varsham.jpg')

    def display_image(self,image_path):
        image_path='Varsham.jpg'
        image = Image.open('Varsham.jpg')
        image = image.resize((150, 150))

        photo = ImageTk.PhotoImage(image)

        
        self.image_label.config(image=photo)
        self.image_label.image = photo  

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_song(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play_music()

    def prev_song(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
