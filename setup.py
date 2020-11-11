from setuptools import setup
import setuptools


setup(
    name="AudioFeaturizer",
    version="1.0.0",
    description="Takes audio as input and returns computed features as a dataframe",
    url="https://github.com/N-Harish/AudioFeaturizer",
    author_email="harishnatarajan24@gmail.com",
    author='Harish-Natarajan',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['librosa', "pandas", "numpy", "matplotlib"],
    python_requires='>=3.7'
)
