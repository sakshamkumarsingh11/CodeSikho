import tkinter as tk
import random

def generate_random_color():
    """Generate a random color in hexadecimal format."""
    return f'#{random.randint(0, 0xFFFFFF):06x}'

def update_palette():
    """Update the color palette with random colors."""
    for color_frame in color_frames:
        color = generate_random_color()
        color_frame.config(bg=color)

# Create the main window
root = tk.Tk()
root.title("Random Color Palette")

# Create a frame to hold the color palette
palette_frame = tk.Frame(root)
palette_frame.pack(pady=20)

# Create a list to hold color frames
color_frames = []

# Create color frames
for _ in range(5):  # Create 5 color frames
    frame = tk.Frame(palette_frame, width=100, height=100, bg='white', relief=tk.RAISED)
    frame.pack(side=tk.LEFT, padx=5)
    color_frames.append(frame)

# Create a button to generate the color palette
generate_button = tk.Button(root, text="Generate Random Colors", command=update_palette)
generate_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()