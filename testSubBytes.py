from SubBytes import subBytes,subBytesInv
from readBlockFile import getBlock

testblock = getBlock("testBlock")
print("Testblock:",testblock)
substitutedBlock = subBytes(testblock)
print("Substitutedblock:",substitutedBlock)
unSubstitutedBlock = subBytesInv(substitutedBlock)
print("UnSubstitutedBlock:",unSubstitutedBlock)