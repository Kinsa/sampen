from setuptools import setup


setup(
    name='sampen',
    version='0.0.2',
    description='A Python module to calculate Sample Entropy (SampEn) of a'
                ' time series.',
    url='http://www.physionet.org/physiotools/sampen',
    download_url='https://github.com/jbergantine/sampen/tarball/0.0.1/',
    author='Doug Lake',
    author_email='dlake@virginia.edu',
    maintainer='Joe Bergantine',
    maintainer_email='joe@kinsa.us',
    license='GNU',
    packages=['sampen'],
    install_requires=[
        'numpy>=1.9.2',
    ],
    keywords=['sample entropy', 'sampen']
)
