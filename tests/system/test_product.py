from unittest import  TestCase

from mypage2 import app
import json
class ProductTest(TestCase):
    def test_welcome(self):
        with app.test_client() as c:
            resp = c.get('/api/products')
            self.assertEqual(resp.status_code, 200)

            self.assertEqual(json.loads(resp.get_data()),
        [{"productId": 1, "productName": "Iphone13", "price": 75444.89, "rating": 4.3},
          {"productId": 2, "productName": "SamsungGalaxyFlip", "price": 19888.89, "rating": 4.2},
          {"productId": 3, "productName": "OnePlus", "price": 65937.89, "rating": 4.5},
          {"productId": "10", "productName": "Xiaomi", "price": "24387", "rating": "4.1"},
          {"productId": "5", "productName": "nokia", "price": "5009", "rating": "3.8"}

        ])