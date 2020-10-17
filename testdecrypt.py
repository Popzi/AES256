import AES256
from readBlockFile import getBlock
from readKeyFile import getKey

key = getKey("testKey")
block = getBlock("testBlock")
print(block)
encryptedBlock = AES256.encrypt(block,key)
print(encryptedBlock)
decryptedBlock = AES256.decrypt(encryptedBlock,key)
print(decryptedBlock)