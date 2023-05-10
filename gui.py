from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, Label
from PIL import Image, ImageTk
from main import generate_response


# Загрузка диалога из файла
def load_from_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        if filepath[-4::] != '.txt':
            print('это не txt')
        else:
            with open(filepath, 'r', encoding='utf-8') as file:
                clear_bot_input()
                text = file.read() + '\n'
                fill_bot_input(text)


def fill_bot_input(message: str):
    bot_input.insert('1.0', message)


def clear_bot_input():
    bot_input.delete('1.0', 'end')


def clear_user_input():
    user_input.delete('0', 'end')


last_response = ""


# Сюда нужно дописать обработку вывода бота
def process_input():
    global last_response
    text = user_input.get('1.0', 'end').replace('\n', ' ')
    user_input.delete('1.0', 'end')
    response = generate_response(text, last_response)
    last_response = response
    usr_message = '(user): ' + text + '\n'
    bot_input.insert('end', usr_message)
    bot_message = '(bot): ' + response + '\n'
    bot_input.insert('end', bot_message)


def save_dialogue():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        if filepath[-4::] != '.txt':
            print('это не txt')
        else:
            with open(filepath, 'w', encoding='utf-8') as file:
                text = bot_input.get('1.0', 'end')
                file.write(text)


window = Tk()

window.geometry("1278x762")

img = Image.open(r"pics\фон.png")
width = 1278
height = 766
imag = img.resize((width, height), Image.LANCZOS)
image = ImageTk.PhotoImage(imag)
panel = Label(window, image=image)
panel.pack(side="top", fill="both")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=762,
    width=1278,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

canvas.create_rectangle(
    0.0,
    1.0,
    1278.0,
    764.0,
    fill="#FFFFFF",
    outline="")

canvas.create_image(0, 0, anchor="nw", image=image)

canvas.create_rectangle(
    283.0,
    111.0,
    996.0,
    412.0,
    fill="#FBCBC9",
    outline="black")

canvas.create_rectangle(
    283.0,
    436.0,
    996.0,
    604.0,
    fill="#FBCBC8",
    outline="black")

canvas.create_rectangle(
    0.0,
    1.0,
    1278.0,
    71.0,
    fill="#FBCBC9",
    outline="black")

canvas.create_text(
    555.0,
    452.0,
    anchor="nw",
    text="Ваше сообщение",
    fill="#000000",
    font=("Inter Light", 20 * -1)
)

canvas.create_text(
    585.0,
    131.0,
    anchor="nw",
    text="Ответ бога",
    fill="#000000",
    font=("Inter Light", 20 * -1)
)

bot_input = Text(
    bd=0,
    wrap="word",
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0)

fill_bot_input("Hello! I'm a bot that can talk to you about books. (If our conversation reaches a dead end, it means that we are not on the same path sorry)\n")

bot_input.place(
    x=305.0,
    y=168.0,
    width=669.0,
    height=221.0
)

user_input = Text(
    bd=0,
    wrap="word",
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)

user_input.place(
    x=305.0,
    y=493.0,
    width=669.0,
    height=88.0
)

button_image_1 = PhotoImage(
    file=r"pics\button_1.png")

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=save_dialogue,
    relief="flat"
)
button_1.place(
    x=1017.0,
    y=11.0,
    width=247.0,
    height=46.0
)

button_image_2 = PhotoImage(
    file=r"pics\button_2.png")

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=load_from_file,
    relief="flat"
)
button_2.place(
    x=744.0,
    y=11.0,
    width=247.0,
    height=45.2203369140625
)

button_image_3 = PhotoImage(
    file=r"pics\button_3.png")

button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=process_input,
    relief="flat"
)
button_3.place(
    x=283.0,
    y=628.0,
    width=713.0,
    height=58.0
)
window.resizable(False, False)
window.mainloop()
