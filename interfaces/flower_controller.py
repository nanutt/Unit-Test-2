from usecases.flower_usecase import FlowerUsecase

class FlowerController:
    def __init__(self):
        self.usecase = FlowerUsecase()

    def create(self, name, description):
        return self.usecase.add_flower(name, description)

    def read(self, name):
        return self.usecase.get_flower(name)

    def update(self, name, description):
        return self.usecase.update_flower(name, description)

    def delete(self, name):
        return self.usecase.delete_flower(name)

    def browse(self):
        return self.usecase.list_flowers()
