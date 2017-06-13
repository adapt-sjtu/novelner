#!/usr/bin/python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-


def split_type(label):
    elems = label.split('-')
    if len(elems) == 2:
        return elems[0], elems[1]  # Example: B-NP: 'B', 'NP'
    elif len(elems) == 1:
        return elems[0], ''  # Example: O (with no type): 'O', ''
    else:
        return '', ''  # Sentence Boundary

inside = False


def convert_to_iobes(from_format, prec, curr, succ):
    global inside
    # preceeding: i.e. before, current i.e. actual, succeeding i.e. following
    prec_tag, prec_type = split_type(prec)
    curr_tag, curr_type = split_type(curr)
    succ_tag, succ_type = split_type(succ)
    if prec_tag == '':  # Reset on sentence start
        inside = False

    # curr_type != prec_type  # Begins some chunk according to the type (including O)
    # curr_type != succ_type  # Ends some chunk according to the type (including O)

    # From valid IOB1:
    # Labels: B, I, O + Types
    # IO + I -> B: when consecutive SAME TYPE chunks and the second is begining
    if from_format == 'IOB1':
        # Single
            # curr_tag == 'B':
            #    Preceeded by SAME TYPE (B or I)
            #    Succeeded by B with SAME TYPE (including Single) or ANY with DIFFERENT TYPE (or O or sentence boundary)
        if ((curr_tag == 'B' and curr_type == prec_type and
            ((succ_tag == 'B' and curr_type == succ_type) or curr_type != succ_type or succ_tag == '')) or
            # curr_tag == 'I':
            #    Preceeded by DIFFERENT TYPE (B or I or sentence boundary)
            #    Succeeded by B with SAME TYPE (including Single) or ANY with DIFFERENT TYPE (or O or sentence boundary)
            (curr_tag == 'I' and curr_type != prec_type and
             ((succ_tag == 'B' and curr_type == succ_type) or curr_type != succ_type or succ_tag == ''))):
            return 'S-{0}'.format(curr_type)

        # Begin of chunk by tag
            # curr_tag == 'B':
            #    Preceeded by SAME TYPE (B or I)
            #    Succeeded by anything... (Pedantic: Only by I with SAME TYPE else it is Single)
        if ((curr_tag == 'B' and curr_type == prec_type) or
            # curr_tag == 'I':
            #    Preceeded by E, O with DIFFERENT TYPE
            #    Succeeded by anything... (including sentence boundary) (Pedantic: Only by I with SAME TYPE else Single)
                (curr_tag == 'I' and curr_type != prec_type)):
            return 'B-{0}'.format(curr_type)

        # Inside of chunk by tag
            # curr_tag == 'I':
            #    Preceeded by SAME TYPE (B or I)
            #    Succeeded by I with SAME TYPE
        if curr_tag == 'I' and curr_type == prec_type and curr_type == succ_type and succ_tag == 'I':
            return 'I-{0}'.format(curr_type)

        # End of chunk by tag
            # curr_tag == 'I':
            #    Preceeded by SAME TYPE (B or I)
            #    Succeeded by anything... (including sentence boundary)
            #    (Pedantic: Only by B with SAME TYPE or DIFFERENT TYPE else Inside)
        if curr_tag == 'I' and curr_type == prec_type:
            return 'E-{0}'.format(curr_type)
        if curr_tag == 'O':
            return 'O'
        return curr

    # -----------------------------------------------------------------------------------------------------------------

    # From valid IOB2:
    # Labels: B, I, O + Types
    # IO + I -> B: Every begining of ANY TYPE chunk is B
    if from_format == 'IOB2':
        # Single
            # curr_tag == 'B':
            #    Preceeded by anything... (including sentence boundary)
            #    Succeeded by B (anytype) or O or sentence boundary
        if curr_tag == 'B' and succ_tag in {'B', 'O', ''}:
            return 'S-{0}'.format(curr_type)

        # Begin of chunk by tag
            # curr_tag == 'B':
            #    Preceeded by anything... (including sentence boundary)
            #    Succeeded by anything... (Pedantic: Only by I with SAME TYPE else it is Single)
        if curr_tag == 'B':
            return 'B-{0}'.format(curr_type)

        # Inside of chunk by tag
            # curr_tag == 'I':
            #    Preceeded by anything... (Pedantic: Only with SAME TYPE else it is Invalid)
            #    Succeeded by anything... (Pedantic: Only with SAME TYPE else it is Invalid)
        if curr_tag == 'I' and succ_tag == 'I':
            return 'I-{0}'.format(curr_type)

        # End of chunk by tag
            # curr_tag == 'I':
            #    Preceeded by anything... (Pedantic: Only with SAME TYPE else it is Invalid)
            #    Succeeded by B or O or sentence boundary
        if curr_tag == 'I' and succ_tag in {'B', 'O', ''}:
            return 'E-{0}'.format(curr_type)
        if curr_tag == 'O':
            return 'O'
        return curr

    # -----------------------------------------------------------------------------------------------------------------

    # From valid IOE1:
    # Labels: I, E, O + Types
    # IO + I -> E: when consecutive SAME TYPE chunks and the first is ending
    if from_format == 'IOE1':
        # Single
            # curr_tag == 'I':
            #    Preceeded by DIFFERENT TYPE (or O or sentence boundary)
            #    Succeeded by I (or O) with DIFFERENT TYPE (including sentence boundary)
        if ((curr_tag == 'I' and ((prec_tag in {'I', 'O', ''} and curr_type != prec_type) or (prec_tag == 'E' and curr_type == prec_type))
                and succ_tag in {'I', 'O', ''} and curr_type != succ_type) or
            # curr_tag == 'E':
            #    Preceeded by E with SAME TYPE
            #    Succeeded by SAME TYPE (I or E)
                (curr_tag == 'E' and ((prec_tag == 'E' and curr_type == prec_type) or curr_type != prec_type) and curr_type == succ_type)):
            return 'S-{0}'.format(curr_type)

        # Begin of chunk by tag
            # curr_tag == 'I':
            #    Preceeded by E with SAME TYPE or ANY with DIFFERENT TYPE (including sentence boundary)
            #    Succeeded by ANY with SAME TYPE (I or E)
        if (curr_tag == 'I' and ((prec_tag == 'E' and curr_type == prec_type) or curr_type != prec_type) and
                curr_type == succ_type):
            return 'B-{0}'.format(curr_type)

        # Inside of chunk by tag
            # curr_tag == 'I':
            #    Preceeded by I with SAME TYPE
            #    Succeeded by ANY with SAME TYPE (I or E)
        if curr_tag == 'I' and prec_tag == 'I' and curr_type == prec_type and curr_type == succ_type:
            return 'I-{0}'.format(curr_type)

        # End of chunk by tag
            # curr_tag == 'I':
            #    Preceeded by I with SAME TYPE
            #    Succeeded by DIFFERENT TYPE (or O or sentence boundary)
        if ((curr_tag == 'I' and prec_tag == 'I' and curr_type == prec_type and curr_type != succ_type) or
            # curr_tag == 'I':
            #    Preceeded by I with SAME TYPE
            #    Succeeded by I or E with SAME TYPE
                (curr_tag == 'E' and prec_tag == 'I' and curr_type == prec_type and curr_type == succ_type)):
            return 'E-{0}'.format(curr_type)
        if curr_tag == 'O':
            return 'O'
        return curr

    # -----------------------------------------------------------------------------------------------------------------

    # From valid IOE2:
    # Labels: I, E, O + Types
    # IO + I -> E: Every ending of ANY TYPE chunk is B
    if from_format == 'IOE2':
        # Single
            # curr_tag == 'E':
            #    Preceeded by E or O with ANY TYPE or sentence boundary (as every end is marked with E)
            #    Succeeded by anything... (including sentence boundary) (as every end is marked with E)
        if curr_tag == 'E' and prec_tag in {'E', 'O', ''}:
            return 'S-{0}'.format(curr_type)

        # Begin of chunk by tag
            # curr_tag == 'I':
            #    Preceeded by E or O with ANY TYPE or sentence boundary
            #    Succeeded by anything... (as every end is marked with E)
        if curr_tag == 'I' and prec_tag in {'E', 'O', ''}:
            return 'B-{0}'.format(curr_type)

        # Inside of chunk by tag
            # curr_tag == 'I':
            #    Preceeded by I (as every end is marked with E)
            #    Succeeded by ANY TYPE (I or E) (as every end is marked with E)
        if curr_tag == 'I' and prec_tag == 'I' and succ_tag in {'I', 'E'}:
            return 'I-{0}'.format(curr_type)

        # End of chunk by tag
            # curr_tag == 'E':
            #    Preceeded by E with SAME TYPE
            #    Succeeded by ANY TYPE (I or E) (including sentence boundary)
        if curr_tag == 'E' and prec_tag == 'I':
            return 'E-{0}'.format(curr_type)
        if curr_tag == 'O':
            return 'O'
        return curr

    # -----------------------------------------------------------------------------------------------------------------

    # From valid SBIEO or IOBES:
    # Labels: S, B, I, E, O + Types
    # IO + B for begin S for single E for end of ANY TYPE chunk
    if from_format in {'IOBES', 'SBIEO'}:
        # Single chunk by tag
            # curr_tag == 'S':
            #    Preceeded by E or O with ANY TYPE or sentence boundary
            #    Succeeded by B or O with ANY TYPE or sentence boundary
        if curr_tag == 'S' and prec_tag in {'E', 'O', 'S', ''} and succ_tag in {'B', 'O', 'S', ''}:
            return 'S-{0}'.format(curr_type)

        # Begin of chunk by tag
            # curr_tag == 'B':
            #    Preceeded by E or O with ANY TYPE or sentence boundary
            #    Succeeded by I or E with SAME TYPE
        if curr_tag == 'B' and prec_tag in {'E', 'O', 'S', ''} and succ_tag in {'I', 'E'} and curr_type == succ_type:
            return 'B-{0}'.format(curr_type)

        # Inside of chunk by tag
            # curr_tag == 'I':
            #    Preceeded by B or I with SAME TYPE
            #    Succeeded by I or E with SAME TYPE
        if (curr_tag == 'I' and prec_tag in {'B', 'I'} and curr_type == prec_type and succ_tag in {'I', 'E'} and
                curr_type == succ_type):
            return 'I-{0}'.format(curr_type)

        # End of chunk by tag
            # curr_tag == 'E':
            #    Preceeded by B or I with SAME TYPE
            #    Succeeded by B or O with ANY TYPE or sentence boundary
        if curr_tag == 'E' and prec_tag in {'B', 'I'} and curr_type == prec_type and succ_tag in {'B', 'O', 'S', ''}:
            return 'E-{0}'.format(curr_type)
        if curr_tag == 'O':
            return 'O'
        return '{0}-{1} Invalid'.format(curr_tag, curr_type)

    # -----------------------------------------------------------------------------------------------------------------

    # From valid O+C:
    # Labels: S, B, E, O + Types
    # IO + I -> O, B for begin S for single E for end of ANY TYPE chunk
    if from_format == 'O+C':
        # Single chunk by tag
            # curr_tag == 'S':
            #    Preceeded by E or O with ANY TYPE or sentence boundary
            #    Succeeded by B or O with ANY TYPE or sentence boundary
        if curr_tag == 'S' and prec_tag in {'E', 'O', 'S', ''} and succ_tag in {'B', 'O', 'S', ''} and not inside:
            return 'S-{0}'.format(curr_type)

        # Begin of chunk by tag
            # curr_tag == 'B':
            #    Preceeded by E or O with ANY TYPE or sentence boundary
            #    Succeeded by E with SAME TYPE (or O)
        if (curr_tag == 'B' and prec_tag in {'E', 'O', 'S', ''} and ((succ_tag == 'E' and curr_type == succ_type) or
                succ_tag == 'O') and not inside):
            inside = True
            return 'B-{0}'.format(curr_type)

        # Inside of chunk by tag
            # curr_tag == 'O':
            #    Preceeded by B with SAME TYPE (or O)
            #    Succeeded by E with SAME TYPE (or O)
        if (curr_tag == 'O' and ((prec_tag == 'B' and curr_type == prec_type) or prec_tag == 'O') and ((succ_tag == 'E' and
                curr_type == succ_type) or succ_tag == 'O') and inside):
            return 'I-{0}'.format(curr_type)

        # End of chunk by tag
            # curr_tag == 'E':
            #    Preceeded by B or I with SAME TYPE
            #    Succeeded by B or O with ANY TYPE or sentence boundary
        if (curr_tag == 'E' and ((prec_tag == 'B' and curr_type == prec_type) or prec_tag == 'O') and
                succ_tag in {'B', 'O', 'S', ''} and inside):
            inside = False
            return 'E-{0}'.format(curr_type)
        if curr_tag == 'O':
            return 'O'
        return curr

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        fh = open(sys.argv[2], encoding='UTF-8')
    elif len(sys.argv) > 1:
        fh = sys.stdin

    else:
        print("usage {0} FORMAT [INPUT]".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)
    iob_format = sys.argv[1]

    l = fh.readline().strip()
    cur = ''
    cur_label = ''
    if len(l) > 0:
        suc = l
        suc_label = l.split()[-1]
    else:
        suc = ''
        suc_label = ''
    for l in fh:
        l = l.strip().split()
        prec_label = cur_label
        cur = suc
        cur_label = suc_label
        suc = l
        if len(l) > 0:
            suc_label = l[-1]
        else:
            suc_label = ''
        if len(cur) > 0:
            print(''.join(cur), convert_to_iobes(iob_format, prec_label, cur_label, suc_label))
        else:
            print()
    if len(suc) > 0:  # Last line not empty!
        prec_label = cur_label
        cur = suc
        cur_label = suc_label
        suc_label = ''
        print(''.join(cur), convert_to_iobes(iob_format, prec_label, cur_label, suc_label))
