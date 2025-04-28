import tkinter as tk
from tkinter import messagebox
import style  # ✅ This is how you connect CSS-like file

def action(name):
    messagebox.showinfo("Action", f"You clicked {name}!")

# Window setup
root = tk.Tk()
root.title("Profile Content")
root.geometry("700x800")
root.configure(bg=style.BACKGROUND_COLOR)

# Heading
heading = tk.Label(
    root,
    text="CHECK MY PROFILE FOR MORE",
    font=style.HEADING_FONT,
    bg=style.BACKGROUND_COLOR
)
heading.pack(pady=(30, 20))

# Content Frames
content_frame = tk.Frame(root, bg=style.BACKGROUND_COLOR)
content_frame.pack(pady=10, padx=20, fill="both", expand=True)

# Left Side (Text + Icons)
left_frame = tk.Frame(content_frame, bg=style.BACKGROUND_COLOR)
left_frame.pack(side="left", anchor="n", padx=(30, 10), pady=10)

items = [
    ("👥", "Interviews"),
    ("📝", "Notes"),
    ("🧙‍♂️", "Explanations"),
    ("🗺️", "RoadMaps")
]

for icon, text in items:
    row = tk.Frame(left_frame, bg=style.BACKGROUND_COLOR)
    row.pack(anchor="w", pady=10)

    text_label = tk.Label(row, text=text, font=style.ITEM_FONT, bg=style.BACKGROUND_COLOR)
    text_label.pack(side="right", padx=10)

    icon_label = tk.Label(row, text=icon, font=style.ICON_FONT, bg=style.BACKGROUND_COLOR)
    icon_label.pack(side="right", padx=10)

follow_label = tk.Label(
    left_frame,
    text="follow for more!",
    font=style.FOLLOW_FONT,
    bg=style.BACKGROUND_COLOR
)
follow_label.pack(pady=(30, 0), anchor="w")

# Right Side (Buttons)
right_frame = tk.Frame(content_frame, bg=style.BACKGROUND_COLOR)
right_frame.pack(side="right", anchor="n", padx=(10, 30), pady=10)

buttons = [
    ("♡", "Like"),
    ("💬", "Comment"),
    ("✈️", "Share"),
    ("🔖", "Save")
]

for icon, name in buttons:
    btn = tk.Button(
        right_frame,
        text=f"{icon}\n{name}",
        font=style.BUTTON_FONT,
        bg=style.BUTTON_BG,
        fg=style.BUTTON_FG,
        activebackground=style.ACTIVE_BG,
        activeforeground=style.ACTIVE_FG,
        width=style.BUTTON_WIDTH,
        height=style.BUTTON_HEIGHT,
        bd=0,
        relief="solid",
        command=lambda n=name: action(n)
    )
    btn.pack(pady=10)

root.mainloop()
