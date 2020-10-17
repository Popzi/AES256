# mainly implemented by looking at pyAES and Wikipedia example C code
def shiftRows(block):
    rows = []
    for r in range(4):
        rows.append(block[r::4] )
        rows[r] = rows[r][r:] + rows[r][:r]
    block = [r[c] for c in range(4) for r in rows]
    return block

def shiftRowsInv(block):
    rows = []
    for r in range(4):
        rows.append(block[r::4] )
        rows[r] = rows[r][4-r:] + rows[r][:4-r]
    block = [r[c] for c in range(4) for r in rows]
    return block