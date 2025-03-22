import unittest
# filepath: /home/didge/projects/docker/playground/Python1/tests/test_app.py
from html.app import subtract

class TestApp(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(100, 50), 50)

if __name__ == '__main__':
    unittest.main()