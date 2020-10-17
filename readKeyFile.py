import os

def getKey(filename):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) # get os current dir
    with open(os.path.join(__location__, filename), "r") as f: #open file in same dir as read
        key = f.read() # -> 000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
        n = 2 # split after 2
        s = [key[i:i+n] for i in range(0, len(key), n)] # -> ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f']
        splitkey = [int(x, 16) for x in s] # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        return splitkey #returns hex integers