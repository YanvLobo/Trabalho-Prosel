import tkinter as tk
from tkinter import ttk
from models.transport_request import TransportRequest

class TransportView:
    def __init__(self, root, controller, user_role):
        self.root = root
        self.controller = controller
        self.user_role = user_role
        self.window = tk.Toplevel(self.root)
        self.window.title("Gerenciar Transportes")
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

        self.tree = ttk.Treeview(frame, columns=('ID', 'Paciente', 'Origem', 'Destino', 'Prioridade', 'Status'), show='headings', selectmode="browse")
        self.tree.heading('ID', text='ID')
        self.tree.heading('Paciente', text='Paciente')
        self.tree.heading('Origem', text='Origem')
        self.tree.heading('Destino', text='Destino')
        self.tree.heading('Prioridade', text='Prioridade')
        self.tree.heading('Status', text='Status')
        self.tree.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky='nsew')

        self.tree_scroll = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.tree_scroll.set)
        self.tree_scroll.grid(row=0, column=6, sticky='ns')

        self.load_transport_requests()

        if self.user_role == 'admin':
            self.create_admin_controls(frame)

        button_frame = ttk.Frame(self.window)
        button_frame.grid(row=1, column=0, columnspan=7, pady=(10, 10))

        refresh_button = ttk.Button(button_frame, text="Atualizar", command=self.load_transport_requests)
        refresh_button.grid(row=0, column=0, padx=5)

        close_button = ttk.Button(button_frame, text="Fechar", command=self.window.destroy)
        close_button.grid(row=0, column=1, padx=5)

    def create_admin_controls(self, frame):
        ttk.Label(frame, text="Nome do Paciente:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.patient_name_entry = ttk.Entry(frame)
        self.patient_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(frame, text="Origem:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.initial_point_entry = ttk.Entry(frame)
        self.initial_point_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(frame, text="Destino:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.destination_point_entry = ttk.Entry(frame)
        self.destination_point_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(frame, text="Prioridade:").grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.priority_combobox = ttk.Combobox(frame, values=["Baixa", "Média", "Alta"])
        self.priority_combobox.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        add_button = ttk.Button(frame, text="Adicionar Transporte", command=self.add_transport_request)
        add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def load_transport_requests(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for request in TransportRequest.get_all():
            self.tree.insert("", "end", values=(request.id, request.patient_name, request.initial_point, request.destination_point, request.priority, request.status))
            if self.user_role == 'maqueiro' and request.status == 'Aguardando transporte':
                self.create_transport_buttons(request)

    def create_transport_buttons(self, request):
        button_frame = ttk.Frame(self.window)
        button_frame.grid(row=request.id + 1, column=0, columnspan=7, pady=(10, 10))

        accept_button = ttk.Button(button_frame, text="Aceitar", command=lambda: self.accept_transport_request(request.id))
        accept_button.grid(row=0, column=0, padx=5)

        reject_button = ttk.Button(button_frame, text="Recusar", command=lambda: self.reject_transport_request(request.id))
        reject_button.grid(row=0, column=1, padx=5)

        complete_button = ttk.Button(button_frame, text="Concluir", command=lambda: self.complete_transport_request(request.id))
        complete_button.grid(row=0, column=2, padx=5)

    def add_transport_request(self):
        patient_name = self.patient_name_entry.get()
        initial_point = self.initial_point_entry.get()
        destination_point = self.destination_point_entry.get()
        priority = self.priority_combobox.get()
        self.controller.add_transport_request(patient_name, initial_point, destination_point, priority)
        self.load_transport_requests()

    def accept_transport_request(self, transport_id):
        self.controller.accept_transport_request(transport_id)
        self.load_transport_requests()

    def reject_transport_request(self, transport_id):
        self.controller.reject_transport_request(transport_id)
        self.load_transport_requests()

    def complete_transport_request(self, transport_id):
        self.controller.complete_transport_request(transport_id)
        self.load_transport_requests()

