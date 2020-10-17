from keyManager import expandKey,createRoundKey,addRoundKey
from readKeyFile import getKey
from readBlockFile import getBlock

key = getKey("testKey")
testBlock = getBlock("testBlock")

expandedKey = expandKey(key)
roundKey0 = createRoundKey(expandedKey, 0)

addedRoundKeyToBlock = addRoundKey(testBlock, roundKey0)
print(addedRoundKeyToBlock)