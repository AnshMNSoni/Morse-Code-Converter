from tkinter import *
import pyperclip, random
from tkinter import messagebox


FONT = ('New Times Roman', 16, 'bold')


morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '--..---','!': '-.-.--',';': '-.-.-.',':': '---...','+': '.-.-.','=': '-...-'
}


try_some = ['.... . .-.. .-.. ---',
 '.-- --- .-. .-.. -..',
 '.--. -.-- - .... --- -.',
 '-- --- .-. ... .',
 '-.-. --- -.. .',
 '.--. .-. --- --. .-. .- --',
 '-.-. --- -- .--. ..- - . .-.',
 '... -.-. .. . -. -.-. .',
 '.-. .- -. -.. --- --',
 '.-- --- .-. -.. ...',
 '- . ... -',
 '..-. .-.. .- ... -.-',
 '.-.. .. -... .-. .- .-. -.--',
 '-.. . ...- . .-.. --- .--. . .-.',
 '- .- - .-',
 '.- .-.. --. --- .-. .. - .... --',
 '-. . - .-- --- .-. -.-',
 '-.. .- - .- -... .- ... .',
 '... -.-. .-. .. .--. -',
 '..-. ..- -. -.-. - .. --- -.',
 '...- .- .-. .. .- -... .-.. .',
 '.-.. --- --- .--.',
 '-.-. --- -. -.. .. - .. --- -.',
 '--- -... .--- . -.-. -',
 '-.-. .-.. .- ... ...']


class Morse_GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('Morse Converter')
        self.window.config(bg='white', highlightthickness=0, padx=40, pady=40)
        
        
        # Morse Logo:
        self.morse_img = PhotoImage(file='morse.png')
        self.img = Canvas(width=240, height=240, highlightthickness=0, bg='white')
        self.img.create_image(120, 120, image=self.morse_img)
        self.img.grid(row=0, column=1)
        
        
        # Text Label:
        self.text = Label(text='Text', font=FONT, bg='white', bd=8)
        self.text.grid(row=1, column=0, pady=10)
        
        
        # Text Input:
        self.input_text = StringVar()
        self.text_input = Entry(textvariable=self.input_text, font=FONT, width=25)
        self.text_input.focus()
        self.text_input.grid(row=1, column=1, padx=20)
        
        
        # Encode Button:
        self.encode_btn = Button(text='Encode', bg='#62DC57', command=self.encode, font=FONT, width=9, bd=8)
        self.encode_btn.grid(row=2, column=0)
        
        
        # Encode Label:
        self.encode_label = Label(text=None, font=FONT, bg='white', highlightthickness=0)
        self.encode_label.grid(row=2, column=1, padx=10)
        
        
        # Copy Button:
        self.copy_btn = Button(text='Copy', command=self.copy_txt, bg='#DB8D58', font=FONT, width=9, bd=8)
        self.copy_btn.grid(row=2, column=2)
        
        
        # Decode Button:
        self.encode_btn = Button(text='Decode', bg='#62DC57', command=self.decode, font=FONT, width=9, bd=8)
        self.encode_btn.grid(row=3, column=0, pady=10)
        
        
        # Decode Label:
        self.decode_label = Label(text=None, bg='white', highlightthickness=0, font=FONT)
        self.decode_label.grid(row=3, column=1, padx=10)
        
        
        # Try Some Morse Code:
        self.try_btn = Button(text="Try Morse's", bg='#54535C', fg='white', command=self.try_me, font=FONT, bd=8)
        self.try_btn.grid(row=3, column=2)
        
        
        self.window.mainloop()
    
    
    def encode(self):
        try:
            self.message = self.text_input.get()
            self.encode_string =  ' '.join(morse_code_dict[char] for char in self.message.upper())
            
        except KeyError:
            messagebox.showwarning(message='Already Encoded!')
            self.text_input.delete(0, END)
        
        else:
            self.encode_label.config(text=self.encode_string)
            self.text_input.delete(0, END)
            
            
    def decode(self):
        try:
            self.message = self.text_input.get()
            self.inverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}
            self.decode_string = ''.join(self.inverse_morse_code_dict[char] for char in self.message.split()).capitalize()
            
        except KeyError:
            messagebox.showwarning(message='Already Decoded!')
            self.text_input.delete(0, END)
        
        else:
            self.decode_label.config(text=self.decode_string)
            self.text_input.delete(0, END)
        
        
    def copy_txt(self):
        try:
            pyperclip.copy(self.encode_string)
        
        except AttributeError:
            messagebox.showinfo(title='Info', message='Sorry! Nothing to Copy')
            
    
    def try_me(self):
        self.text_input.delete(0, END)
        self.text_input.insert(0, random.choice(try_some))
        
        
Morse_GUI()