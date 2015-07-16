sampen
======

Python code to calculate [Sample Entropy (SampEn)](http://www.physionet.org/physiotools/sampen/). Partial port of v1.2 C-language code from [PhysioNet](http://www.physionet.org/physiotools/sampen/c/) last updated 1 November 2004, by George Moody. Original methods not ported: readdata, sampen.

Installation
------------

### Via Git

Clone the repo:

```sh
$ git clone <SSH clone URL>
```

This will create a new directory, `pyeeg` with the repo in it. Change into that directory and execute `setup.py`:

```sh
$ cd $_
$ python setup.py install
```

## Running Tests

From the repo:

```sh
$ python ./tests/test_sampen.py
```
