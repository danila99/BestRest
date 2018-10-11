from mapsJson import get_best_restaurant
import unittest

class TestRestaurants(unittest.TestCase):
    
    def test_best_restaurant_1(self):
        restaurants = [
            {"rating": 5.0, "name": "Restr Five"},
            {"rating": 4.4, "name": "Restr Four"},
            {"rating": 3.3, "name": "Restr Three"},
            {"rating": 2.2, "name": "Restr Two"},
            {"rating": 1.0, "name": "Restr One"},
        ]
        r = get_best_restaurant(restaurants)
        self.assertEqual(r["name"], "Restr Five")

    def test_best_restaurant_2(self):
        restaurants = [
            {"rating": 1.0, "name": "Restr One"},
            {"rating": 2.2, "name": "Restr Two"},
            {"rating": 4.4, "name": "Restr Four"},
            {"rating": 3.3, "name": "Restr Three"},
            {"rating": 5.0, "name": "Restr Five"},
        ]
        r = get_best_restaurant(restaurants)
        self.assertEqual(r["name"], "Restr Five")

    def test_best_restaurant_3(self):
        restaurants = [
            {"rating": 1.0, "name": "Restr One"},
            {"rating": 2.2, "name": "Restr Two"},
            {"name": "Restr Four"},
            {"rating": 5.0, "name": "Restr Five"},
            {"rating": 3.3, "name": "Restr Three"},
        ]
        r = get_best_restaurant(restaurants)
        self.assertEqual(r["name"], "Restr Five")


if __name__ == '__main__':
    unittest.main()


