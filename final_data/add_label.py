import sys
f = open(sys.argv[1])
for line in f.readlines():
    if len(line)>5:
        print line.rstrip() +'\tO'
    else:
        print 
