from readBlockFile import getBlock
from RowShifter import shiftRows,shiftRowsInv

block = getBlock("testBlock")
shiftedblock = shiftRows(block)
unsshiftedblock = shiftRowsInv(shiftedblock)
print("Shifted: ",shiftedblock)
print("Unshifted: ",unsshiftedblock)