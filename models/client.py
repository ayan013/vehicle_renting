class Client:
    def __init__(self,name:str,email:str,contact:int):
        self.name = name
        self.email = email
        self.contact = contact

    def __str__(self):
        return f"Name: {self.name}\n Email: {self.email}\n Contact: {self.contact}"