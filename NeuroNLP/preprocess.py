import sys
filename = sys.argv[1]
count = 1
for line in open(filename).readlines():
    if len(line) > 1:
        print str(count)+'\t' + line.rstrip()
    else:
        count = 1
        print ''
