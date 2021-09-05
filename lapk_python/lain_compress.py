# based on https://github.com/magical/nlzss/blob/master/lzss3.py and https://github.com/m35/jpsxdec/blob/readme/laintools/src/laintools/Lain_Pk.java
class DecompressionError(ValueError):
    pass

def LainCompress(io):

    def bits(byte):
        return ((byte >> 7) & 1,
                (byte >> 6) & 1,
                (byte >> 5) & 1,
                (byte >> 4) & 1,
                (byte >> 3) & 1,
                (byte >> 2) & 1,
                (byte >> 1) & 1,
                (byte) & 1)

    decompressed_size = io.read_u4le()
    print(f'decompressed size: {decompressed_size}')
    data = bytearray()

    while len(data) < decompressed_size:
        flags = bits(io.read_u1())
        print(f"flags: {flags}")

        for flag in flags:

            if flag == 0:
                byte = io.read_bytes(1)
                print(f"extending by byte {byte}")
                data.extend(byte)

            elif flag == 1:
                offset = io.read_u1() + 1
                size = io.read_u1() + 3
                print(f"copying from offset {offset} with size {size}")

                for _ in range(size):
                    print(f"appending {data[-offset]}")
                    data.append(data[-offset])

            else:
                raise ValueError(flag)

            if decompressed_size <= len(data):
                break

    if len(data) != decompressed_size:
        raise DecompressionError("decompressed size does not match the expected size")

    io.seek(io.pos() + 1)
    return data
