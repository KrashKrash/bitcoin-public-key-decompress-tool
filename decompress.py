#! /usr/bin/env python3

import binascii

p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

def decompress_pubkey(pk):
    x = int.from_bytes(pk[1:33], byteorder='big')
    y_sq = (pow(x, 3, p) + 7) % p
    y = pow(y_sq, (p + 1) // 4, p)
    if y % 2 != pk[0] % 2:
        y = p - y
    y = y.to_bytes(32, byteorder='big')
    return b'\x04' + pk[1:33] + y

print(binascii.hexlify(decompress_pubkey(binascii.unhexlify('0245a6b3f8eeab8e88501a9a25391318dce9bf35e24c377ee82799543606bf5212'))).decode())
print(binascii.hexlify(decompress_pubkey(binascii.unhexlify('0245a6b3f8eeab8e88501a9a25391318dce9bf35e24c377ee82799543606bf5212'))).decode())

