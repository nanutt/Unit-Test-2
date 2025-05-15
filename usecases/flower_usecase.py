from repositories.flower_repository import FlowerRepository
from entities.flower import Flower

class FlowerUsecase:
    def __init__(self, repo=None):
        self.repo = repo if repo else FlowerRepository()


    def add_flower(self, name, description):
        flower = Flower(name, description)
        self.repo.add(flower)
        return flower

    def get_flower(self, name):
        return self.repo.get(name)

    def update_flower(self, name, description):
        return self.repo.update(name, description)

    def delete_flower(self, name):
        return self.repo.delete(name)

    def list_flowers(self):
        return self.repo.list_all()