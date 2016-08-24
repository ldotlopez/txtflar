# -*- coding: utf-8 -*-


import argparse
import os
import shutil
from os import path


import rosettxta


if __name__ == '__main__':
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
        filename = path.realpath(fn)
        new_filename = rosettxta.get_language_aware_filename(filename)

        if filename == new_filename:
            msg = "# I: '{filename}' is already correct"
            msg = msg.format(filename=fn)
            print(msg)
            continue

        if args.dry_run:
            msg = "mv '{old} '{new}'"
            msg = msg.format(old=fn, new=new_filename)
            print(msg)
            continue

        if path.exists(new_filename):
            if not args.force:
                msg = "# E: '{new}' already exists"
                msg = msg.format(new=new_filename)
                print(msg)
                continue
            else:
                os.unlink(new_filename)

        shutil.move(fn, new_filename)
