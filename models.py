class Document:
    """ Класс документа """
    reg_date: int
    personal_number: str
    description: str
    serial_number: int

    def __init__(self, personal_number,  description, serial_number):
        self.personal_number = personal_number
        self.description = description
        self.serial_number = serial_number

class BarCode:
    """ Класс баркода """
    type: str
    data: str
    location: str
    quality: int

    def __init__(self, type, data, location, quality):
        self.type = type
        self.data = data
        self.location = location
        self.quality = quality