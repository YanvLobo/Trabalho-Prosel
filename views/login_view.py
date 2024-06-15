import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from models.user import User

class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.window = tk.Toplevel(self.root)
        self.window.title("Login")
        self.window.geometry("350x250")
        self.window.resizable(False, False)

        style = ttk.Style(self.window)
        style.theme_use("clam")
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12))

        frame = ttk.Frame(self.window, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        title_label = ttk.Label(frame, text="Por favor, faça o login", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=(0, 20))

        ttk.Label(frame, text="Username:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.username_entry = ttk.Entry(frame, width=25)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(frame, text="Password:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.password_entry = ttk.Entry(frame, show="*", width=25)
        self.password_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=(20, 0))

        login_button = ttk.Button(button_frame, text="Login", command=self.login)
        login_button.grid(row=0, column=0, padx=5)

        cancel_button = ttk.Button(button_frame, text="Cancelar", command=self.window.destroy)
        cancel_button.grid(row=0, column=1, padx=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = User.authenticate(username, password)
        if user:
            self.controller.user = user
            self.window.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

