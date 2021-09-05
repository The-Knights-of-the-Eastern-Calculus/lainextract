import wave
import numpy as np

with open('file_list.txt', 'r') as f:
    filenames = f.readlines()

offsets = np.fromfile('voice_offset_table.bin', dtype=np.uint32)

with open('voice.bin', 'rb') as f:
    voice_data = f.read()

for i, file in enumerate(filenames):
    offset = offsets[i * 2] * 2048
    size = offsets[i * 2 + 1]
    print(f'{file.strip()}: offset - {offset}, size - {size}')
    if i not in [9, 10, 11]: # bya, byo, byu are already in wav
        with wave.open('extracted/' + file.strip(), 'wb') as wav_file:
            wav_file.setparams((1, 2, 22050, 0, 'NONE', 'NONE')) # mono, 16bit, 22050Khz
            wav_file.writeframes(voice_data[offset:offset + size])
    else:
        with open('extracted/' + file.strip(), 'wb') as f:
            f.write(voice_data[offset:offset + size])

