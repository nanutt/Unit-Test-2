class Flower:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Flower(name='{self.name}', description='{self.description}')"
