class Ticket:
    def __init__(self, movie, price, count):
        self.movie = movie
        self.price = price
        self.count = count

    def total_cost(self):
        return self.price * self.count

    def show_info(self):
        print(f"Film: {self.movie}")
        print(f"Chipta narxi: {self.price}")
        print(f"Chipta soni: {self.count}")
        print(f"Umumiy narx: {self.total_cost()}")


ticket = Ticket('Avatar', 40000, 3)
print(ticket.total_cost)
ticket.show_info()