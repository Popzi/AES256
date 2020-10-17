import AES256
import time
from readBlockFile import getBlock, getNumberofBlocks
from readKeyFile import getKey

# LOAD KEY
key = getKey("testKey")

# READ FILE
blockstart = time.time()
block = getBlock("tWotW.txt")
blockend = time.time()

# ENCRYPT
encryptstart = time.time()
encryptedBlock = AES256.encrypt(block,key)
encryptend = time.time()

# DECRYPT
decryptstart = time.time()
decryptedBlock = AES256.decrypt(encryptedBlock,key)
#readfileblock = getBlock("encoded")
#decryptedBlock = AES256.decrypt(readfileblock,key)
decryptend = time.time()

### Get number of blocks
print("Number of blocks: ",getNumberofBlocks())
print("Readblock time: ", blockend - blockstart,"s")
print("Encryption time: ", encryptend - encryptstart,"s")
print("Decryption time: ", decryptend - decryptstart,"s")
### WRITE TO FILES
print("Encoding and trying to write file.")
encryptedtext = bytearray(encryptedBlock)
encryptedfile = open("encoded", "wb")
encryptedfile.write(encryptedtext)

print("Decoding and writing to file.")
decryptedtext = ''.join(map(chr,decryptedBlock))
decodedfile='decoded.txt' 
with open(decodedfile, 'w', newline='') as dfile:
    try:
        dfile.write(decryptedtext)
    except UnicodeEncodeError:
        print("Error while decoding text. Not writing decoded textfile.")
print("Done.")