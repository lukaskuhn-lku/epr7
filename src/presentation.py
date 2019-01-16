class Presentation:
    presenter = None

    def __init__(self, title, date):
        self.title = title
        self.date = date
        print("Presentation created: " + str(title) + " | " + str(date))

    def change_date(self, date):
        self.date = date

    def set_presenter(self, member):
        self.presenter = member
