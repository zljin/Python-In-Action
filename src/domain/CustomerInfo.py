class CustomerInfo:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def __str__(self):
        return f"CustomerInfo(name={self.name}, age={self.age}, score={self.score})"
