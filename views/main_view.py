import tkinter as tk
from tkinter import ttk

class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.window = tk.Toplevel(self.root)
        self.window.title("Menu Principal")
        self.window.geometry("400x200")

        frame = ttk.Frame(self.window, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        transport_button = ttk.Button(frame, text="Gerenciar Transportes", command=self.controller.show_transport_view)
        transport_button.grid(row=0, column=0, padx=5, pady=5)

        incident_button = ttk.Button(frame, text="Gerenciar Incidentes", command=self.controller.show_incident_view)
        incident_button.grid(row=1, column=0, padx=5, pady=5)

        history_button = ttk.Button(frame, text="Visualizar Histórico", command=self.controller.show_history_view)
        history_button.grid(row=2, column=0, padx=5, pady=5)

        logout_button = ttk.Button(frame, text="Logout", command=self.controller.logout)
        logout_button.grid(row=3, column=0, padx=5, pady=5)
