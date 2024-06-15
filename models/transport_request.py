class TransportRequest:
    transport_requests = []
    id_counter = 1

    def __init__(self, patient_name, initial_point, destination_point, priority, status, assigned_to=None):
        self.id = TransportRequest.id_counter
        self.patient_name = patient_name
        self.initial_point = initial_point
        self.destination_point = destination_point
        self.priority = priority
        self.status = status
        self.assigned_to = assigned_to
        TransportRequest.transport_requests.append(self)
        TransportRequest.id_counter += 1

    @staticmethod
    def get_all():
        return TransportRequest.transport_requests

    @staticmethod
    def get_transport_by_id(transport_id):
        for request in TransportRequest.transport_requests:
            if request.id == transport_id:
                return request
        return None
