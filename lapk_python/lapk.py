# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

import lain_compress
class Lapk(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x6C\x61\x70\x6B":
            raise kaitaistruct.ValidationNotEqualError(b"\x6C\x61\x70\x6B", self.magic, self._io, u"/seq/0")
        self.lapk_size = self._io.read_u4le()
        self._raw_data = self._io.read_bytes(self.lapk_size)
        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
        self.data = Lapk.LapkData(_io__raw_data, self, self._root)

    class CellHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cell_offset = self._io.read_u4le()
            self.negative_x_position = self._io.read_u2le()
            self.negative_y_position = self._io.read_u2le()
            self.unknown = self._io.read_u4le()


    class CellData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.width = self._io.read_u2le()
            self.height = self._io.read_u2le()
            self.chrominance_quantisation_scale = self._io.read_u2le()
            self.luminance_quantisation_scale = self._io.read_u2le()
            self.image_data_size = self._io.read_u4le()
            self.run_length_code_count = self._io.read_u4le()
            self.image_data = self._io.read_bytes((self.image_data_size - 4))
            self._raw_bit_mask = self._io.read_bytes_full()
            _io__raw_bit_mask = KaitaiStream(BytesIO(self._raw_bit_mask))
            self.bit_mask = lain_compress.LainCompress(_io__raw_bit_mask)


    class LapkData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cell_count = self._io.read_u4le()
            self.cell_headers = [None] * (self.cell_count)
            for i in range(self.cell_count):
                self.cell_headers[i] = Lapk.CellHeader(self._io, self, self._root)

            self._raw_cell_data = [None] * (self.cell_count)
            self.cell_data = [None] * (self.cell_count)
            for i in range(self.cell_count):
                self._raw_cell_data[i] = self._io.read_bytes(((((self._parent.lapk_size - 4) - (self.cell_count * 12)) - self.cell_headers[i].cell_offset) if i == (self.cell_count - 1) else (self.cell_headers[(i + 1)].cell_offset - self.cell_headers[i].cell_offset)))
                _io__raw_cell_data = KaitaiStream(BytesIO(self._raw_cell_data[i]))
                self.cell_data[i] = Lapk.CellData(_io__raw_cell_data, self, self._root)




