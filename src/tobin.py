'''

@author: work
'''


while True:
    inputs = raw_input("num: ")
    ss = inputs.split(',')
    outs = []
    for s in ss:
        s = s.strip()
        if not s:
            continue
        n = int(s)
        out = ""
        for i in range (0, 32):
            out = ("1" if n & 0x01 else "0") + out
            n = n >> 1
        print out
 #       outs.append(out)
 #   res = ""
  #  for out in outs:
 #       res += out
  #      res += ", "
  #  print res