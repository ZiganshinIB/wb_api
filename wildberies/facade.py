from .supply import SupplyAPI

class WildberriesAPI:

    def __init__(self, token):
        self.token = token
        self.supply = SupplyAPI(self)



