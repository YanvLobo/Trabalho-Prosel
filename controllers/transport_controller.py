import tkinter as tk
from views.transport_view import TransportView
from models.transport_request import TransportRequest

class TransportController:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.view = TransportView(self.root, self)
    
    def add_transport_request(self, patient_name, initial_point, destination_point, priority):
        request = TransportRequest(patient_name, initial_point, destination_point, priority, self.user.username)
        print("Solicitação de transporte adicionada:", request)
    
    def update_transport_status(self, transport_id, status):
        pass
    
    def update_transport_priority(self, transport_id, priority):
        pass

    def __init__(self, root):
        self.view = TransportView(root, self)

    def add_transport_request(self, patient_name, initial_point, destination_point, priority):
        TransportRequest(patient_name, initial_point, destination_point, priority)
        self.view.load_transport_requests()

    def report_incident(self, transport_id, descricao):
        TransportRequest.report_incident(transport_id, descricao)
        self.view.load_transport_requests()