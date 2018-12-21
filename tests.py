import unittest
import scorer

class Tester(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(scorer.scorer('X-X-X-X-X-X-X-X-X-X-XX'), 300)

    def test_2(self):
        self.assertEqual(scorer.scorer('45-54-36-27-09-63-81-18-90-72'), 90)
    
    def test_3(self):
        self.assertEqual(scorer.scorer('5/-5/-5/-5/-5/-5/-5/-5/-5/-5/-5'), 150)
    
    def test_4(self):
        self.assertEqual(scorer.scorer('45-54-36-27-09-63-81-18-90-7/-5'), 96)
        
if __name__ == '__main__':
    unittest.main()