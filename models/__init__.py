#!/usr/bin/python3
"""__init__"""

from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
