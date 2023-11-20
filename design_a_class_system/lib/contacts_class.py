class Contact:
    def __init__(self, name, phone_number):
        if type(name) != str or type(phone_number) != str:
            raise Exception('Both of these values need to be a string!')
        self.name = name
        self.phone_number = phone_number
    
    def format_contact(self):
        return f"{self.name}:{self.phone_number}"