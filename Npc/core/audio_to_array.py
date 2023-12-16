from io import BytesIO

import numpy as np
from pydub import AudioSegment

def audio_to_array(response_data):
    audio = AudioSegment.from_file(BytesIO(response_data), format="mp3")
    sample_rate = audio.frame_rate
    raw_data = audio.raw_data
    np_array = np.frombuffer(raw_data, dtype=np.int16)
    np_array = np_array.astype(np.float32) / 32767.0
    return np_array, sample_rate