from ColumnMixer import mixColumns,mixColumnsInv
from readBlockFile import getBlock

testblock = getBlock("testBlock")
print("Testblock:",testblock)
mixedBlock = mixColumns(testblock)
print("Mixedblock:",mixedBlock)
unmixedBlock = mixColumnsInv(mixedBlock)
print("Unmixedblock:",unmixedBlock)