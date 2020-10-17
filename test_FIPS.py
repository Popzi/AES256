import unittest
from keyManager import createRoundKey,expandKey
from readKeyFile import getKey

class TestKeys(unittest.TestCase):
    keys = [
        '0123456789abcdef',
        '101112131415161718191a1b1c1d1e1f',
        'a573c29fa176c498a97fce93a572c09c',
        '1651a8cd244beda1a5da4c1640bade',
        'ae87dff0ff11b68a68ed5fb3fc1567',
        '6de1f1486fa54f9275f8eb5373b8518d',
        'c656827fc9a799176f294cec6cd5598b',
        '3de23a75524775e727bf9eb4547cf39',
        'bdc905fc27b948ad5245a4c1871c2f',
        '45f5a66017b2d38730d4d3364a82a',
        '7ccff71cbeb4fe5413e6bbf0d261a7df',
        'f01afafee7a82979d7a5644ab3afe640',
        '2541fe719bf50258813bbd55a721ca',
        '4e5a6699a9f24fe07e572baacdf8cdea',
        '8ea2b7ca516745bfeafc49904b496089'
        ]

    def test_encrypt_keys(self):
        key = getKey("testKey")
        expandedkey = expandKey(key)
        for i in range (14):
            with self.subTest(i=i):
                self.assertEqual(print_hex(createRoundKey(expandedkey,i)), TestKeys.keys[i])
        
    def test_decrypt_keys(self):
        key = getKey("testKey")
        expandedkey = expandKey(key)
        for i in range(13,0,-1):
            with self.subTest(i=i):
                self.assertEqual(print_hex(createRoundKey(expandedkey,i)), TestKeys.keys[i])

def print_hex(key):
    return ''.join(hex(x)[2:] for x in key)

if __name__ == '__main__':
    unittest.main()