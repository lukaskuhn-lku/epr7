from member import Member

class WiMi(Member):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        print("WiMi created: " + str(id) + " | " + str(name))