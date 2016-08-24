# -*- coding: utf-8 -*-


from os import path


import babelfish
import langdetect


def get_language(buff):
    return langdetect.detect(buff)


def get_file_language(filepath):
    with open(filepath) as stream:
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
