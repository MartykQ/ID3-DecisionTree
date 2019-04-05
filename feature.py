class Feature:
    def __init__(self, name, answers):
        self.name = name
        self.answers = answers

    def __str__(self):
        return self.name + ": " + str(self.answers)


