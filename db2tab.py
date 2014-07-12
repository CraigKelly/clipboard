#!/usr/bin/env python
"""db2tab.py

Turns DB-tool formatted data (read from stdin) into a tab-delimited file
(written to stdout)

DB-tool format (our name) looks like this:

Column A Column B Column C
-------- -------- ------------
Row 1    Data A   More Data A
Row 2    Data B   More Data B
Row 3    Data C   More Data C

So it's really a fixed-width format where line 1 contains column names
and line 2 contains the field-widths encoded as equal signs.

This format is used for output by various DB tools, including MS SQL
Server tools (like Query Analyzer) and Oracle SQL Developer
"""

import sys

FLD_SPEC = '-'
LINE_DELIM = '\n'
FLD_DELIM = '\t'

def output(out):
    sys.stdout.write(out + LINE_DELIM)

def output_flds(flds):
    output(FLD_DELIM.join(flds))

def make_parser(fld_widths):
    def parser(s):
        start = 0
        data  = []
        for w in fld_widths:
            data.append(s[start:start+w].strip())
            start += w
            if start >= len(s):
                break
        return data

    return parser

def main():
    line1, line2 = None, None

    for line in sys.stdin:
        inp = line.rstrip()
        if not inp:
            continue

        if not line1:
            line1 = str(inp)
            continue

        elif not line2:
            line2 = str(inp)
            widths = line2.strip().split(' ')
            fldspec = []

            for width in widths:
                tst = width.strip()
                if not tst:
                    continue
                if tst != FLD_SPEC * len(tst):
                    raise "Invalid second line: " + line2
                fldspec.append(len(tst) + 1) #Add one for the extra space

            parser = make_parser(fldspec)
            col_names = parser(line1)
            #for col,wid in zip(col_names, fldspec):
            #    sys.stderr.write("%20s [%20i]\n" % (col,wid))
            output_flds(col_names)

        else:
            output_flds(parser(inp))

if __name__ == "__main__":
    main()
