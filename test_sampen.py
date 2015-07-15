import unittest

from sampen import sampen_with_variance


class SampEnTests(unittest.TestCase):
    def test_sampen_with_variance(self):
        data = []

        with open('sampentest.txt', 'r') as file:
            for row in file:
                data.append(float(row.strip(' \t\n\r')))

        self.assertEqual(
            sampen_with_variance(data, mm=5, normalize=True),
            [
                (0, 2.1965947354057174, 0.002685407401832965),
                (1, 2.2242457199296832, 0.004642522636570079),
                (2, 2.1980190478634287, 0.007533356114576163),
                (3, 2.1552015875613715, 0.017693023262169073),
                (4, 2.315007612992603, 0.0331496460180921),
                (5, None, None),
            ]
        )


if __name__ == '__main__':
    unittest.main()
