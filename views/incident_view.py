import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from models.incident import Incident
from models.transport_request import TransportRequest

class IncidentView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.window = tk.Toplevel(self.root)
        self.window.title("Gerenciar Incidentes")
        self.window.geometry("800x600")

        style = ttk.Style(self.window)
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#D3D3D3")
        style.map("Treeview", background=[("selected", "#347083")])

        frame = ttk.Frame(self.window, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.tree = ttk.Treeview(frame, columns=('ID', 'Transporte', 'Descrição', 'Data/Hora'), show='headings', selectmode="browse")
        self.tree.heading('ID', text='ID')
        self.tree.heading('Transporte', text='Transporte')
        self.tree.heading('Descrição', text='Descrição')
        self.tree.heading('Data/Hora', text='Data/Hora')
        self.tree.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

        self.tree_scroll = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.tree_scroll.set)
        self.tree_scroll.grid(row=0, column=4, sticky='ns')

        self.load_incidents()

        ttk.Label(frame, text="ID do Transporte:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.transport_id_entry = ttk.Entry(frame)
        self.transport_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(frame, text="Descrição do Incidente:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.description_entry = ttk.Entry(frame)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        add_button = ttk.Button(frame, text="Registrar Incidente", command=self.add_incident)
        add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        button_frame = ttk.Frame(self.window)
        button_frame.grid(row=1, column=0, columnspan=5, pady=(10, 10))

        refresh_button = ttk.Button(button_frame, text="Atualizar", command=self.load_incidents)
        refresh_button.grid(row=0, column=0, padx=5)

        close_button = ttk.Button(button_frame, text="Fechar", command=self.window.destroy)
        close_button.grid(row=0, column=1, padx=5)

    def load_incidents(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for incident in Incident.get_all():
            self.tree.insert("", "end", values=(incident.id, incident.transport_id, incident.descricao, incident.timestamp))

    def add_incident(self):
        transport_id = self.transport_id_entry.get()
        description = self.description_entry.get()
        if transport_id and description:
            self.controller.report_incident(transport_id, description)
            self.load_incidents()
            self.controller.refresh_history_view() 
            messagebox.showinfo("Sucesso", "Incidente registrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")


