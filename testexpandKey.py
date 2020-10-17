from keyManager import expandKey
from readKeyFile import getKey

key = getKey("testKey")
print(key)
expandedKey = expandKey(key)
print(expandedKey)