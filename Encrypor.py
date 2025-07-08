from tkinter import *
import customtkinter
import ctypes

def encryptor_input(new_alphabet):
    global alphabet

def encrypt_alphabet(direction, ammount):
    global alphabet

    ammount = ammount % 26
    new_alphabet = alphabet
    
    if direction == "L":
        new_alphabet.extend(new_alphabet[0:ammount])
        del(new_alphabet[0:ammount])
    elif direction == "R":
        temp = new_alphabet[-ammount:]
        temp.extend(new_alphabet)
        new_alphabet = temp
        del(new_alphabet[-ammount:])
        
    return new_alphabet

def key_change(key_string):
    global page, alphabet

    key_string = key_string.get()

    if page == "Lvl. 1":
        try:
            if key_string[0] not in ["L", "R"]:
                ctypes.windll.user32.MessageBoxW(0, "Key Must Begin With L or R", "WARNING:", 1)
            
            new_alphabet = encrypt_alphabet(key_string[0], int(key_string[1:]))

            encryptor_input(new_alphabet)
        except:
            pass

def lvl_1_page():
    global content, page

    page = "Lvl. 1"

    content.destroy()

    menu_frame.rowconfigure(0, weight = 1, minsize = 20)
    menu_frame.rowconfigure(1, weight = 100000, minsize = 20)
    menu_frame.columnconfigure(0, weight = 9)
    menu_frame.columnconfigure(1, weight = 1)

    content = customtkinter.CTkFrame(menu_frame, fg_color = "transparent")

    content.grid(row=1, column = 0, columnspan = 2, rowspan = 1, sticky = "nsew")

    content.rowconfigure(0, weight = 100000, minsize = 40)
    content.rowconfigure(1, weight = 1, minsize = 20)
    content.rowconfigure(2, weight = 100000, minsize = 40)

    content.columnconfigure(0, weight = 1)

    text_in = customtkinter.CTkTextbox(content, wrap = "word")
    text_in.grid(row = 0, column = 0, columnspan = 1, sticky = "nsew", padx = 10, pady = 10)

    key_box = StringVar()
    key_box.trace("w", lambda name, index, mode, key_box=key_box: key_change(key_box))

    key = customtkinter.CTkEntry(content, placeholder_text = "Key", font = ("TkDefaultFont", 20), width = 400, textvariable = key_box)
    key.grid(row = 1, column = 0, padx = 10)

    text_out = customtkinter.CTkTextbox(content, wrap = "word")
    text_out.grid(row = 2, column = 0, columnspan = 1, rowspan = 1, sticky = "nsew", padx = 10, pady = 10)

def lvl_2_page():
    global content, page

    content.destroy()

    menu_frame.rowconfigure(0, weight = 1, minsize = 20)
    menu_frame.rowconfigure(1, weight = 100000, minsize = 20)
    menu_frame.columnconfigure(0, weight = 9)
    menu_frame.columnconfigure(1, weight = 1)

    content = customtkinter.CTkFrame(menu_frame, fg_color = "transparent")

    content.grid(row=1, column = 0, columnspan = 2, rowspan = 1, sticky = "nsew")

    content.rowconfigure(0, weight = 100000, minsize = 40)
    content.rowconfigure(1, weight = 1, minsize = 20)
    content.rowconfigure(2, weight = 100000, minsize = 40)

    content.columnconfigure(0, weight = 1)

    text_in = customtkinter.CTkTextbox(content, wrap = "word")
    text_in.grid(row = 0, column = 0, columnspan = 1, sticky = "nsew", padx = 10, pady = 10)

    key = customtkinter.CTkEntry(content, placeholder_text = "Key", font = ("TkDefaultFont", 20), width = 400)
    key.grid(row = 1, column = 0, padx = 10)

    text_out = customtkinter.CTkTextbox(content, wrap = "word")
    text_out.grid(row = 2, column = 0, columnspan = 1, rowspan = 1, sticky = "nsew", padx = 10, pady = 10)

def note_page():
    global content

    content.destroy()
    content = customtkinter.CTkFrame(menu_frame)

    content.grid(row=1, column = 0, columnspan = 2, sticky = "nsew")

    test = customtkinter.CTkLabel(content, text = "Notepad - INOP")
    test.pack()

def switch_page(ins):
    if ins == "Lvl. 1":
        lvl_1_page()
    elif ins == "Lvl. 2":
        lvl_2_page()
    elif ins == "Notepad":
        note_page()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.geometry("1000x600")
root.minsize(width = 300, height = 300)
root.title("Encryptor - By George A.C. Cooke")

menu_frame = customtkinter.CTkFrame(root)

menu_frame.rowconfigure(0, weight = 1, minsize = 20)
menu_frame.rowconfigure(1, weight = 100000, minsize = 80)
menu_frame.columnconfigure(0, weight = 9)
menu_frame.columnconfigure(1, weight = 1)

menu_buttons = customtkinter.CTkSegmentedButton(menu_frame, values = ["Lvl. 1", "Lvl. 2", "Notepad"], command  = switch_page, font = ("TkDefaultFont", 20))
menu_buttons.set("Lvl. 1")
menu_buttons.grid(row = 0, column = 0, sticky = "nsw", padx = 10, pady = 10)

content = customtkinter.CTkFrame(menu_frame)

content.grid(row=1, column = 0, columnspan = 2, rowspan = 1, sticky = "nsew")

lvl_1_page()

menu_frame.pack(anchor = "center", expand = True, fill = "both")

root.mainloop()