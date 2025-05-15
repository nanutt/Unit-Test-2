class FlowerRepository:
    def __init__(self):
        self.flowers = {}

    def add(self, flower):
        self.flowers[flower.name] = flower

    def get(self, name):
        return self.flowers.get(name)

    def delete(self, name):
        if name in self.flowers:
            del self.flowers[name]
            return True
        return False

    def update(self, name, new_description):
        if name in self.flowers:
            self.flowers[name].description = new_description
            return True
        return False

    def list_all(self):
        return list(self.flowers.values())