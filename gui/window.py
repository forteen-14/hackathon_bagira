import os
import tkinter as tk
from tkinter import font
import socket
import consts
import user
import time

window = tk.Tk()
window.title("Chat Hackathon")
window.geometry("1000x750")
window.resizable(False, False)
window.config(bg='#4fe3a5')

font1 = font.Font(family='Georgia', size=22, weight='bold')  # Font
user = user.User("name", 0, 0)


def start_connection():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((consts.IP, consts.PORT))
    return client


def send_msg_to_everyone(catagory, msg, client):
    msg_to_send = f"{consts.SEND}#{user.name}#{catagory}#{msg}"
    client.sendall(bytes(str(msg_to_send), 'UTF-8'))


def login(client):
    # we would get that from gui
    user_name = "idk"
    msg_to_send = f"{consts.LOGIN}#{user_name}"
    client.sendall(bytes(str(msg_to_send), 'UTF-8'))
    time.sleep(0.1)
    get_user_info(client)


def get_user_info(client):
    data = client.recv(1024)
    sever_msg = data.decode()
    user_info = sever_msg.split("#")
    user.name = user_info[1]
    user.help_given = user_info[2]
    user.help_got = user_info[3]


def upload_msg_at_login(client):
    msg_to_send = f"{consts.UPLOAD_MSG_AT_LOGIN}"


def keep_connection(client):
    login(client)
    send_msg_to_everyone(consts.DANGER, "im stuck", client)


def subject_chat_window(root, client, name, subject):
    root.title("Chat Hackathon")
    root.geometry("1000x630")
    root.resizable(False, False)

    tk.Label(root, bg=consts.BG_COLOR, fg=consts.TEXT_COLOR, text=subject, font=consts.FONT_BOLD, pady=10, width=20,
             height=1).grid(row=0, column=1)

    txt = tk.Text(root, bg=consts.BG_COLOR, fg=consts.TEXT_COLOR, font=consts.FONT, width=75, height=25)
    txt.grid(row=1, column=2)

    scrollbar = tk.Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)

    e = tk.Entry(root, bg="#2C3E50", fg=consts.TEXT_COLOR, font=consts.FONT, width=35)
    e.grid(row=3, column=2)
    tk.Button(root, text="Send", font=consts.FONT_BOLD, bg=consts.BG_GRAY,
              command=lambda: send(e, txt, name, client)).place(x=810, y=595)


def chat_window_widget(root, client, name="No name"):
    root.title("Chat Hackathon")
    root.geometry("1000x630")
    root.resizable(False, False)
    tk.Label(root, bg=consts.BG_COLOR, fg=consts.TEXT_COLOR, text=consts.GENERAL, font=consts.FONT_BOLD, pady=10,
             width=20,
             height=1).grid(row=0, column=1)

    txt = tk.Text(root, bg=consts.BG_COLOR, fg=consts.TEXT_COLOR, font=consts.FONT, width=75, height=25)
    txt.grid(row=1, column=2)

    scrollbar = tk.Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)

    e = tk.Entry(root, bg="#2C3E50", fg=consts.TEXT_COLOR, font=consts.FONT, width=35)
    e.grid(row=3, column=2)
    img = tk.PhotoImage(file='not_not.jpg')

    tk.Button(root,image=img ,text="Send", font=consts.FONT_BOLD, bg=consts.BG_GRAY,
              command=lambda: send(e, txt, name, client)).place(x=810, y=595)

    # User rating
    help_give_rating = 0
    help_got_rating = 0

    label_text = tk.StringVar()
    label_text.set(name + "\n\n" + "help give: \n" + str(help_give_rating)
                   + " stars" "\n\n" + "help got: \n" + str(help_got_rating) + " stars")

    tk.Label(root, bg="#B0E0E6", fg="Green", textvariable=label_text, font=consts.FONT_BOLD, pady=2, width=10,
             height=31, anchor='n').place(x=0, y=45)

    label_category = tk.StringVar()
    label_category.set("category")

    tk.Label(root, bg="#B0E0E6", fg="Red", textvariable=label_category, font=consts.FONT_BOLD, pady=2, width=10,
             height=31, anchor='n').place(x=100, y=45)

    tk.Button(root, text=consts.CAR_HELP, font=consts.FONT_BOLD, bg=consts.BG_GRAY,
              command=lambda: subject_chat_window(root, client, name, consts.CAR_HELP), width=8, height=5).place(x=110,
                                                                                                                 y=80)
    tk.Button(root, text=consts.RESCUE_FROM_ELEVATOR, font=consts.FONT_BOLD, bg=consts.BG_GRAY,
              command=lambda: subject_chat_window(root, client, name, consts.RESCUE_FROM_ELEVATOR), width=8,
              height=5).place(x=110, y=180)
    tk.Button(root, text=consts.RESCUE_FROM_HARSH_CONDITIONS, font=consts.FONT_BOLD, bg=consts.BG_GRAY,
              command=lambda: subject_chat_window(root, client, name, consts.RESCUE_FROM_HARSH_CONDITIONS), width=8,
              height=5).place(x=110, y=280)
    tk.Button(root, text=consts.DANGER, font=consts.FONT_BOLD, bg=consts.BG_GRAY,
              command=lambda: subject_chat_window(root, client, name, consts.DANGER), width=8, height=5).place(x=110,
                                                                                                               y=380)


def change_to_main_window(client):
    name = name_var.get()
    name_var.set("")
    chat_screen.pack(fill='both', expand=1)
    login_btn.destroy()
    name_entry.destroy()
    welcome_text.destroy()
    window.destroy()
    chat_window = tk.Tk()
    login(client)
    chat_window_widget(chat_window, client, name)


def send(e, txt, username, client):
    msg = e.get()
    txt.insert(tk.END, "\n" + username + ": " + msg)
    send_msg_to_everyone("", msg, client)
    e.delete(0, tk.END)


chat_screen = tk.Frame(window)
name_var = tk.StringVar()

# Widgets in the screen
welcome_text = tk.Label(window, text="Welcome! Sign in", foreground="blue", font=font1, justify="center")

login_btn = tk.Button(window, text="Sign in", font=font1, command=lambda: change_to_main_window(client),
                      justify="center")

name_entry = tk.Entry(window, textvariable=name_var, font=('calibre', 10, 'normal'), )

name_entry.pack()
welcome_text.pack()
login_btn.pack(pady=20)
name_entry.place(relx=0.5, rely=0.5, anchor="center")
welcome_text.place(relx=0.5, rely=0.4, anchor="center")
login_btn.place(relx=0.5, rely=0.57, anchor="center")
chat_screen.pack()

try:
    client = start_connection()
    keep_connection(client)
except:
    print("ERROR: Connection failed")

window.mainloop()
