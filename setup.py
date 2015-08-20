import ez_setup

from setuptools import setup


ez_setup.use_setuptools()

setup(
    name='sampen',
    version='0.0.7',
    description='A Python module to calculate Sample Entropy (SampEn) of a'
                ' time series.',
    url='http://www.physionet.org/physiotools/sampen',
    download_url='https://github.com/jbergantine/sampen/tarball/0.0.6/',
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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Intended Audience :: Science/Research',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)
