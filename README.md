# AudioFeaturizer

The Real Python Feed Reader is a basic [web feed](https://en.wikipedia.org/wiki/Web_feed) reader that can download the latest Real Python tutorials from the [Real Python feed](https://realpython.com/contact/#rss-atom-feed).

For more information see the tutorial [How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/) on Real Python.

AudioFeaturizer is a python package that uses librosa under the hood and extracts features from audio and returns it into a pandas dataframe. 
It also has a spectrogram generation function which generates spectrogram of the audio file path which is passed. 


## Installation

You can install the AudioFeaturizer from [PyPI](https://pypi.org/project/AudioFeaturizer/):

    pip install AudioFeaturizer

The reader is supported on Python 3.7 and above.
