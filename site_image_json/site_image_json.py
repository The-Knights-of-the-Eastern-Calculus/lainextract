import numpy as np
import json

site_a_offsets = np.fromfile('sitea_offset_table.bin', dtype=np.uint32)
site_b_offsets = np.fromfile('siteb_offset_table.bin', dtype=np.uint32)

site_a_out = []
site_b_out = []

for i in range(790):
    offset = site_a_offsets[i * 2] * 2048
    size = site_a_offsets[i * 2 + 1]
    print(f'{i}: offset - {offset}, size - {size}')
    site_a_out.append({'offset': int(offset), 'size': int(size), 'is_compressed':True})
    print(site_a_out[-1])

for i in range(558):
    offset = site_b_offsets[i * 2] * 2048
    size = site_b_offsets[i * 2 + 1]
    print(f'{i}: offset - {offset}, size - {size}')
    site_b_out.append({'offset': int(offset), 'size': int(size), 'is_compressed':True})
    print(site_b_out[-1])

with open('site_a_images.json', 'w') as f:
    json.dump(site_a_out, f)

with open('site_b_images.json', 'w') as f:
    json.dump(site_b_out, f)
