import sys
f = open(sys.argv[1],'r')
txt = f.read()
txt = txt.replace('creative-work','creativework')
print txt

