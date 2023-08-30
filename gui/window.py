import tkinter as tk
from tkinter import font

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

window = tk.Tk()
window.title("Chat Hackton")
window.geometry("1000x750")
window.resizable(False, False)
window.config(bg='#4fe3a5')

font1 = font.Font(family='Georgia', size=22, weight='bold')  # Font


def chat_window_widget(root, name):
    # img = tk.PhotoImage(file='../../../PycharmProjects/gui/images/send_btn.png')
    tk.Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text=name, font=FONT_BOLD, pady=10, width=20, height=1).grid(
        row=0)

    txt = tk.Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)

    scrollbar = tk.Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)

    e = tk.Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)

    tk.Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=lambda: send(e, txt)).grid(row=2, column=1)


def change_to_main_window():
    name = name_var.get()
    name_var.set("")
    chat_screen.pack(fill='both', expand=1)
    login_btn.destroy()
    name_entry.destroy()
    welcome_text.destroy()
    window.destroy()
    chat_window = tk.Tk()
    chat_window_widget(chat_window, name)


# ______________________________________________________________________#

def create_chat_screen():
    tk.Label(chat_screen, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
        row=0)

    txt = tk.Text(chat_screen, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)

    scrollbar = tk.Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)

    e = tk.Entry(chat_screen, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)

    tk.Button(chat_screen, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1).grid(row=2, column=1)


def send(e, txt):
    submit = "You -> " + e.get()
    txt.insert(tk.END, "\n" + submit)

    e.delete(0, tk.END)


# ______________________________________________________________________#
chat_screen = tk.Frame(window)
name_var = tk.StringVar()

# Widgets in the screen
welcome_text = tk.Label(window, text="Welcome! Sign in", foreground="blue", font=font1, justify="center")
# empty_text = tk.Label(chat_screen, text="You're in!", foreground="blue", font=font1, justify="center")

login_btn = tk.Button(window, text="Sign in", font=font1, command=change_to_main_window, justify="center")

name_entry = tk.Entry(window, textvariable=name_var, font=('calibre', 10, 'normal'), )

name_entry.pack()
welcome_text.pack()
login_btn.pack(pady=20)
name_entry.place(relx=0.5, rely=0.5, anchor="center")
welcome_text.place(relx=0.5, rely=0.4, anchor="center")
login_btn.place(relx=0.5, rely=0.57, anchor="center")
chat_screen.pack()

# empty_text.pack()

window.mainloop()
