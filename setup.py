from setuptools import setup


setup(
    name='sampen',
    version='0.0.11',
    description='A Python module to calculate Sample Entropy (SampEn) of a'
                ' time series.',
    url='http://www.physionet.org/physiotools/sampen',
    download_url='https://github.com/jbergantine/sampen/tarball/0.0.11/',
    author='Doug Lake',
    author_email='dlake@virginia.edu',
    maintainer='Joe Bergantine',
    maintainer_email='joe@kinsa.us',
    license='GNU',
    packages=['sampen'],
    install_requires=[
        'numpy>=1.9.2',
    ],
    keywords=['sample entropy', 'sampen'],
    test_suite="tests.test_sampen",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
    ]
)
