⚠️ NOTE: This project was done as a thought experiment without the intention of being highly secure or trust worthy. DO NOT use it for sensitive or important information. It does have bugs and it can be easily decrypted by malicious parties. I absolve myself as its creator of any responsibility regarding the security of any data inputted into it. ⚠️

# The Brief:
For my summer work preceding my enrolment to 6th form, I was tasked with researching an element of computer science that I would not typically have great interest in. Whilst I have loved programming since I was first introduced to it, I have never considered anything relating to security or encryption. For this reason, I thought it would be an interesting experiment to try and program my own encryption software. In doing so, I learnt about: the use of f strings, the basics of encryption, and furthered my understanding of the custom tkinter library.

## Installing & Running:
To run this program you must have the following installed:

- Python 3.13 or later,
- Custom tkinter,

Python can be installed from the official python website downloads page (https://www.python.org/downloads/) or on the Microsoft store. Custom tkinter must be installed using the pip command in command prompt. This can be done with the following command:

```
pip install customtkinter
```

Should that fail, the following alternatives can be used:

```
python3 -m pip install customtkinter
```

```
pip3 install customtkinter
```

Having installed the prerequisites, the file "Encryption Tool" can be double clicked and run. To view the code, open it in your IDE of choice.

## Usage:
Pages can be navigated through the menu at the top of the window. Pages are as follows: Lvl. 1, Lvl. 2, Notepad. The levels one and two pages act as playgrounds for experimentation with the encryption engine; plain text should be inputted in the topmost box of the page with the encryption key in the middle. Encrypted text will then be outputted in the bottom most box. Keys should start with either the capital letter "L" or the capital letter "R" and then be followed by a string of integers. To decrypt encrypted text, copy the encrypted text in to the encrypted text out box in the relevant encryption level page and insert the key into the key box.

The notepad page can be used to save data between uses and acts similarly to any word processor you may be used to. The only difference is that any files that are saved will be encrypted using the level and key specified in the top left corner of the page. Note, if the key is left blank, the saved file will be in human-legible plain text. To decrypt encrypted files, open the text file in the app and input the encryption key you used to originally save the file. If you forget the key, the file will be locked/encrypted permanently and any data within it will be lost/illegible. To change the encryption key of a file, import it to the notepad page normally and then, once it has been decrypted having inputted the original key, change the key in the top left corner and update the text body - this can be by deleting one character and then replacing it with the same. You can then save the file and key will be changed. If you do not change the body of the text, the file will not be changed.

## Encryption Methods:

#### Level 1:
Level 1 encryption is a simple directional Caesar cypher with the letter at the beginning of the key indicating the direction of shift. This will offset all characters by the same amount in the direction of shift. Note: if the numeric section of the key exceeds 78, the alphabet will start again. As such, any key above L78 or R78 is no longer going to be different from a key below it. Equally, a right shift of 4 (a key of "R4") will be the same as a left shift of 74 (a key of "L74").

#### Level 2:
Level 2 encryption is more secure in that each letter in the text will be shifted by a different amount for as long as the numeric section of the key is. Similarly to level 1, the first character if the key ("L" or "R") indicates the direction of shift. Conversely, the numbers each indicate the number of shifts for each character in the plain text. For example, with a key of "L1234", all shifts will be in the left direction but the first letter will be shifted by one while the second is by two, the third by three and the fourth by four. Equally, with a key of "L4321", the first character will be shifted left by four, the second by three, the third by two and the fourth by one. If the plain text is longer than the numeric section of the key, the cycle will repeat itself. For example with the key of "L1234", we already know what will happen to the first four characters of the plain text. The fifth character will be offset to the left by an index of one, the sixth by two, the seventh by three and the eighth by four.

## Screenshot Gallery:

<img width="602" height="380" alt="image" src="https://github.com/user-attachments/assets/cc091b99-26a0-454a-8182-8968a4010a40" />

<img width="602" height="380" alt="image" src="https://github.com/user-attachments/assets/a4546f70-83fb-44ed-8c1f-c07d22770489" />

