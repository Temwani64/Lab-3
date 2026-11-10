
import tkinter as tk
import random
import string
import pygame

# 1. KEY GENERATOR - VARIANT 9
def generate_key():
    numbers = random.sample(range(1, 27), 2)

    start = min(numbers)
    end = max(numbers)

    alphabet = string.ascii_uppercase

    letters = alphabet[start - 1:end]

    middle = ''.join(random.choices(letters, k=7))

    key = f"{start:02d} {middle} {end:02d}"

    return key

# 2. GENERATE KEY
def generate():
    key = generate_key()

    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)

    status.config(text="NEW KEY GENERATED!")

# 3. COPY KEY
def copy_key():
    key = key_entry.get()

    if key:
        root.clipboard_clear()
        root.clipboard_append(key)

        status.config(text="KEY COPIED!")

# 4. MUSIC FUNCTIONS
music_paused = False

def play_music():
    global music_paused

    if music_available:
        if music_paused:
            pygame.mixer.music.unpause()
            music_paused = False
        elif not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

        music_status.config(text="MUSIC: PLAYING")

def pause_music():
    global music_paused

    if music_available:
        pygame.mixer.music.pause()
        music_paused = True

        music_status.config(text="MUSIC: PAUSED")

def stop_music():
    global music_paused

    if music_available:
        pygame.mixer.music.stop()
        music_paused = False

        music_status.config(text="MUSIC: STOPPED")

# 5. MAIN WINDOW
root = tk.Tk()

root.title("Key Generator - Variant 9")
root.geometry("900x600")
root.resizable(False, False)

# 6. BACKGROUND IMAGE
background = tk.PhotoImage(file="background.png")

background_label = tk.Label(
    root,
    image=background
)

background_label.place(
    x=0,
    y=0,
    relwidth=1,
    relheight=1
)

background_label.lower()

# 7. TITLE
title = tk.Label(
    root,
    text="MINECRAFT KEY GENERATOR",
    font=("Arial", 26, "bold"),
    fg="white",
    bg="#20252E"
)

title.pack(pady=60)

# 8. KEY DISPLAY
key_entry = tk.Entry(
    root,
    font=("Consolas", 20, "bold"),
    width=22,
    justify="center",
    bg="#20252E",
    fg="#00FF99",
    relief="flat"
)

key_entry.pack(pady=20, ipady=10)

# 9. GENERATE BUTTON
generate_button = tk.Button(
    root,
    text="GENERATE KEY",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    command=generate
)
generate_button.pack(pady=15, ipadx=25, ipady=10)

# 10. COPY BUTTON
copy_button = tk.Button(
    root,
    text="COPY KEY",
    font=("Arial", 12, "bold"),
    bg="#39465C",
    fg="white",
    command=copy_key
)
copy_button.pack(pady=10, ipadx=30, ipady=8)

# 11. STATUS MESSAGE
status = tk.Label(
    root,
    text="READY TO GENERATE",
    font=("Arial", 11, "bold"),
    fg="#00FF99",
    bg="#20252E"
)

status.pack(pady=15)

# 12. TITLE ANIMATION
def animate():
    if title["fg"] == "white":
        title.config(fg="#00FF99")
    else:
        title.config(fg="white")

    root.after(700, animate)

# 13. INITIALIZE MUSIC
music_available = False

try:
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.set_volume(0.3)

    music_available = True

except pygame.error:
    print("Music file could not be loaded.")

# 14. MUSIC CONTROLS
music_status = tk.Label(
    root,
    text="MUSIC: STOPPED",
    font=("Arial", 10, "bold"),
    fg="#00FF99",
    bg="#20252E"
)
music_status.pack(pady=5)

music_frame = tk.Frame(root, bg="#20252E")
music_frame.pack()

play_button = tk.Button(
    music_frame,
    text="PLAY",
    command=play_music,
    bg="green",
    fg="white"
)
play_button.pack(side="left", padx=5)
pause_button = tk.Button(
    music_frame,
    text="PAUSE",
    command=pause_music,
    bg="orange",
    fg="white"
)
pause_button.pack(side="left", padx=5)
stop_button = tk.Button(
    music_frame,
    text="STOP",
    command=stop_music,
    bg="red",
    fg="white"
)
stop_button.pack(side="left", padx=5)

# 15. START APPLICATION
generate()
animate()
play_music()

root.mainloop()
