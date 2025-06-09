class Vehicle:
    def __init__(self, id: int, type: str, rent: int, is_available: bool ):
        self.id = id
        self.type = type
        self.rent = rent
        self.is_available = is_available

    def calculate_cost(self,days:int) -> float:
        return self.rent * days

    def mark_rented(self):
        self.is_available = False

    def mark_returned(self):
        self.is_available = True

    def __str__(self):
        return f"[{self.id}] {self.type} - {self.rent} per day - Available {["yes" if self.is_available else "No"]}"




