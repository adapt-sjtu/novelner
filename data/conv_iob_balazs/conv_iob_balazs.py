#!/usr/bin/python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

import sys
sys.dont_write_bytecode = True

from toIOB1 import convert_to_iob1
from toIOB2 import convert_to_iob2
from toIOE1 import convert_to_ioe1
from toIOE2 import convert_to_ioe2
from toIOBES import convert_to_iobes
from toOC import convert_to_oc


toFormat = {'IOB1': convert_to_iob1, 'IOB2': convert_to_iob2, 'IOE1': convert_to_ioe1, 'IOE2': convert_to_ioe2,
            'IOBES': convert_to_iobes, 'O+C': convert_to_oc, 'OC': convert_to_oc}

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 5:
        print('USAGE {0} FROM-FORMAT TO-FORMAT INPUT-FILE OUTPUT-FILE'.format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    if sys.argv[3] == '-':
        FP_in = sys.stdin
    else:
        FP_in = open(sys.argv[3], encoding='UTF-8')
    if sys.argv[4] == '-':
        FP_out = sys.stdout
    else:
        FP_out = open(sys.argv[4], 'w', encoding='UTF-8')
    from_iob_format = sys.argv[1]
    to_iob_format = sys.argv[2]

    if from_iob_format not in toFormat:
        print('INVALID FROM FORMAT: {0}'.format(from_iob_format), file=sys.stderr)
        sys.exit(1)
    if to_iob_format not in toFormat:
        print('INVALID TO FORMAT: {0}'.format(to_iob_format), file=sys.stderr)
        sys.exit(1)

    if from_iob_format == 'OC':
        from_iob_format = 'O+C'

    to_iob_format_fun = toFormat[to_iob_format]
    l = FP_in. readline().strip()
    curr = ''
    curr_label = ''
    if len(l) > 0:
        succ = l.split()[0:-1]
        succ_label = l.split()[-1]
    else:
        succ = ''
        succ_label = ''
    for l in FP_in:
        l = l.strip().split()
        prec_label = curr_label
        curr = succ
        curr_label = succ_label
        succ = l[0:-1]
        if len(l) > 0:
            succ_label = l[-1]
        else:
            succ_label = ''
        if len(curr) > 0:
            print(' '.join(curr), to_iob_format_fun(from_iob_format, prec_label, curr_label, succ_label), file=FP_out)
        else:
            print('', file=FP_out)
    if len(succ) > 0:  # Last line not empty!
        prec_label = curr_label
        curr = succ
        curr_label = succ_label
        succ_label = ''
        print(' '.join(curr), to_iob_format_fun(from_iob_format, prec_label, curr_label, succ_label), file=FP_out)
    else:
        print('', file=FP_out)
