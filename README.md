sampen
======

Python code to calculate [Sample Entropy (SampEn)](http://www.physionet.org/physiotools/sampen/). Partial port of v1.2 C-language code from [PhysioNet](http://www.physionet.org/physiotools/sampen/c/) last updated 1 November 2004, by George Moody. Original functions not ported: `readdata()`, `sampen()`. Functions ported: `normalize_data()`, `sampen2()`.

Installation
------------

### Via PIP

```sh
$ pip install sampen
```

### Via Git

Clone the repo:

```sh
$ git clone git@github.com:jbergantine/sampen.git
```

This will create a new directory with the repo in it. Change into that directory and execute `setup.py`:

```sh
$ cd $_
$ python setup.py install
```

Usage
-----

Unlike the original C code which loads time series data either from standard input or a file, this script expects the time series to be expressed in a list of floats. If the time series exists in a flat text file that can be loaded into Python and saved into a list:

```py
from sampen import sampen2


# initialize a list
series_data = []

# open the file and read each line into the list
with open('relative/path/to/file.txt', 'r') as file:
    for row in file:
        series_data.append(float(row.strip(' \t\n\r')))

# calculate the sample entroyp
sampen_of_series = sampen2(series_data)
```

The default maximum epoch length (`m`) is `2`, the default tolerance (`r`) is `0.2`.

The estimate of the conditional probability that the subseries of the epoch length that matches pointwise within the tolerance (that is, the Sample Entropy) will be the last item in the returned tuple.

The earlier items in the returned tuple will be the sample entropies for lengths 0 up to the maximum epoch.

Therefore, inspecting the returned data:

```py
>>> sampen_of_series
```

Return something like:

```py
[
    (0, 2.140629540027156, 0.0028357991885715863)
    (1, 2.162868347337613, 0.004903248034526253),
    (
        # Epoch length for max epoch
        2,
        # SampEn
        2.123328492035711,
        # Standard Deviation
        0.007596323621379352
    ),
]
```

Running Tests
-------------

For development, from the repo (if the package is installed rather than simply cloned, skip setting the PYTHONPATH):

```sh
$ PYTHONPATH=$PYTHONPATH:./sampen/ export PYTHONPATH; python ./tests/test_sampen.py
```

Contributing
------------

1. Fork the repository on Github
2. Create a named feature branch (like `feature/add_component_x`)
3. Write your change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using Github