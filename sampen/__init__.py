import math
import numpy as np

"""SAMPLE ENTROPY

---------------------------------------------------------------------------
Last revised: 15 July 2015 (by joe@kinsa.us)

Modified version (ported C code to Python, modified to run as a callable
function) of original code:

sampen: calculate Sample Entropy
Copyright (C) 2002-2004 Doug Lake

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.  You may also
view the agreement at http://www.fsf.org/copyleft/gpl.html.

You may contact the author via electronic mail (dlake@virginia.edu).
For updates to this software, please visit PhysioNet
(http://www.physionet.org/).

"""


def normalize_data(data):
    """
    Normalize such that the mean of the input is 0 and the sample variance is 1

    :param data: The data set, expressed as a flat list of floats.
    :return: The normalized data set, as a flat list of floats.

    """

    var = 0.0
    n = len(data)

    mean = np.mean(data)

    for i in range(n):
        data[i] += data[i] - mean
        var += data[i] * data[i]

    var = math.sqrt(var / float(n))

    for i in range(n):
        data[i] = data[i] / var

    return data


def sampen2(data, mm=2, r=0.2, normalize=False):
    """
    Calculates an estimate of sample entropy and the variance of the estimate.

    :param data: The data set, expressed as a flat list of floats.
    :param mm: Maximum epoch length, expressed as an int. Default is m = 2.
    :param r: Tolerance, expressed as a float. Typically 0.1 or 0.2.
    :param normalize: Normalize such that the mean of the input is 0 and the
    sample, variance is 1
    :return: A list of tuples of the format [(epoch length as Int, sample
    entropy as Float or None, standard deviation as Float or None), ...]

    """

    n = len(data)

    if n == 0:
        raise ValueError("Parameter `data` contains an empty list")

    if mm > n / 2:
        raise ValueError(
            "Maximum epoch length of %d too large for time series of length "
            "%d (mm > n / 2)" % (
                mm,
                n,
            )
        )

    mm += 1

    MM = 2 * mm

    if MM > n:
        raise ValueError(
            "Maximum epoch length of %d too large for time series of length "
            "%d ((mm + 1) * 2 > n)" % (
                mm,
                n,
            )
        )

    if normalize is True:
        data = normalize_data(data)

    # initialize the lists
    run = [0] * n
    run1 = run[:]

    R1 = [0] * (n * MM)
    R2 = R1[:]
    F = R1[:]

    F1 = [0] * (n * mm)
    F2 = F1[:]

    K = [0] * ((mm + 1) * mm)

    A = [0] * mm
    B = A[:]
    p = A[:]
    v1 = A[:]
    v2 = A[:]
    s1 = A[:]
    n1 = A[:]
    n2 = A[:]

    for i in range(n - 1):
        nj = n - i - 1
        y1 = data[i]

        for jj in range(nj):
            j = jj + i + 1

            if data[j] - y1 < r and y1 - data[j] < r:
                run[jj] = run1[jj] + 1
                m1 = mm if mm < run[jj] else run[jj]

                for m in range(m1):
                    A[m] += 1
                    if j < n - 1:
                        B[m] += 1
                    F1[i + m * n] += 1
                    F[i + n * m] += 1
                    F[j + n * m] += 1

            else:
                run[jj] = 0

        for j in range(MM):
            run1[j] = run[j]
            R1[i + n * j] = run[j]

        if nj > MM - 1:
            for j in range(MM, nj):
                run1[j] = run[j]

    for i in range(1, MM):
        for j in range(i - 1):
            R2[i + n * j] = R1[i - j - 1 + n * j]
    for i in range(MM, n):
        for j in range(MM):
            R2[i + n * j] = R1[i - j - 1 + n * j]
    for i in range(n):
        for m in range(mm):
            FF = F[i + n * m]
            F2[i + n * m] = FF - F1[i + n * m]
            K[(mm + 1) * m] += FF * (FF - 1)
    m = mm - 1
    while m > 0:
        B[m] = B[m - 1]
        m -= 1
    B[0] = float(n) * (n - 1.0) / 2.0
    for m in range(mm):
        p[m] = float(A[m]) / float(B[m])
        v2[m] = p[m] * (1.0 - p[m]) / B[m]
    for m in range(mm):
        d2 = m + 1 if m + 1 < mm - 1 else mm - 1
        for d in range(d2):
            for i1 in range(d + 1, n):
                i2 = i1 - d - 1
                nm1 = F1[i1 + n * m]
                nm3 = F1[i2 + n * m]
                nm2 = F2[i1 + n * m]
                nm4 = F2[i2 + n * m]
                # if R1[i1 + n * j] >= m + 1:
                #    nm1 -= 1
                # if R2[i1 + n * j] >= m + 1:
                #    nm4 -= 1
                for j in range(2 * (d + 1)):
                    if R2[i1 + n * j] >= m + 1:
                        nm2 -= 1
                for j in range(2 * d + 1):
                    if R1[i2 + n * j] >= m + 1:
                        nm3 -= 1
                K[d + 1 + (mm + 1) * m] += float(2 * (nm1 + nm2) * (nm3 + nm4))

    n1[0] = float(n * (n - 1) * (n - 2))
    for m in range(mm - 1):
        for j in range(m + 2):
            n1[m + 1] += K[j + (mm + 1) * m]
    for m in range(mm):
        for j in range(m + 1):
            n2[m] += K[j + (mm + 1) * m]

    # calculate standard deviation for the set
    for m in range(mm):
        v1[m] = v2[m]
        dv = (n2[m] - n1[m] * p[m] * p[m]) / (B[m] * B[m])
        if dv > 0:
            v1[m] += dv
        s1[m] = math.sqrt(v1[m])

    # assemble and return the response
    response = []
    for m in range(mm):
        if p[m] == 0:
            # Infimum, the data set is unique, there were no matches.
            response.append((m, None, None))
        else:
            response.append((m, -math.log(p[m]), s1[m]))
    return response
