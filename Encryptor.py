from tkinter import *
import customtkinter
import ctypes

def encryptor_input_change(event):
    global page, text_in, text_out, canvas, encryption_type, notepad_encrypted

    if page == "Lvl. 1":
        plain_text = text_in.get(0.0, 'end')
        encrypt(plain_text, 0)

    elif page == "Lvl. 2":
        plain_text = text_in.get(0.0, 'end')
        string = ""
        index = 0

        for i in plain_text:
            next_encrypted_letter = encrypt(i, index)
            string = string + str(next_encrypted_letter)
            index = index + 1

        text_out.delete(0.0, 'end')
        text_out.insert(0.0, string)

    elif page == "Notepad":
        plain_text = canvas.get(0.0, 'end')
        encryption_method = encryption_type.get()

        if encryption_method == "Lvl. 1":
            encrypted = encrypt(plain_text, "null")
        elif encryption_method == "Lvl. 2":
            encrypted = ""
            index = 0

            for i in plain_text:
                next_encrypted_letter = encrypt(i, index)
                encrypted = encrypted + str(next_encrypted_letter)
                index = index + 1

        print(f"{plain_text = }")
        print(f"{encrypted = }")
        notepad_encrypted = encrypted

def encrypt(text, index):
    global key_box, alphabet, page, key

    if page == "Lvl. 1":
        new_alphabet = key_change(key_box)

        encrypted = ""

        for i in text:
            try:
                position_original_alphabet = alphabet.index(i)
                new_char = new_alphabet[position_original_alphabet]
                encrypted = encrypted + new_char
            except:
                encrypted = encrypted + i

        text_out.delete(0.0, 'end')
        text_out.insert(0.0, encrypted)

    elif page == "Lvl. 2":
        key_string = key_box.get()
        try:
            direction = key_string[0]
            key_int = int(key_string[1:])
            
            length_key = len(str(key_int))
            key_index = index % length_key
            ammount = int(str(key_int)[key_index])
            
            new_alphabet = []
            new_alphabet.extend(alphabet)

            if direction == "L":
                new_alphabet.extend(new_alphabet[0:ammount])
                del(new_alphabet[0:ammount])
            elif direction == "R":
                temp = new_alphabet[-ammount:]
                temp.extend(new_alphabet)
                new_alphabet = temp
                del(new_alphabet[-ammount:])

            try:
                position_original_alphabet = alphabet.index(text)
                next_letter = new_alphabet[position_original_alphabet]
            except:
                next_letter = text

            return next_letter

        except:
            pass

    elif page == "Notepad":
        if index == "null": # Lvl. 1 encryption
            new_alphabet = key_change(key)

            encrypted = ""

            for i in text:
                try:
                    position_original_alphabet = alphabet.index(i)
                    new_char = new_alphabet[position_original_alphabet]
                    encrypted = encrypted + new_char
                except:
                    encrypted = encrypted + i

            return encrypted

        else: # Lvl. 2 encryption
            key_string = key.get()

            try:

                direction = key_string[0]
                key_int = int(key_string[1:])

                length_key = len(str(key_int))
                key_index = index % length_key
                ammount = int(str(key_int)[key_index])

                new_alphabet = []
                new_alphabet.extend(alphabet)

                if direction == "L":
                    new_alphabet.extend(new_alphabet[0:ammount])
                    del(new_alphabet[0:ammount])
                elif direction == "R":
                    temp = new_alphabet[-ammount:]
                    temp.extend(new_alphabet)
                    new_alphabet = temp
                    del(new_alphabet[-ammount:])

                try:
                    position_original_alphabet = alphabet.index(text)
                    next_letter = new_alphabet[position_original_alphabet]
                except:
                    next_letter = text

                return next_letter

            except:
                pass

def encrypt_alphabet(direction, ammount):
    global alphabet

    ammount = ammount % 78
    new_alphabet = []
    new_alphabet.extend(alphabet)

    if direction == "L":
        new_alphabet.extend(new_alphabet[0:ammount])
        del(new_alphabet[0:ammount])
    elif direction == "R":
        temp = new_alphabet[-ammount:]
        temp.extend(new_alphabet)
        new_alphabet = temp
        del(new_alphabet[-ammount:])

    return new_alphabet

def key_change(key_box):
    global page, alphabet

    key_string = key_box.get()

    if page == "Lvl. 1":
        try:
            if key_string[0] not in ["L", "R"]:
                ctypes.windll.user32.MessageBoxW(0, "Key Must Begin With L or R", "WARNING:", 0)
            
            return encrypt_alphabet(key_string[0], int(key_string[1:]))

        except:
            pass

    elif page == "Notepad":
        try:
            if key_string[0] not in ["L", "R"]:
                ctypes.windll.user32.MessageBoxW(0, "Key Must Begin With L or R", "WARNING:", 0)
            
            return encrypt_alphabet(key_string[0], int(key_string[1:]))

        except:
            pass

def lvl_1_page():
    global content, page, text_in, key_box, text_out

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
    text_in.bind('<KeyRelease>', encryptor_input_change)
    text_in.grid(row = 0, column = 0, columnspan = 1, sticky = "nsew", padx = 10, pady = 10)

    key_box = StringVar()
    key_box.trace("w", lambda name, index, mode, key_box=key_box: encryptor_input_change(text_in.get(0.0, 'end')))

    key = customtkinter.CTkEntry(content, placeholder_text = "Key", font = ("TkDefaultFont", 20), width = 400, textvariable = key_box)
    key.grid(row = 1, column = 0, padx = 10)

    text_out = customtkinter.CTkTextbox(content, wrap = "word")
    text_out.grid(row = 2, column = 0, columnspan = 1, rowspan = 1, sticky = "nsew", padx = 10, pady = 10)

def lvl_2_page():
    global content, page, text_in, key_box, text_out

    page = "Lvl. 2"

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
    text_in.bind('<KeyRelease>', encryptor_input_change)
    text_in.grid(row = 0, column = 0, columnspan = 1, sticky = "nsew", padx = 10, pady = 10)

    key_box = StringVar()
    key_box.trace("w", lambda name, index, mode, key_box=key_box: encryptor_input_change(text_in.get(0.0, 'end')))

    key = customtkinter.CTkEntry(content, placeholder_text = "Key", font = ("TkDefaultFont", 20), width = 400, textvariable = key_box)
    key.grid(row = 1, column = 0, padx = 10)

    text_out = customtkinter.CTkTextbox(content, wrap = "word")
    text_out.grid(row = 2, column = 0, columnspan = 1, rowspan = 1, sticky = "nsew", padx = 10, pady = 10)

def note_page():
    global content, page, canvas, encryption_type, key

    page = "Notepad"

    content.destroy()
    content = customtkinter.CTkFrame(menu_frame, fg_color = "transparent")
    content.grid(row=1, column = 0, columnspan = 2, rowspan = 1, sticky = "nsew")

    content.rowconfigure(0, weight = 1, minsize = 20)
    content.rowconfigure(1, weight = 10000)

    content.columnconfigure(0, weight = 1, minsize = 120)
    content.columnconfigure(1, weight = 1, minsize = 120)
    content.columnconfigure(2, weight = 1, minsize = 120)
    content.columnconfigure(3, weight = 1000000)
    content.columnconfigure(4, weight = 1, minsize = 300)
    content.columnconfigure(5, weight = 1, minsize = 120)

    new_file = customtkinter.CTkButton(content, text = "New File", font = ("TkDefaultFont", 20), command = ...)
    new_file.grid(row = 0, column = 0, sticky = "nsew", padx = 10)

    open_file = customtkinter.CTkButton(content, text = "Open File", font = ("TkDefaultFont", 20), command = ...)
    open_file.grid(row = 0, column = 1, sticky = "nsew", padx = 10)

    save_file = customtkinter.CTkButton(content, text = "Save File", font = ("TkDefaultFont", 20), command = ...)
    save_file.grid(row = 0, column = 2, sticky = "nsew", padx = 10)

    middle_filler = customtkinter.CTkLabel(content, text = "Key:", font = ("TkDefaultFont", 20))
    middle_filler.grid(row = 0, column = 3, sticky = "nse")

    key_box = StringVar()
    key_box.trace("w", lambda name, index, mode, key_box=key_box: encryptor_input_change(canvas.get(0.0, 'end')))

    key = customtkinter.CTkEntry(content, placeholder_text = "Key", font = ("TkDefaultFont", 20), width = 400, textvariable = key_box)
    key.grid(row = 0, column = 4, sticky = "nsew", padx = 10)

    encryption_type = customtkinter.CTkOptionMenu(content, values = ["Lvl. 1", "Lvl. 2"], font = ("TkDefaultFont", 20))
    encryption_type.grid(row = 0, column = 5, sticky = "nsew", padx = 10)

    canvas = customtkinter.CTkTextbox(content, wrap = "word")
    canvas.bind('<KeyRelease>', encryptor_input_change)
    canvas.grid(row = 1, column = 0, columnspan = 6, rowspan = 1, sticky = "nsew", padx = 10, pady = 10)

def switch_page(ins):
    if ins == "Lvl. 1":
        lvl_1_page()
    elif ins == "Lvl. 2":
        lvl_2_page()
    elif ins == "Notepad":
        note_page()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "'", '"', ";", ":", "(", ")", "!", "$", "%", "&", "-", "_", "?", " "]


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