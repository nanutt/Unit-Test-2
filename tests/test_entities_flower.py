import unittest
from entities.flower import Flower

class TestFlowerEntity(unittest.TestCase):
    def test_create_flower(self):
        flower = Flower("Rose", "Red flower")
        self.assertEqual(flower.name, "Rose")
        self.assertEqual(flower.description, "Red flower")

    def test_flower_str_representation(self):
        flower = Flower("Lily", "White flower")
        expected = "Flower(name='Lily', description='White flower')"
        self.assertEqual(str(flower), expected)

    def test_flower_update_attributes(self):
        flower = Flower("Tulip", "Pink flower")
        flower.name = "Tulip Updated"
        flower.description = "New description"
        self.assertEqual(flower.name, "Tulip Updated")
        self.assertEqual(flower.description, "New description")

if __name__ == '__main__':
    unittest.main()
