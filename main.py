import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from algorithms import (caesar_decrypt, rail_fence_decrypt, row_matrix_decrypt,
                        substitution_decrypt, vigenere_decrypt, 
                        caesar_encrypt, rail_fence_encrypt, row_matrix_encrypt,
                        substitution_encrypt, vigenere_encrypt)

class DecryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Decryptor Pro")
        self.root.geometry("600x500")  # Fixed window size
        self.root.configure(bg="#2E2E2E")  # Dark gray background
        self.root.resizable(False, False)  # Prevent resizing

        # Title label
        self.title_label = tk.Label(
            self.root,
            text="Decryptor Program",
            font=("Helvetica", 28),
            fg="white",
            bg="#2E2E2E"
        )
        self.title_label.pack(pady=20)

        # Frame for input section
        self.input_frame = tk.Frame(self.root, bg="#2E2E2E")
        self.input_frame.pack(pady=(0, 20))

        # Text input label
        self.input_label = tk.Label(
            self.input_frame,
            text="Upload Text File or Enter Text:",
            font=("Helvetica", 14),
            fg="white",
            bg="#2E2E2E"
        )
        self.input_label.pack(pady=(0, 10))

        # Text input
        self.text_input = tk.Text(self.input_frame, height=6, width=70, bg="#3E3E3E", fg="white", font=("Helvetica", 12), wrap=tk.WORD)
        self.text_input.pack(pady=(0, 10))

        # File upload button
        self.file_button = tk.Button(
            self.input_frame,
            text="Choose a File",
            command=self.show_filechooser,
            bg="skyblue",
            font=("Helvetica", 12),
            width=20
        )
        self.file_button.pack(pady=(0, 10))

        # Algorithm selection
        self.algorithm_var = tk.StringVar(value="Select Algorithm")
        self.algorithm_menu = tk.OptionMenu(self.input_frame, self.algorithm_var, 
                                             'Caesar Cipher', 
                                             'Rail Fence Cipher', 
                                             'Row Matrix', 
                                             'Substitution Cipher', 
                                             'Vigenère Cipher')
        self.algorithm_menu.config(bg="#3E3E3E", fg="white", font=("Helvetica", 12))
        self.algorithm_menu.pack(pady=(0, 10))

        # Buttons frame for action buttons
        self.button_frame = tk.Frame(self.root, bg="#2E2E2E")
        self.button_frame.pack(pady=(10, 20))

        # Decrypt button
        self.decrypt_button = tk.Button(
            self.button_frame,
            text="Decrypt",
            command=self.decrypt_text,
            bg="skyblue",
            font=("Helvetica", 14),
            width=15
        )
        self.decrypt_button.pack(side=tk.LEFT, padx=10)

        # Save output button
        self.save_button = tk.Button(
            self.button_frame,
            text="Save Output",
            command=self.save_output,
            bg="skyblue",
            font=("Helvetica", 14),
            width=15
        )
        self.save_button.pack(side=tk.LEFT, padx=10)

        # Test encryption button
        self.test_button = tk.Button(
            self.root,
            text="Test Encryption",
            command=self.open_encryption_window,
            bg="skyblue",
            font=("Helvetica", 14),
            width=20
        )
        self.test_button.pack(pady=(10, 20))

        # Result label
        self.result_label = tk.Label(
            self.root,
            text="Decrypted Text Will Appear Here",
            font=("Helvetica", 14),
            fg="white",
            bg="#2E2E2E",
            wraplength=550
        )
        self.result_label.pack(pady=(10, 20))

    def show_filechooser(self):
        """Open a file chooser dialog to select a text file."""
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_input.delete(1.0, tk.END)  # Clear existing text
                self.text_input.insert(tk.END, file.read())  # Insert file content

    def decrypt_text(self):
        """Decrypt the input text based on the selected algorithm."""
        selected_algorithm = self.algorithm_var.get()
        input_text = self.text_input.get(1.0, tk.END).strip()

        # Perform decryption based on selected algorithm
        if selected_algorithm == 'Caesar Cipher':
            decrypted = caesar_decrypt(input_text, shift=3)  # Example shift value
        elif selected_algorithm == 'Rail Fence Cipher':
            decrypted = rail_fence_decrypt(input_text, key=3)  # Example key
        elif selected_algorithm == 'Row Matrix':
            decrypted = row_matrix_decrypt(input_text, key=[1, 2, 3])  # Example key
        elif selected_algorithm == 'Substitution Cipher':
            decrypted = substitution_decrypt(input_text, mapping={'a': 'z', 'b': 'y', 'c': 'x'})  # Example mapping
        elif selected_algorithm == 'Vigenère Cipher':
            decrypted = vigenere_decrypt(input_text, key='KEYWORD')  # Example key
        else:
            decrypted = "Invalid Algorithm or Input"

        # Display the decrypted text
        self.result_label.config(text=f"Decrypted Text: {decrypted}")
        self.decrypted_text = decrypted

    def save_output(self):
        """Prompt user to select a location to save the decrypted output."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.decrypted_text)
            messagebox.showinfo("Success", "Output saved successfully!")

    def open_encryption_window(self):
        """Open a new window for text encryption."""
        self.encryption_window = Toplevel(self.root)
        self.encryption_window.title("Encryption Window")
        self.encryption_window.geometry("500x400")  # Fixed window size
        self.encryption_window.configure(bg="#2E2E2E")

        # Back button
        back_button = tk.Button(
            self.encryption_window,
            text="Back",
            command=self.encryption_window.destroy,
            bg="skyblue",
            font=("Helvetica", 12)
        )
        back_button.pack(pady=(10, 10), anchor='nw')  # Place back button in the top-left corner

        # Text input for encryption
        self.encryption_text = tk.Text(self.encryption_window, height=6, width=60, bg="#3E3E3E", fg="white", font=("Helvetica", 12), wrap=tk.WORD)
        self.encryption_text.pack(pady=(0, 10))

        # Algorithm selection for encryption
        self.encryption_algorithm_var = tk.StringVar(value="Select Algorithm")
        self.encryption_algorithm_menu = tk.OptionMenu(self.encryption_window, self.encryption_algorithm_var, 
                                                         'Caesar Cipher', 
                                                         'Rail Fence Cipher', 
                                                         'Row Matrix', 
                                                         'Substitution Cipher', 
                                                         'Vigenère Cipher')
        self.encryption_algorithm_menu.config(bg="#3E3E3E", fg="white", font=("Helvetica", 12))
        self.encryption_algorithm_menu.pack(pady=(0, 10))

        # Encrypt button
        encrypt_button = tk.Button(
            self.encryption_window,
            text="Encrypt",
            command=self.encrypt_text,
            bg="skyblue",
            font=("Helvetica", 14)
        )
        encrypt_button.pack(pady=(10, 10))

        # Result label for encrypted text
        self.encrypted_result_label = tk.Label(
            self.encryption_window,
            text="Encrypted Text Will Appear Here",
            font=("Helvetica", 14),
            fg="white",
            bg="#2E2E2E",
            wraplength=450
        )
        self.encrypted_result_label.pack(pady=(10, 20))

        # Copy button
        copy_button = tk.Button(
            self.encryption_window,
            text="Copy Encrypted Text",
            command=self.copy_encrypted_text,
            bg="skyblue",
            font=("Helvetica", 12)
        )
        copy_button.pack(pady=(10, 10))

    def encrypt_text(self):
        """Encrypt the input text based on the selected algorithm in the encryption window."""
        selected_algorithm = self.encryption_algorithm_var.get()
        input_text = self.encryption_text.get(1.0, tk.END).strip()

        # Perform encryption based on selected algorithm
        if selected_algorithm == 'Caesar Cipher':
            encrypted = caesar_encrypt(input_text, shift=3)  # Example shift value
        elif selected_algorithm == 'Rail Fence Cipher':
            encrypted = rail_fence_encrypt(input_text, key=3)  # Example key
        elif selected_algorithm == 'Row Matrix':
            encrypted = row_matrix_encrypt(input_text, key=[1, 2, 3])  # Example key
        elif selected_algorithm == 'Substitution Cipher':
            encrypted = substitution_encrypt(input_text, mapping={'a': 'z', 'b': 'y', 'c': 'x'})  # Example mapping
        elif selected_algorithm == 'Vigenère Cipher':
            encrypted = vigenere_encrypt(input_text, key='KEYWORD')  # Example key
        else:
            encrypted = "Invalid Algorithm or Input"

        # Display the encrypted text
        self.encrypted_result_label.config(text=f"Encrypted Text: {encrypted}")
        self.encrypted_text = encrypted

    def copy_encrypted_text(self):
        """Copy the encrypted text to the clipboard."""
        self.root.clipboard_clear()  # Clear the clipboard
        self.root.clipboard_append(self.encrypted_text)  # Copy encrypted text
        messagebox.showinfo("Copied", "Encrypted text copied to clipboard!")

if __name__ == '__main__':
    root = tk.Tk()
    app = DecryptorApp(root)
    root.mainloop()
