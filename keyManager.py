from sbox import sbox
from rcon import rcon

def rotate(word):
    return word[1:] + word[:1]

def keyScheduleCore(word, i):
    word = rotate(word)
    nword = []
    for b in word:
        nword.append(sbox[b])
    nword[0] = nword[0]^rcon[i]
    return nword

def createRoundKey(expandKey,n):
    return expandKey[(n*16):(n*16+16)]

def addRoundKey(roundKey, block):
        assert len(block) == 16
        assert len(roundKey) == 16
        for i in range(16):
            block[i] ^= roundKey[i]
        return block
        
def expandKey(key):
    #this is straght up from the Python AES implementation called pyAES, no idea to re-invent the wheel here
    cipherKeySize = len(key)
    assert cipherKeySize == 32
    # container for expanded key
    expandedKey = []
    currentSize = 0
    rconIter = 1
    # temporary list to store 4 bytes at a time
    t = [0,0,0,0]

    # copy the first 32 bytes of the cipher key to the expanded key
    for i in range(cipherKeySize):
        expandedKey.append(key[i])
    currentSize += cipherKeySize

    # generate the remaining bytes until we get a total key size
    # of 240 bytes
    while currentSize < 240:
        # assign previous 4 bytes to the temporary storage t
        for i in range(4):
            t[i] = expandedKey[(currentSize - 4) + i]

        # every 32 bytes apply the core schedule to t
        if currentSize % cipherKeySize == 0:
            t = keyScheduleCore(t, rconIter)
            rconIter += 1

        # since we're using a 256-bit key -> add an extra sbox transform
        if currentSize % cipherKeySize == 16:
            for i in range(4):
                t[i] = sbox[t[i]]

        # XOR t with the 4-byte block [16,24,32] bytes before the end of the
        # current expanded key.  These 4 bytes become the next bytes in the
        # expanded key
        for i in range(4):
            expandedKey.append(((expandedKey[currentSize - cipherKeySize]) ^ (t[i])))
            currentSize += 1
            
    return expandedKey