import os
import codecs

def is_hex(s):
    try:
        int(s, 16)
    except ValueError:
        return False
    return len(s) % 2 == 0

total_blocks = 0
def getNumberofBlocks():
    return total_blocks

def getBlock(filename):
    returnblock = []
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) # get os current dir
    global total_blocks
    with open(os.path.join(__location__, filename), "rb") as f: #open file in same dir as read
        while True:
            block = f.read(16) #32 -> 00112233445566778899aabbccddeeff
            total_blocks = total_blocks+1
            if not is_hex(block):
                block = codecs.encode(block,'hex') #block.hex()
            if block:
                n = 2 # split after 2
                s = [block[i:i+n] for i in range(0, len(block), n)] # -> ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']
                try:
                    returnblock.extend([int(x, 16) for x in s]) # -> [0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255]
                except ValueError:
                    print('\nValueError in block. Affected block: >>>',block,"<<<. Extending returnblock with this. (no decode).")
                    returnblock.extend(block)
            else:
                break
        return returnblock