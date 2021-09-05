import numpy as np
import json

offsets = np.fromfile('lapks_offset_table.bin', dtype=np.uint32)

out = []

for i in range(59):
    offset = offsets[i * 2] * 2048
    size = offsets[i * 2 + 1]
    print(f'{i}: offset - {offset}, size - {size}')
    out.append({'output_name': '', 'offset': int(offset), 'size': int(size)})
    print(out[-1])

with open('lapks.json', 'w') as f:
    json.dump(out, f)

