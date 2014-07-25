
def inttostr(i):
    return chr((i&0xff000000) >> 24) + chr((i&0x00ff0000) >> 16) +chr((i&0x0000ff00) >> 8) + chr((i&0x000000ff)) 

def hash(*args):
#    hash = 0;
#    for arg in args:
#        sarg = inttostr(arg)
#        for c in sarg:
#            hash = hash ^ ord(c)
    h = 0;
    for arg in args:
        h = h ^ arg
    return h

'''
def inttostr(i):
    return i

def hash(*args):
    hash = 0;
    for arg in args:
        hash = hash ^ arg
    return hash
'''