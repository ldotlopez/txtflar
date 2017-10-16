# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Luis López <luis@cuarentaydos.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
# USA.


from .txtflar import (
    DetectError,
    EncodingDetectError,
    LanguageDetectError,
    get_file_language,
    get_filename_for_language,
    get_language,
    get_language_aware_filename
)

version = [0, 0, 0, 20171016, 2]

__all__ = [
    'DetectError',
    'EncodingDetectError',
    'LanguageDetectError',
    'get_file_language',
    'get_language_aware_filename',
    'get_language',
    'get_filename_for_language',
    'version'
]
