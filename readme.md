sampen
======

Python code to calculate Sample Entropy (SampEn). Partial port of C code from [PhysioNet](http://www.physionet.org/physiotools/sampen). (The method to calculate Sample Entropy without variance not yet ported.)

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
