# -*- coding: utf-8 -*-


from os import path


import babelfish
import chardet
import langdetect


class DetectError(Exception):
    pass


def get_language(buff):
    # Try with utf-8
    try:
        return langdetect.detect(buff.decode('utf-8'))
    except UnicodeError:
        pass

    # Try guessing
    guess = chardet.detect(buff)
    if not guess:
        raise DetectError('Unknow encoding')

    return langdetect.detect(buff.decode(guess['encoding']))


def get_file_language(filepath):
    with open(filepath, 'rb') as stream:
        ret = get_language(stream.read())

    return ret


def get_filename_for_language(filepath, language):
    name, ext = path.splitext(filepath)
    name_without_langext, langext = path.splitext(name)

    try:
        babelfish.Language.fromalpha2(langext[1:])
        name = name_without_langext
    except (IndexError, babelfish.LanguageReverseError):
        pass

    return name + "." + language + ext


def get_language_aware_filename(filepath):
    return get_filename_for_language(
        filepath,
        get_file_language(filepath)
    )
