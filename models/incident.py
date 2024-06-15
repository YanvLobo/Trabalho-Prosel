import datetime

class Incident:
    incidents = []
    next_id = 1

    def __init__(self, transport_id, descricao):
        self.id = Incident.next_id
        Incident.next_id += 1
        self.transport_id = transport_id
        self.descricao = descricao
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Incident.incidents.append(self)

    @classmethod
    def get_all(cls):
        return cls.incidents
