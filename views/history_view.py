import tkinter as tk
from tkinter import ttk
from models.transport_request import TransportRequest
from models.incident import Incident

class HistoryView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.window = tk.Toplevel(self.root)
        self.window.title("Histórico de Transportes")
        self.window.geometry("1400x600")

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
        
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # Treeview for Transport Requests
        self.tree = ttk.Treeview(frame, columns=('ID', 'Paciente', 'Origem', 'Destino', 'Prioridade', 'Status', 'Ação por'), show='headings', selectmode="browse")
        self.tree.heading('ID', text='ID')
        self.tree.heading('Paciente', text='Paciente')
        self.tree.heading('Origem', text='Origem')
        self.tree.heading('Destino', text='Destino')
        self.tree.heading('Prioridade', text='Prioridade')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Ação por', text='Ação por')
        self.tree.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

        self.tree_scroll = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.tree_scroll.set)
        self.tree_scroll.grid(row=0, column=4, sticky='ns')

        self.load_history()

        # Separator
        ttk.Label(frame, text="Histórico de Incidentes", font=("Helvetica", 14, "bold")).grid(row=1, column=0, columnspan=4, padx=5, pady=(20, 5))

        # Treeview for Incidents
        self.incident_tree = ttk.Treeview(frame, columns=('ID', 'Transporte', 'Descrição', 'Data/Hora'), show='headings', selectmode="browse")
        self.incident_tree.heading('ID', text='ID')
        self.incident_tree.heading('Transporte', text='Transporte')
        self.incident_tree.heading('Descrição', text='Descrição')
        self.incident_tree.heading('Data/Hora', text='Data/Hora')
        self.incident_tree.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

        self.incident_scroll = ttk.Scrollbar(frame, orient="vertical", command=self.incident_tree.yview)
        self.incident_tree.configure(yscroll=self.incident_scroll.set)
        self.incident_scroll.grid(row=2, column=4, sticky='ns')

        self.load_incidents()

        # Buttons
        button_frame = ttk.Frame(self.window)
        button_frame.grid(row=3, column=0, columnspan=5, pady=(20, 10))

        refresh_button = ttk.Button(button_frame, text="Atualizar", command=self.refresh)
        refresh_button.grid(row=0, column=0, padx=5)

        close_button = ttk.Button(button_frame, text="Fechar", command=self.window.destroy)
        close_button.grid(row=0, column=1, padx=5)

    def load_history(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for request in TransportRequest.get_all():
            self.tree.insert("", "end", values=(request.id, request.patient_name, request.initial_point, request.destination_point, request.priority, request.status, request.assigned_to))

    def load_incidents(self):
        for row in self.incident_tree.get_children():
            self.incident_tree.delete(row)
        for incident in Incident.get_all():
            self.incident_tree.insert("", "end", values=(incident.id, incident.transport_id, incident.descricao, incident.data_hora))

    def refresh(self):
        self.load_history()
        self.load_incidents()

