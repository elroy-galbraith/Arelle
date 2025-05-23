#! /usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Written by Martin v. L�wis <loewis@informatik.hu-berlin.de>

"""Generate binary message catalog from textual translation description.

This program converts a textual Uniforum-style message catalog (.po file) into
a binary GNU catalog (.mo file).  This is essentially the same function as the
GNU msgfmt program, however, it is a simpler implementation.

Usage: msgfmt.py [OPTIONS] filename.po

Options:
    -o file
    --output-file=file
        Specify the output file to write to.  If omitted, output will go to a
        file named filename.mo (based off the input file name).

    -h
    --help
        Print this message and exit.

    -V
    --version
        Display version information and exit.

Example (for russian in arelle, run from this directory)
    python3.5 msgfmt.py -o arelle/locale/ru/LC_MESSAGES/arelle.mo arelle/locale/ru/LC_MESSAGES/ru.po
"""

import sys
import os
import getopt
import struct
import array

__version__ = "1.1"

MESSAGES = {}



def usage(code, msg=''):
    print (__doc__, file=sys.stderr)
    if msg:
        print (msg, file=sys.stderr)
    sys.exit(code)


def add(id, str, fuzzy):
    "Add a non-fuzzy translation to the dictionary."
    global MESSAGES
    if not fuzzy and str:
        MESSAGES[id] = str


def generate():
    "Return the generated output."
    global MESSAGES
    keys = sorted(MESSAGES.keys())
    # the keys are sorted in the .mo file
    #keys.sort()
    offsets = []
    ids = strs = b''
    for id in keys:
        msg = MESSAGES[id].encode("utf-8")
        id = id.encode("utf-8")
        # For each string, we need size and file offset.  Each string is NUL
        # terminated; the NUL does not count into the size.
        offsets.append((len(ids), len(id), len(strs), len(msg)))
        ids += id + b'\0'
        strs += msg + b'\0'
    output = b''
    # The header is 7 32-bit unsigned integers.  We don't use hash tables, so
    # the keys start right after the index tables.
    # translated string.
    keystart = 7*4+16*len(keys)
    # and the values start after the keys
    valuestart = keystart + len(ids)
    koffsets = []
    voffsets = []
    # The string table first has the list of keys, then the list of values.
    # Each entry has first the size of the string, then the file offset.
    for o1, l1, o2, l2 in offsets:
        koffsets += [l1, o1+keystart]
        voffsets += [l2, o2+valuestart]
    offsets = koffsets + voffsets
    output = struct.pack("Iiiiiii",
                         0x950412de,       # Magic
                         0,                 # Version
                         len(keys),         # # of entries
                         7*4,               # start of key index
                         7*4+len(keys)*8,   # start of value index
                         0, 0)              # size and offset of hash table
    output += array.array("i", offsets).tostring()
    output += ids
    output += strs
    return output


def make(filename, outfile):
    ID = 1
    STR = 2

    # Compute .mo name from .po name and arguments
    if filename.endswith('.po'):
        infile = filename
    else:
        infile = filename + '.po'
    if outfile is None:
        outfile = os.path.splitext(infile)[0] + '.mo'

    try:
        lines = open(infile, encoding='utf-8').readlines()
    except IOError as msg:
        print (msg, file=sys.stderr)
        sys.exit(1)

    section = None
    fuzzy = 0

    msgid = None
    msgstr = None

    # Parse the catalog
    lno = 0
    for l in lines:
        lno += 1
        # If we get a comment line after a msgstr, this is a new entry
        if l[0] == '#' and section == STR:
            add(msgid, msgstr, fuzzy)
            section = None
            fuzzy = 0
        # Record a fuzzy mark
        if l[:2] == '#,' and 'fuzzy' in l:
            fuzzy = 1
        # Skip comments
        if l[0] == '#':
            continue
        # Now we are in a msgid section, output previous section
        if l.startswith('msgid') and not l.startswith('msgid_plural'):
            if section == STR:
                add(msgid, msgstr, fuzzy)
            section = ID
            l = l[5:]
            msgid = msgstr = ''
            is_plural = False
        # This is a message with plural forms
        elif l.startswith('msgid_plural'):
            if section != ID:
                print ('msgid_plural not preceeded by msgid on %s:%d' %\
                    (infile, lno), file=sys.stderr)
                sys.exit(1)
            l = l[12:]
            msgid += '\0' # separator of singular and plural
            is_plural = True
        # Now we are in a msgstr section
        elif l.startswith('msgstr'):
            section = STR
            if l.startswith('msgstr['):
                if not is_plural:
                    print ('plural without msgid_plural on %s:%d' %\
                        (infile, lno), file=sys.stderr)
                    sys.exit(1)
                l = l.split(']', 1)[1]
                if msgstr:
                    msgstr += '\0' # Separator of the various plural forms
            else:
                if is_plural:
                    print ('indexed msgstr required for plural on  %s:%d' %\
                        (infile, lno), file=sys.stderr)
                    sys.exit(1)
                l = l[6:]
        # Skip empty lines
        l = l.strip()
        if not l:
            continue
        # XXX: Does this always follow Python escape semantics?
        l = eval(l)
        if section == ID:
            msgid += l
        elif section == STR:
            msgstr += l
        else:
            print ('Syntax error on %s:%d' % (infile, lno), \
                  'before:', file=sys.stderr)
            print (l, file=sys.stderr)
            sys.exit(1)
    # Add last entry
    if section == STR:
        add(msgid, msgstr, fuzzy)

    # Compute output
    output = generate()

    try:
        open(outfile,"wb").write(output)
    except IOError as msg:
        print (msg, file=sys.stderr)



def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hVo:',
                                   ['help', 'version', 'output-file='])
    except getopt.error as msg:
        usage(1, msg)

    outfile = None
    # parse options
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage(0)
        elif opt in ('-V', '--version'):
            print ("msgfmt.py", __version__, file=sys.stderr)
            sys.exit(0)
        elif opt in ('-o', '--output-file'):
            outfile = arg
    # do it
    if not args:
        print ('No input file given', file=sys.stderr)
        print ("Try `msgfmt --help' for more information.", file=sys.stderr)
        return

    for filename in args:
        make(filename, outfile)


if __name__ == '__main__':
    main()
