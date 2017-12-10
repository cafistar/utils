# Python 3.5.2

def multi_key_sorted(data):
    """
    多重キーでソートする
    """
    return sorted(data, key=lambda x: (x[1], x[2]))


class MultiKeySortedTest(unittest.TestCase):

    def test_it(self):
        data = [
            ['a', 4, 101],
            ['b', 4, 102],
            ['c', 3, 104],
            ['d', 3, 103],
            ['e', 2, 103],
            ['f', 1, 999],
        ]
        self.assertEqual(
            multi_key_sorted(data),
            [
                ['f', 1, 999],
                ['e', 2, 103],
                ['d', 3, 103],
                ['c', 3, 104],
                ['a', 4, 101],
                ['b', 4, 102]
            ]
        )


if __name__ == '__main__':
    unittest.main()
