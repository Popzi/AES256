from sbox import sbox
from sboxInv import sboxInv

def subBytes(block):
    sublist = []
    for c in block:
       sublist.append(sbox[c])
    return sublist

def subBytesInv(block):
    unsublist = []
    for c in block:
       unsublist.append(sboxInv[c])
    return unsublist