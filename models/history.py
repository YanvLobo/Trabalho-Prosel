class History:
   histories = []

def __init__(self, transport_id, descricao):
        self.transport_id = transport_id
        self.descricao = descricao
        self.data_hora = "06/06/2024 - 07:50:21"
        History.histories.append(self)

@classmethod
def get_all(cls):
        return cls.histories
