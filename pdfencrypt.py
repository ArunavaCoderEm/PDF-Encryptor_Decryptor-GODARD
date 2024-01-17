import PyPDF2
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

splash = Tk()
splash.title ('GodardEncrypt')
splash.geometry ('400x400')
splash.resizable (0,0)
splash.configure (background = 'red')
spl_lab = Label (splash, text = 'GodARD Devos \n PDF Encrypt/Decrypt', bg = 'yellow', fg = 'blue', font = ('vendana', 20, 'bold'))
spl_lab.pack (pady = 150)

def mainscreen():
    splash.destroy()
    
    def select_file():
        file_path = ''
        filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        file_entry.delete(0, END)
        file_entry.insert(0, file_path)
    
    def encrypt_pdf():
        file_path = file_entry.get()
        password = password_entry.get()
    
        if file_path and password:
            pdf = PyPDF2.PdfFileReader(file_path, "rb")
            output_pdf = PyPDF2.PdfFileWriter()
    
            for page_num in range(pdf.getNumPages()):
                page = pdf.getPage(page_num)
                output_pdf.addPage(page)
    
            output_pdf.encrypt(password)
    
            output_file_path = ''
            filedialog.asksaveasfilename(defaultextension=".pdf")
            with open(output_file_path, "wb") as output_file:
                output_pdf.write(output_file)
            
            file_entry.delete(0, END)
            password_entry.delete(0, END)
    
            messagebox.showinfo("Encryption Complete", 
            "PDF file encrypted successfully!")
        else:
            messagebox.showerror("Error", 
            "Please select a file and enter a password.")
    
    def decrypt_pdf():
        file_path = file_entry.get()
        password = password_entry.get()
    
        if file_path and password:
            pdf = PyPDF2.PdfFileReader(file_path, "rb")
    
            if pdf.isEncrypted:
                pdf.decrypt(password)
                output_pdf = PyPDF2.PdfFileWriter()
    
                for page_num in range(pdf.getNumPages()):
                    page = pdf.getPage(page_num)
                    output_pdf.addPage(page)
    
                output_file_path = ''
                filedialog.asksaveasfilename(defaultextension=".pdf")
                with open(output_file_path, "wb") as output_file:
                    output_pdf.write(output_file)
                
                file_entry.delete(0, END)
                password_entry.delete(0, END)
    
                messagebox.showinfo("Decryption Complete", 
                "PDF file decrypted successfully!")
            else:
                messagebox.showerror("Error", 
                "The selected PDF file is not encrypted.")
        else:
            messagebox.showerror("Error", 
            "Please select a file and enter a password.")
    
    
    root = Tk()
    root.title("PDF Encryption and Decryption GODARD")
    root.geometry("400x250")
    
    file_label = Label(root, text="Select PDF file:")
    file_label.pack()
    
    file_entry = Entry(root, width=50)
    file_entry.pack()
    
    browse_button = Button(root, text="Browse", command=select_file)
    browse_button.pack()
    
    password_label = Label(root, text="Enter password:")
    password_label.pack()
    
    password_entry = Entry(root, width=50, show="*")
    password_entry.pack()
    
    encrypt_button = Button(root, text="Encrypt", command=encrypt_pdf)
    encrypt_button.pack()
    
    decrypt_button = Button(root, text="Decrypt", command=decrypt_pdf)
    decrypt_button.pack()

splash.after ( 2500, mainscreen)

mainloop()
