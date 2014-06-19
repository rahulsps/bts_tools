#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

if sys.platform.startswith('linux'):
    class Config:
        BITSHARES_HOME_DIR = '~/.BitSharesXTS'
        BITSHARES_BUILD_DIR = '~/.bitshares_toolkit'
        BITSHARES_BIN_DIR = '~/.BitSharesXTS_bin'

elif sys.platform == 'darwin':
    class Config:
        BITSHARES_HOME_DIR = '~/Library/Application Support/BitShares XTS'
        BITSHARES_BUILD_DIR = '~/.bitshares_toolkit'
        BITSHARES_BIN_DIR = '~/.BitSharesXTS_bin'

elif sys.platform == 'win32':
    raise OSError('Windows platform not supported yet, please submit a patch :)')
    class Config:
        BITSHARES_HOME_DIR = ''
        BITSHARES_BUILD_DIR = ''
        BITSHARES_BIN_DIR = ''

# expand '~' in path names to the user's home dir
for attr in filter(lambda x: not x.startswith('_'), dir(Config)):
    setattr(Config, attr, os.path.expanduser(getattr(Config, attr)))
