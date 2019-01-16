class Research_Group:
    member = []
    head_member = None

    def __init__(self, name, total_presentation):
        self.name = name
        self.total_presentation = total_presentation
        print("Research_Group created: " + str(name) + " | " + str(total_presentation))

    def get_member(self):
        return self.member
    
    def get_head(self):
        return self.head_member

    def set_head(self,member):
        self.head_member = member

    def add_member(self,member):
        self.member.append(member)
