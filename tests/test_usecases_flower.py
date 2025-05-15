import unittest
from usecases.flower_usecase import FlowerUsecase
from entities.flower import Flower

class TestFlowerUsecase(unittest.TestCase):
    def setUp(self):
        self.usecase = FlowerUsecase()

    def test_add_flower(self):
        flower = self.usecase.add_flower("Kamboja", "Kuning")
        self.assertEqual(flower.name, "Kamboja")
        self.assertEqual(flower.description, "Kuning")
        self.assertIsInstance(flower, Flower)

    def test_get_flower(self):
        self.usecase.add_flower("Tulip", "Merah")
        flower = self.usecase.get_flower("Tulip")
        self.assertIsNotNone(flower)
        self.assertEqual(flower.description, "Merah")

    def test_delete_flower(self):
        self.usecase.add_flower("Anggrek", "Ungu")
        self.assertTrue(self.usecase.delete_flower("Anggrek"))
        self.assertIsNone(self.usecase.get_flower("Anggrek"))

    def test_update_flower(self):
        self.usecase.add_flower("Dahlia", "Merah")
        self.assertTrue(self.usecase.update_flower("Dahlia", "Pink"))
        self.assertEqual(self.usecase.get_flower("Dahlia").description, "Pink")

    def test_list_flowers(self):
        self.usecase.add_flower("Lily", "Putih")
        flowers = self.usecase.list_flowers()
        self.assertGreaterEqual(len(flowers), 1)


if __name__ == '__main__':
    unittest.main()
