import customtkinter
from tkinter import filedialog
import ctypes
from tkinter import *
import Encryption

def INOP(function):
    ctypes.windll.user32.MessageBoxW(0, f"This feature is currently INOP. {function = }", "WARNING:", 0)

def func_new_file(canvas, key_box): # Create new file button in notepad page
    global file_path # I HATE GLOBAL VARIABLES - MESSY --- FIX IF POSSIBLE!!!!!!!!!!!!!!!!!!!!

    file = filedialog.asksaveasfilename(initialdir = "C:\\", title = "Create Encrypted Text File", filetypes = (("Text File", "*.txt"), ))

    try:
        file_path = file + ".txt"
        file_rw = open(file_path, "w")
        file_rw.close()

        canvas.delete(0.0, 'end')
        key_box.delete()
    except:
        file_path = ""



def func_open_file(canvas, key_box, widget_encryption_type): # Open file button in notepad page
    global file_path

    file_path = filedialog.askopenfilename(initialdir = "C:\\", title = "Create Encrypted Text File", filetypes = (("Text File", "*.txt"), ))
    file_rw = open(file_path, "r+")

    encrypted = file_rw.read()

    file_rw.close()

    key_request_root = customtkinter.CTk()

    key_request_root.title("Submit File Encryption Key:")
    key_request_root.minsize(300, 100)
    key_request_root.resizable(width = False, height = False)

    key_request_frame = customtkinter.CTkFrame(key_request_root, fg_color = "transparent")

    key_request_frame.rowconfigure(0, weight = 1)
    key_request_frame.rowconfigure(1, weight = 1)

    key_request_frame.columnconfigure(0, weight = 3)
    key_request_frame.columnconfigure(1, weight = 1)

    key_request_box = customtkinter.CTkEntry(key_request_frame, placeholder_text = "Encryption Key")
    key_request_box.grid(row = 0, column = 0)

    encryption_type_select = customtkinter.CTkOptionMenu(key_request_frame, values = ["Lvl. 1", "Lvl. 2"])
    encryption_type_select.grid(row = 0, column = 1)

    submit_key_button = customtkinter.CTkButton(key_request_frame, text = "Continue", command = lambda: func_continue_open(key_request_box, encryption_type_select, encrypted, canvas, key_box, key_request_root, widget_encryption_type))
    submit_key_button.grid(pady = 10, row = 1, column = 0, columnspan = 2, sticky = "nesw")

    key_request_frame.pack(padx = 10, pady = 10, anchor = "center", expand = True, fill = "both")
    key_request_root.mainloop()

def func_continue_open(key_request_box, encryption_type_select, encrypted_text, canvas, key_box, key_request_root, widget_encryption_type): # Submit button in open file get key page - Triggered on button press
    encryption_key = key_request_box.get()
    encryption_type = encryption_type_select.get()

    decrypted = Encryption.decrypt(encrypted_text, encryption_key, encryption_type)

    canvas.delete(0.0, 'end')
    canvas.insert(0.0, decrypted)

    key_box.delete(0, 'end')
    key_box.insert(0, encryption_key)

    widget_encryption_type.set(encryption_type)

    key_request_root.withdraw()
    key_request_root.quit()

def func_save_file(canvas, key_box, widget_encryption_type): # Save file button in notepad page
    global file_path

    plain_text = canvas.get(0.0, 'end')
    encryption_key = key_box.get()
    encryption_type = widget_encryption_type.get()

    encrypted_text = Encryption.encrypt(plain_text, encryption_key, encryption_type)

    if file_path == "": # If file has ! been created or opened --> will need to save new file location and make it
        file_path = filedialog.asksaveasfilename(initialdir = "C:\\", title = "Save As Encrypted Text File", filetypes = (("Text File", "*.txt"), ))

    if file_path != "":
        file_rw = open(file_path, "w")
        file_rw.write(encrypted_text)
        file_rw.close()

def func_lvl_one_encryptor_input_change(event): # Triggered when the text is changed in any of the input boxes - generates new encrypted text
    plain_text = widget_text_in.get(0.0, 'end')
    encryption_key = widget_key_box.get()

    encrypted_text = Encryption.encrypt(plain_text, encryption_key, "Lvl. 1")

    widget_text_out.delete(0.0, 'end')
    widget_text_out.insert(0.0, encrypted_text)

def func_lvl_two_encryptor_input_change(event): # Triggered when the text is changed in any of the input boxes - generates new encrypted text
    plain_text = widget_text_in.get(0.0, 'end')
    encryption_key = widget_key_box.get()

    encrypted_text = Encryption.encrypt(plain_text, encryption_key, "Lvl. 2")

    widget_text_out.delete(0.0, 'end')
    widget_text_out.insert(0.0, encrypted_text)

def lvl_1_page(content):
    global widget_text_in, widget_key_box, widget_text_out

    content.destroy()

    menu_frame.rowconfigure(0, weight = 1, minsize = 20)
    menu_frame.rowconfigure(1, weight = 100000, minsize = 20)
    menu_frame.columnconfigure(0, weight = 9)
    menu_frame.columnconfigure(1, weight = 1)

    content = customtkinter.CTkFrame(menu_frame, fg_color = "transparent")

    content.grid(row=1, column = 0, columnspan = 2, rowspan = 1, sticky = "nsew")

    content.rowconfigure(0, weight = 1, minsize = 40)
    content.rowconfigure(1, weight = 1, minsize = 15)
    content.rowconfigure(2, weight = 100000, minsize = 40)
    content.rowconfigure(3, weight = 2, minsize = 20)
    content.rowconfigure(4, weight = 1, minsize = 15)
    content.rowconfigure(5, weight = 100000, minsize = 40)
    content.rowconfigure(6, weight = 1)

    content.columnconfigure(0, weight = 1)

    key_frame = customtkinter.CTkFrame(content, fg_color = "transparent")
    key_frame.columnconfigure(0)
    key_frame.columnconfigure(1)

    level_label = customtkinter.CTkLabel(content, text = "Level 1 Encryption:", font = ("TkDefaultFont", 30, 'bold'))
    level_label.grid(row = 0, column = 0, columnspan = 1, sticky = "nsw", padx = 10, pady = 10)

    text_in_label = customtkinter.CTkLabel(content, text = "Plain Text In:", font = ("TkDefaultFont", 15))
    text_in_label.grid(row = 1, column = 0, columnspan = 1, sticky = "nsw", padx = 10)

    widget_text_in = customtkinter.CTkTextbox(content, wrap = "word")
    widget_text_in.bind('<KeyRelease>', func_lvl_one_encryptor_input_change)
    widget_text_in.grid(row = 2, column = 0, columnspan = 1, sticky = "nsew", padx = 10)


    key_label = customtkinter.CTkLabel(key_frame, text = "Key:", font = ("TkDefaultFont", 15))
    key_label.grid(row = 0, column = 0, columnspan = 1, sticky = "nse", padx = 5)

    key = StringVar()
    key.trace("w", lambda name, index, mode, key=key: func_lvl_one_encryptor_input_change("nah"))

    widget_key_box = customtkinter.CTkEntry(key_frame, placeholder_text = "Key", font = ("TkDefaultFont", 20), width = 400, textvariable = key)
    widget_key_box.grid(row = 0, column = 1, padx = 5, sticky = "nsw")

    key_frame.grid(row = 3, column = 0, pady = 10)


    text_out_label = customtkinter.CTkLabel(content, text = "Encrypted Text Out:", font = ("TkDefaultFont", 15))
    text_out_label.grid(row = 4, column = 0, columnspan = 1, sticky = "nsw", padx = 10)

    widget_text_out = customtkinter.CTkTextbox(content, wrap = "word")
    widget_text_out.grid(row = 5, column = 0, columnspan = 1, rowspan = 1, sticky = "nsew", padx = 10)

    spacing_label = customtkinter.CTkLabel(content, text = "", font = ("TkDefaultFont", 1))
    spacing_label.grid(row = 6, column = 0, columnspan = 1, sticky = "nsw", padx = 10)

def lvl_2_page(content):
    global widget_text_in, widget_key_box, widget_text_out

    content.destroy()

    menu_frame.rowconfigure(0, weight = 1, minsize = 20)
    menu_frame.rowconfigure(1, weight = 100000, minsize = 20)
    menu_frame.columnconfigure(0, weight = 9)
    menu_frame.columnconfigure(1, weight = 1)

    content = customtkinter.CTkFrame(menu_frame, fg_color = "transparent")

    content.grid(row=1, column = 0, columnspan = 2, rowspan = 1, sticky = "nsew")

    content.rowconfigure(0, weight = 1, minsize = 40)
    content.rowconfigure(1, weight = 1, minsize = 15)
    content.rowconfigure(2, weight = 100000, minsize = 40)
    content.rowconfigure(3, weight = 2, minsize = 20)
    content.rowconfigure(4, weight = 1, minsize = 15)
    content.rowconfigure(5, weight = 100000, minsize = 40)
    content.rowconfigure(6, weight = 1)

    content.columnconfigure(0, weight = 1)

    key_frame = customtkinter.CTkFrame(content, fg_color = "transparent")
    key_frame.columnconfigure(0)
    key_frame.columnconfigure(1)

    level_label = customtkinter.CTkLabel(content, text = "Level 2 Encryption:", font = ("TkDefaultFont", 30, 'bold'))
    level_label.grid(row = 0, column = 0, columnspan = 1, sticky = "nsw", padx = 10, pady = 10)

    text_in_label = customtkinter.CTkLabel(content, text = "Plain Text In:", font = ("TkDefaultFont", 15))
    text_in_label.grid(row = 1, column = 0, columnspan = 1, sticky = "nsw", padx = 10)

    widget_text_in = customtkinter.CTkTextbox(content, wrap = "word")
    widget_text_in.bind('<KeyRelease>', func_lvl_two_encryptor_input_change)
    widget_text_in.grid(row = 2, column = 0, columnspan = 1, sticky = "nsew", padx = 10)


    key_label = customtkinter.CTkLabel(key_frame, text = "Key:", font = ("TkDefaultFont", 15))
    key_label.grid(row = 0, column = 0, columnspan = 1, sticky = "nse", padx = 5)

    key = StringVar()
    key.trace("w", lambda name, index, mode, key=key: func_lvl_two_encryptor_input_change("nah"))

    widget_key_box = customtkinter.CTkEntry(key_frame, placeholder_text = "Key", font = ("TkDefaultFont", 20), width = 400, textvariable = key)
    widget_key_box.grid(row = 0, column = 1, padx = 5, sticky = "nsw")

    key_frame.grid(row = 3, column = 0, pady = 10)


    text_out_label = customtkinter.CTkLabel(content, text = "Encrypted Text Out:", font = ("TkDefaultFont", 15))
    text_out_label.grid(row = 4, column = 0, columnspan = 1, sticky = "nsw", padx = 10)

    widget_text_out = customtkinter.CTkTextbox(content, wrap = "word")
    widget_text_out.grid(row = 5, column = 0, columnspan = 1, rowspan = 1, sticky = "nsew", padx = 10)

    spacing_label = customtkinter.CTkLabel(content, text = "", font = ("TkDefaultFont", 1))
    spacing_label.grid(row = 6, column = 0, columnspan = 1, sticky = "nsw", padx = 10)

def note_page(content):
    file_path = ""

    content.destroy()
    content = customtkinter.CTkFrame(menu_frame, fg_color = "transparent")
    content.grid(row=1, column = 0, columnspan = 2, rowspan = 1, sticky = "nsew")

    content.rowconfigure(0, weight = 1, minsize = 20)
    content.rowconfigure(1, weight = 10000)

    content.columnconfigure(0, weight = 1, minsize = 120)
    content.columnconfigure(1, weight = 1, minsize = 120)
    content.columnconfigure(2, weight = 1, minsize = 120)
    content.columnconfigure(3, weight = 1000000, minsize = 75)
    content.columnconfigure(4, weight = 1, minsize = 300)
    content.columnconfigure(5, weight = 1, minsize = 120)

    canvas = customtkinter.CTkTextbox(content, wrap = "word")
    canvas.grid(row = 1, column = 0, columnspan = 6, rowspan = 1, sticky = "nsew", padx = 10, pady = 10)

    key_box = customtkinter.CTkEntry(content, placeholder_text = "Key", font = ("TkDefaultFont", 20), width = 400)
    key_box.grid(row = 0, column = 4, sticky = "nsew")

    widget_encryption_type = customtkinter.CTkOptionMenu(content, values = ["Lvl. 1", "Lvl. 2"], font = ("TkDefaultFont", 20))
    widget_encryption_type.grid(row = 0, column = 5, sticky = "nsew", padx = 10)

    new_file = customtkinter.CTkButton(content, text = "New File", font = ("TkDefaultFont", 20), command = lambda: func_new_file(canvas, key_box))
    new_file.grid(row = 0, column = 0, sticky = "nsew", padx = 10)

    open_file = customtkinter.CTkButton(content, text = "Open File", font = ("TkDefaultFont", 20), command = lambda: func_open_file(canvas, key_box, widget_encryption_type))
    open_file.grid(row = 0, column = 1, sticky = "nsew")

    save_file = customtkinter.CTkButton(content, text = "Save File", font = ("TkDefaultFont", 20), command = lambda: func_save_file(canvas, key_box, widget_encryption_type))
    save_file.grid(row = 0, column = 2, sticky = "nsew", padx = 10)

    middle_filler = customtkinter.CTkLabel(content, text = "Key:", font = ("TkDefaultFont", 20))
    middle_filler.grid(row = 0, column = 3, sticky = "nse", padx = 10)


def switch_page(ins):
    if ins == "Lvl. 1":
        lvl_1_page(content)
    elif ins == "Lvl. 2":
        lvl_2_page(content)
    elif ins == "Notepad":
        note_page(content)

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.geometry("1000x600")
root.minsize(width = 900, height = 350)
root.title("Encryptor - By George A.C. Cooke")

menu_frame = customtkinter.CTkFrame(root)

menu_frame.rowconfigure(0, weight = 1, minsize = 20)
menu_frame.rowconfigure(1, weight = 100000, minsize = 80)
menu_frame.columnconfigure(0, weight = 9)
menu_frame.columnconfigure(1, weight = 1)

content = customtkinter.CTkFrame(menu_frame)

content.grid(row=1, column = 0, columnspan = 2, rowspan = 1, sticky = "nsew")

menu_buttons = customtkinter.CTkSegmentedButton(menu_frame, values = ["Lvl. 1", "Lvl. 2", "Notepad"], command  = switch_page, font = ("TkDefaultFont", 20))
menu_buttons.set("Lvl. 1")
menu_buttons.grid(row = 0, column = 0, sticky = "nsw", padx = 10, pady = 10)


lvl_1_page(content)

menu_frame.pack(anchor = "center", expand = True, fill = "both")

file_path = ""

root.mainloop()