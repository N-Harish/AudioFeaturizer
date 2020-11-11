# AudioFeaturizer

AudioFeaturizer is a python package that uses librosa under the hood and extracts features from audio and returns it into a pandas dataframe. 
It also has a spectrogram generation function which generates spectrogram of the audio file path which is passed. 


## Installation

You can install the AudioFeaturizer from [PyPI](https://pypi.org/project/AudioFeaturizer/):

    pip install AudioFeaturizer

The reader is supported on Python 3.7 and above.


## How to Use

For extracting features
```>>> from audio_feature.audio_featurizer import *
>>> audio_process(r'D:\PYTHON_FILES\audio-ml\genres\classical\classical.00000.wav')
   chroma_stft      rmse  spectral_centroid  spectral_bandwidth  ...    mfcc17    mfcc18    mfcc19    mfcc20
0     0.252391  0.036255        1505.299012         1558.952849  ... -0.303796  1.778557  0.890328 -0.837884

[1 rows x 26 columns]
>>>
```

for displaying spectrogram
```
from audio_feature.audio_featurizer import *

spectrogram_plot(r'D:\PYTHON_FILES\audio-ml\genres\classical\classical.00000.wav')
```

