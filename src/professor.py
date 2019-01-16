from member import Member

class Professor(Member):
    def __init__(self, id, name, cost_center_no):
        self.id = id
        self.name = name
        self._cost_center_no = cost_center_no
        print("Professor created: " + str(id) + " | " + str(name))
