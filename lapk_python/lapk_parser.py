from construct import *

lapk_cell_data = Struct(
    'width' / Int16ul,
    'height' / Int16ul,
    'chrominance_quantisation_scale' / Int16ul,
    'luminance_quantisation_scale' / Int16ul,
    'image_data_size' / Int32ul,
    'run_length_code_count' / Int32ul,
    'image_data' / Bytes(this.image_data_size)
)

lapk_cell = Struct(
    'cell_offset' / Int32ul,
    'negative_x_position' / Int16ul,
    'negative_y_position' / Int16ul,
    'unknown' / Int32ul
)

lapk_header = Struct(
    'signature' / Const(b'lapk'),
    'size' / Int32ul,
    'cell_count' / Int32ul,
    'cells' / lapk_cell[this.cell_count],
    'cell_data' / lapk_cell_data[this.cell_count]
)

