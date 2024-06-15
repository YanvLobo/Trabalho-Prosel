import tkinter as tk
from views.incident_view import IncidentView
from models.incident import Incident

class IncidentController:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.view = IncidentView(self.root, self)
    
    def report_incident(self, transport_id, descricao):
        incident = Incident(transport_id, descricao)
        print("Incidente relatado:", incident)

    def __init__(self, root):
        self.view = IncidentView(root, self)

    def report_incident(self, transport_id, descricao):
        Incident(transport_id, descricao)
        self.view.load_incidents()