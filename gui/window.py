import tkinter as tk
from tkinter import font
import consts

window = tk.Tk()
window.title("Chat Hackathon")
window.geometry("1000x750")
window.resizable(False, False)
window.config(bg='#4fe3a5')

font1 = font.Font(family='Georgia', size=22, weight='bold')  # Font


def chat_window_widget(root, name):
    root.title("Chat Hackathon")
    # img = tk.PhotoImage(file=r'../../../PycharmProjects/gui/images/send_btn.png')
    # img = img.subsample(2, 2)
    # tk.Label(root, bg=consts.BG_COLOR, fg=consts.TEXT_COLOR, text=name, font=consts.FONT_BOLD, pady=10,
    #          width=20, height=1).grid(row=0)

    txt = tk.Text(root, bg=consts.BG_COLOR, fg=consts.TEXT_COLOR, font=consts.FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)

    scrollbar = tk.Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)

    e = tk.Entry(root, bg="#2C3E50", fg=consts.TEXT_COLOR, font=consts.FONT, width=55)
    e.grid(row=2, column=0)

    tk.Button(root, text="Send", font=consts.FONT_BOLD, bg=consts.BG_GRAY,
              command=lambda: send(e, txt)).grid(row=2, column=1)

    help_give_rating = 0
    help_got_rating = 0

    tk.Label(root, bg="#B0E0E6", fg="Green", text=name+"\n\n"+"help give: " + str(help_give_rating)
             + "\n\n" + "help got: " + str(help_got_rating), font=consts.FONT_BOLD, pady=2,
             width=10, height=35, anchor='n').place(x=0, y=0)


def change_to_main_window():
    name = name_var.get()
    name_var.set("")

    # Removing all widgets from window
    login_btn.destroy()
    name_entry.destroy()
    welcome_text.destroy()
    window.destroy()

    # Creating chat window
    chat_window = tk.Tk()
    chat_window_widget(chat_window, name)


def send(e, txt):
    submit = "You -> " + e.get()
    txt.insert(tk.END, "\n" + submit)

    e.delete(0, tk.END)


name_var = tk.StringVar()

# Widgets in the screen
welcome_text = tk.Label(window, text="Welcome! Sign in", foreground="blue", font=font1, justify="center")

login_btn = tk.Button(window, text="Sign in", font=font1, command=change_to_main_window, justify="center")

name_entry = tk.Entry(window, textvariable=name_var, font=('calibre', 10, 'normal'), )

name_entry.pack()
welcome_text.pack()
login_btn.pack(pady=20)
name_entry.place(relx=0.5, rely=0.5, anchor="center")
welcome_text.place(relx=0.5, rely=0.4, anchor="center")
login_btn.place(relx=0.5, rely=0.57, anchor="center")

window.mainloop()
