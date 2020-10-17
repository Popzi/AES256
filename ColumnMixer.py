from copy import copy

# This entire implementation is also from pyAES, no idea to re-invent the wheel here either
def gmul(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11b
        b >>= 1
    return p % 256

def mixColumn(col):
    tempcol = copy(col)
    col[0] = gmul(tempcol[0],2) ^ gmul(tempcol[3],1) ^ \
                gmul(tempcol[2],1) ^ gmul(tempcol[1],3)
    col[1] = gmul(tempcol[1],2) ^ gmul(tempcol[0],1) ^ \
                gmul(tempcol[3],1) ^ gmul(tempcol[2],3)
    col[2] = gmul(tempcol[2],2) ^ gmul(tempcol[1],1) ^ \
                gmul(tempcol[0],1) ^ gmul(tempcol[3],3)
    col[3] = gmul(tempcol[3],2) ^ gmul(tempcol[2],1) ^ \
                gmul(tempcol[1],1) ^ gmul(tempcol[0],3)
    return col

def mixColumnInv(col):
    tempcol = copy(col)
    col[0] = gmul(tempcol[0],14) ^ gmul(tempcol[3],9) ^ \
                gmul(tempcol[2],13) ^ gmul(tempcol[1],11)
    col[1] = gmul(tempcol[1],14) ^ gmul(tempcol[0],9) ^ \
                gmul(tempcol[3],13) ^ gmul(tempcol[2],11)
    col[2] = gmul(tempcol[2],14) ^ gmul(tempcol[1],9) ^ \
                gmul(tempcol[0],13) ^ gmul(tempcol[3],11)
    col[3] = gmul(tempcol[3],14) ^ gmul(tempcol[2],9) ^ \
                gmul(tempcol[1],13) ^ gmul(tempcol[0],11)
    return col

# this is partly from pyAES and stackoverflow for the list map list zip iter
def mixColumns(block):
    columns = list(map(list,zip(*([iter(block)] * 4))))
    mixed = []
    for i in range(len(columns)):
        col = mixColumn(columns[i])
        for j in range(len(col)):
            mixed.append(col[j])
    return mixed

def mixColumnsInv(block):
    columns = list(map(list,zip(*([iter(block)] * 4))))
    unmixed = []
    for i in range(len(columns)):
        col = mixColumnInv(columns[i])
        for j in range(len(col)):
            unmixed.append(col[j])
    return unmixed