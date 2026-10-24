class Contact:
    def __init__(self, ismi, telefonraqami):
        self.ismi = ismi
        self.telefonraqami = telefonraqami

    def update_phone(self, new_phone):
        self.telefonraqami = new_phone

    def show_info(self):
        print(f"Ism: {self.ismi}")
        print(f"Telefon: {self.telefonraqami}")


contact = Contact('Malika', '901234567')
contact.update_phone('931112233')
contact.show_info()