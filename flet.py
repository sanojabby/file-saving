from tkinter import filedialog, Text, INSERT, END

def save_file():
    open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if open_file is None:
        return
    text_content = text_widget.get(1.0, END)
    open_file.write(text_content)
    open_file.close()

def open_file():
    file = filedialog.askopenfile(mode='r', filetype=[('Text files', '*.txt')])
    if file is not None:
        content = file.read()
        text_widget.insert(INSERT, content)

# Assuming you have created a Tkinter window and a Text widget named text_widget
# Here's a simplified example of how you might do it:

import tkinter as tk

root = tk.Tk()
root.geometry("600x600")
root.title("Sano_Notepad")
root.config(bg="lightblue")
root.resizable(False,False)
text_widget = tk.Text(root)
text_widget.pack()


# Create buttons to trigger save_file and open_file functions
save_button = tk.Button(root, text="Save File", command=save_file)
save_button.pack()

open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack()
#save_button=tk.Button(root,width='20',height='2',bg='#fff',text='save file',command=save_file).place(X=100,Y=5)
#save_button.pack()
#open_button=tk.Button(root,width='20',height='2',bg='#fff',text='open file',command=open_file).place(x=300,y=5)
#open_button.pack()


root.mainloop()