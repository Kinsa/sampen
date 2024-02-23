from setuptools import setup


setup(
    name='sampen',
    version='0.0.19',
    description='A Python module to calculate an estimation of the '
                'Sample Entropy of a time series.',
    long_description=open("README.rst").read(),
    url='https://readthedocs.org/projects/sampen/',
    download_url='https://github.com/Kinsa/sampen/tarball/0.0.17/',
    author='Kinsa Creative Incorporated',
    author_email='enquiries@kinsa.cc',
    maintainer='Kinsa Creative Incorporated',
    maintainer_email='enquiries@kinsa.cc',
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
    ]
)
