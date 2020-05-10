# -*- coding: utf-8 -*-
#
# This file is part of the kif2pgn library.
# Copyright (C) 2013-2020 TANIGUCHI Takaki <takaki@asis.media-as.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import io
import setuptools

setuptools.setup(
    name = 'kif2pgn',
    version = '0.1',
    author = 'TANIGUCHI Takaki',
    author_email = 'takaki@asis.media-as.org',
    description = 'Shogi kifu record converter',
    license = "GPL3",
    keywords = 'shogi csa kif',
    url = 'https://github.com/takaki/kif2pgn',
    scripts = [],
    classifiers = [
      'Intended Audience :: Developers',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Topic :: Games/Entertainment :: Board Games',
      'Topic :: Games/Entertainment :: Turn Based Strategy',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
