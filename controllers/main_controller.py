from views.history_view import HistoryView
from views.login_view import LoginView
from views.main_view import MainView
from views.transport_view import TransportView
from views.incident_view import IncidentView
from models.transport_request import TransportRequest
from models.incident import Incident

class MainController:
    def __init__(self, root):
        self.root = root
        self.user = None
        self.show_login()

    def show_login(self):
        login_view = LoginView(self.root, self)
        self.root.wait_window(login_view.window)
        if self.user:
            self.show_main_view()

    def show_main_view(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        main_view = MainView(self.root, self)

    def show_transport_view(self):
        transport_view = TransportView(self.root, self, self.user.role)

    def show_incident_view(self):
        incident_view = IncidentView(self.root, self)

    def add_transport_request(self, patient_name, initial_point, destination_point, priority):
        if self.user.role == 'admin':
            TransportRequest(patient_name, initial_point, destination_point, priority, "Aguardando transporte")

    def show_history_view(self):
        history_view = HistoryView(self.root, self)
    
    def accept_transport_request(self, transport_id):
        if self.user.role == 'maqueiro':
            transport = TransportRequest.get_transport_by_id(transport_id)
            if transport and transport.status == 'Aguardando transporte':
                transport.status = 'Em transporte'
                transport.assigned_to = self.user.username
                self.show_transport_view()

    def reject_transport_request(self, transport_id):
        if self.user.role == 'maqueiro':
            transport = TransportRequest.get_transport_by_id(transport_id)
            if transport and transport.status == 'Aguardando transporte':
                transport.status = 'Recusado'
                transport.assigned_to = self.user.username
                self.show_transport_view()
                

    def report_incident(self, transport_id, descricao):
        Incident(transport_id, descricao)

    def logout(self):
        self.user = None
        for widget in self.root.winfo_children():
            widget.destroy()
        self.show_login()
