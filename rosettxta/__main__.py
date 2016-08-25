# -*- coding: utf-8 -*-


import argparse
import os
import shutil
import sys
from os import path


import rosettxta


def _escape_filename(filename):
    return filename.replace("\\", "\\\\").replace("'", "\\'")


def main():
    parser = argparse.ArgumentParser(prog='rosettxta', add_help=True)
    parser.add_argument(
        '-n', '--dry-run',
        action='store_true',
        default=False,
        help="Don't rename files, just show whatever will be done"
        )
    parser.add_argument(
        '-f', '--force',
        action='store_true',
        default=False,
        help="Force rename even if destination filename exists"
        )
    parser.add_argument(
        'filenames',
        nargs='+')

    args = parser.parse_args()
    for fn in args.filenames:
        src_fn = path.realpath(fn)
        try:
            dst_fn = rosettxta.get_language_aware_filename(src_fn)
        except rosettxta.DetectError as e:
            msg = "# E: '{filename}' detect error: {msg}"
            msg = msg.format(filename=_escape_filename(fn), msg=str(e))
            print(msg, file=sys.stderr)
            continue

        if src_fn == dst_fn:
            msg = "# I: '{filename}' is already correct"
            msg = msg.format(filename=fn)
            print(msg, file=sys.stderr)
            continue

        if args.dry_run:
            msg = "mv '{src}' '{dst}'"
            msg = msg.format(
                src=_escape_filename(fn), dst=_escape_filename(dst_fn))
            print(msg)
            continue

        if path.exists(dst_fn):
            if not args.force:
                msg = ("# [E] Destination file '{filename}' already exists "
                       "and --force wasn't especified")
                msg = msg.format(new=_escape_filename(dst_fn))
                print(msg, file=sys.stderr)
                continue

            try:
                os.unlink(dst_fn)
            except OSError as e:
                msg = ("# [E] Unable to remove previous destination file "
                       "'{filename}': {msg}")
                msg = msg.format(filename=_escape_filename(fn), msg=str(e))
                print(msg, file=sys.stderr)
                continue

        shutil.move(fn, dst_fn)


if __name__ == '__main__':
    main()
