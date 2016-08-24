# -*- coding: utf-8 -*-

import unittest
from os import path

import rosettxta


sample_dir = path.dirname(path.realpath(__file__)) + "/samples"


class TestRosettxta(unittest.TestCase):
    tests = [
        ('en',
         'eng-xx-doctor-who-2005-s02e04.srt',
         'eng-xx-doctor-who-2005-s02e04.en.srt'),
        ('es',
         'spa-es-doctor-who-s01e01.srt',
         'spa-es-doctor-who-s01e01.es.srt')
    ]

    def test_get_language(self):
        for (lang, filename, x) in self.tests:
            got = rosettxta.get_file_language(sample_dir + "/" + filename)

            self.assertEqual(lang, got, filename)

    def test_get_language_aware_filename(self):
        for (x, filename, language_aware_filename) in self.tests:
            expected = sample_dir + "/" + language_aware_filename

            got = rosettxta.get_language_aware_filename(
                sample_dir + "/" + filename)

            self.assertEqual(expected, got, filename)

    def test_get_filename_for_language(self):
        # Correct filename
        self.assertEqual(
            rosettxta.get_filename_for_language('foo.en.txt', 'en'),
            'foo.en.txt'
        )

        # Add language ext
        self.assertEqual(
            rosettxta.get_filename_for_language('foo.doc', 'es'),
            'foo.es.doc'
        )

        # Ignore non-lang subextension
        self.assertEqual(
            rosettxta.get_filename_for_language('foo.other.doc', 'br'),
            'foo.other.br.doc'
        )

        # Fix incorrect extension
        self.assertEqual(
            rosettxta.get_filename_for_language('molo.en.md', 'es'),
            'molo.es.md'
        )


if __name__ == '__main__':
    unittest.main()
