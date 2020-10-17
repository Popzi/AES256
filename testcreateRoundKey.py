from keyManager import expandKey,createRoundKey
from readKeyFile import getKey

key = getKey("testKey")
expandedKey = expandKey(key)

roundkey0 = createRoundKey(expandedKey, 0)
roundkey7 = createRoundKey(expandedKey, 7)
roundkey14 = createRoundKey(expandedKey, 14)

print("Expandedkey:",expandedKey)
print("roundkey0",roundkey0)
print("roundkey7",roundkey7)
print("roundkey14",roundkey14)