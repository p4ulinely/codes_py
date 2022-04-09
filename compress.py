#!/usr/bin/python3

import sys
import zlib
import mymd5

#print(sys.version[:6])

def compressing(filename_in: str, filename_out: str) -> str:
    with open(filename_in, mode="rb") as fin, open(filename_out, mode="wb") as fout:
        data = fin.read()
        compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)

        size_mb = sys.getsizeof(data)/1024/1024
        hash_original = mymd5.md5_bytes(data)
        print(f"Original size: {round(size_mb,2)}MB | md5: {hash_original}")

        size_mb = sys.getsizeof(compressed_data)/1024/1024
        hash_compressed = mymd5.md5_bytes(compressed_data)
        print(f"Compressed size: {round(size_mb,2)}MB | md5: {hash_compressed}")

        fout.write(compressed_data)

        return hash_original

def decompress(filename_in: str) -> str:
    #filename_out = "decompressed_data.csv"

    with open(filename_in, mode="rb") as fin:
        data = fin.read()
        decompressed_data = zlib.decompress(data)

        size_mb = sys.getsizeof(data)/1024/1024
        print(f"Compressed size: {round(size_mb,2)}MB | md5: {mymd5.md5_bytes(data)}")

        size_mb = sys.getsizeof(decompressed_data)/1024/1024
        hash_decompressed = mymd5.md5_bytes(decompressed_data)
        print(f"Decompressed size: {round(size_mb,2)}MB | md5: {hash_decompressed}")

        return hash_decompressed

if __name__ == '__main__':
    filesrc_original = "data.csv"
    filesrc_compressed = "compressed_data.csv"
    print('compressing...')
    hash_orignal = compressing(filesrc_original, filesrc_compressed)
    print('decompressing...')
    hash_decompressed = decompress(filesrc_compressed)

    print(f'hashs match: {hash_orignal == hash_decompressed}')


