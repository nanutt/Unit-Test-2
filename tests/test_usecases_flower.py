import unittest
from usecases.flower_usecase import FlowerUsecase
from entities.flower import Flower

class TestFlowerUsecase(unittest.TestCase):
    def setUp(self):
        self.usecase = FlowerUsecase()

    # TEST ADD FLOWER 
    def test_add_flower_success(self):
        flower = self.usecase.add_flower("Kamboja", "Kuning")
        self.assertEqual(flower.name, "Kamboja")
        self.assertEqual(flower.description, "Kuning")
        self.assertIsInstance(flower, Flower)

    def test_add_flower_duplicate(self):
        self.usecase.add_flower("Melati", "Putih")
        flower = self.usecase.add_flower("Melati", "Putih")
        self.assertEqual(flower.name, "Melati")

    def test_add_flower_empty_name(self):
        flower = self.usecase.add_flower("", "Hijau")
        self.assertEqual(flower.name, "")
        self.assertEqual(flower.description, "Hijau")

    # TEST GET FLOWER 
    def test_get_flower_success(self):
        self.usecase.add_flower("Tulip", "Merah")
        flower = self.usecase.get_flower("Tulip")
        self.assertIsNotNone(flower)
        self.assertEqual(flower.description, "Merah")

    def test_get_flower_not_exist(self):
        flower = self.usecase.get_flower("TidakAda")
        self.assertIsNone(flower)

    def test_get_flower_after_update(self):
        self.usecase.add_flower("Aster", "Kuning")
        self.usecase.update_flower("Aster", "Merah")
        flower = self.usecase.get_flower("Aster")
        self.assertEqual(flower.description, "Merah")


    # TEST DELETE FLOWER 
    def test_delete_flower_success(self):
        self.usecase.add_flower("Anggrek", "Ungu")
        self.assertTrue(self.usecase.delete_flower("Anggrek"))
        self.assertIsNone(self.usecase.get_flower("Anggrek"))

    def test_delete_flower_not_exist(self):
        self.assertFalse(self.usecase.delete_flower("TidakAda"))

    def test_delete_flower_twice(self):
        self.usecase.add_flower("Kenanga", "Putih")
        self.usecase.delete_flower("Kenanga")
        result = self.usecase.delete_flower("Kenanga")
        self.assertFalse(result)

    # TEST UPDATE FLOWER 
    def test_update_flower_success(self):
        self.usecase.add_flower("Dahlia", "Merah")
        self.assertTrue(self.usecase.update_flower("Dahlia", "Pink"))
        self.assertEqual(self.usecase.get_flower("Dahlia").description, "Pink")

    def test_update_flower_not_exist(self):
        result = self.usecase.update_flower("TidakAda", "Biru")
        self.assertFalse(result)

    def test_update_flower_same_value(self):
        self.usecase.add_flower("Lavender", "Ungu")
        result = self.usecase.update_flower("Lavender", "Ungu")
        self.assertTrue(result)
        self.assertEqual(self.usecase.get_flower("Lavender").description, "Ungu")

    # TEST LIST FLOWERS 
    def test_list_flowers_non_empty(self):
        self.usecase.add_flower("Lily", "Putih")
        flowers = self.usecase.list_flowers()
        self.assertGreaterEqual(len(flowers), 1)

    def test_list_flowers_empty(self):
        flowers = self.usecase.list_flowers()
        self.assertEqual(len(flowers), 0)

    def test_list_flowers_after_delete(self):
        self.usecase.add_flower("Sepatu", "Merah")
        self.usecase.delete_flower("Sepatu")
        flowers = self.usecase.list_flowers()
        self.assertEqual(len(flowers), 0)


if __name__ == '__main__':
    unittest.main()
