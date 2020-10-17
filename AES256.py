from keyManager import createRoundKey,expandKey,addRoundKey
from ColumnMixer import mixColumns,mixColumnsInv
from rcon import rcon
from RowShifter import shiftRows,shiftRowsInv
from sbox import sbox
from sboxInv import sboxInv
from SubBytes import subBytes,subBytesInv
from functools import partial

def pad(blocklist):
    blocklist += [0] * (16 - len(blocklist))
    return blocklist

def split_blocks(message, block_size=16):
    # From https://github.com/boppreh/aes/blob/master/aes.py
    if len(message) < 16:
        message = message + '0' * (16 - len(message))
    return [message[i:i+16] for i in range(0, len(message), block_size)]

def encrypt(block,key):
    encryptedblock = []
    for cblock in split_blocks(block):
        encryptedblock.extend(encrypter(cblock,key))
    return encryptedblock

def encrypter(block,key):
    if len(block) < 16:
        block = pad(block)
    rounds = 14
    expandedkey = expandKey(key)
    roundkey = createRoundKey(expandedkey, 0)
    block = addRoundKey(block, roundkey)
    for i in range(1, rounds):
        roundKey = createRoundKey(expandedkey, i)
        block = subBytes(block)
        block = shiftRows(block)
        block = mixColumns(block)
        block = addRoundKey(block,roundKey)
    # 14th round, no mixcolumns
    roundKey = createRoundKey(expandedkey, rounds)
    block = subBytes(block)
    block = shiftRows(block)
    block = addRoundKey(block, roundKey)
    return block

def decrypt(block,key):
    decryptedblock = []
    for cblock in split_blocks(block):
        decryptedblock.extend(decrypter(cblock,key))
    return decryptedblock

def decrypter(block,key):
    rounds = 14
    expandedkey = expandKey(key)
    roundKey = createRoundKey(expandedkey, rounds)
    block = addRoundKey(block, roundKey)
    block = shiftRowsInv(block)
    block = subBytesInv(block)

    for i in range(rounds-1,0,-1):
        roundKey = createRoundKey(expandedkey, i)
        block = addRoundKey(block,roundKey)
        block = mixColumnsInv(block)
        block = shiftRowsInv(block)
        block = subBytesInv(block)       
 
    # 14th round or round 0
    roundkey = createRoundKey(expandedkey, 0)
    block = addRoundKey(block, roundkey)

    return block