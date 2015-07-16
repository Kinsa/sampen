from setuptools import setup


setup(
    name='sampen',
    version='0.0.1',
    description='A Python module to calculate Sample Entropy (SampEn).',
    url='https://github.com/jbergantine/sampen',
    author='Joe Bergantine',
    license='GNU',
    packages=['sampen'],
    install_requires=[
        'numpy>=1.9.2',
    ],
    zip_safe=False
)
