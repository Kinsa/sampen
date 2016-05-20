import os
import unittest

from math import ceil

from sampen import normalize_data
from sampen import sampen2

try:
    from statistics import mean, pvariance
except ImportError:
    def mean(data):
        n = len(data)
        if n < 1:
            raise ValueError('mean requires at least one data point')
        return sum(data) / n  # in Python 2 use sum(data)/float(n)

    def _ss(data):
        """Return sum of square deviations of sequence data."""
        c = mean(data)
        ss = sum((x - c)**2 for x in data)
        return ss

    def pvariance(data):
        n = len(data)
        if n < 2:
            raise ValueError('variance requires at least two data points')
        ss = _ss(data)
        pvar = ss / n  # the population variance
        return pvar


class SampEnTests(unittest.TestCase):
    def setUp(self):
        dir = os.path.dirname(__file__)
        self.file_path = os.path.join(dir, 'sampentest.txt')

    def test_sampen2_matching_makefile(self):
        data = []

        with open(self.file_path, 'r') as file:
            for row in file:
                data.append(float(row.strip(' \t\n\r')))

        self.assertEqual(
            sampen2(data, mm=5, normalize=True),
            [
                (0, 2.196817997610929, 0.002684778756853663),
                (1, 2.2248168592127824, 0.004639787747652105),
                (2, 2.1972245773362196, 0.007540128072706757),
                (3, 2.1552015875613715, 0.017693023262169073),
                (4, 2.315007612992603, 0.0331496460180921),
                (5, None, None),
            ]
        )

    def test_sampen2_with_defaults(self):
        data = []

        with open(self.file_path, 'r') as file:
            for row in file:
                data.append(float(row.strip(' \t\n\r')))

        self.assertEqual(
            sampen2(data, mm=2, r=0.2, normalize=False),
            [
                (0, 2.140629540027156, 0.0028357991885715863),
                (1, 2.162868347337613, 0.004903248034526253),
                (2, 2.123328492035711, 0.007596323621379352)
            ]
        )


class NormalizeDataTests(unittest.TestCase):
    def test_normalize_data(self):
        data = [2.0, 3.0, 4.0]
        normalized_data = normalize_data(data)
        self.assertEqual(ceil(pvariance(normalized_data)), 1.0)
        self.assertEqual(mean(normalized_data), 0.0)


if __name__ == '__main__':
    unittest.main()
