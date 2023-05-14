#!/usr/bin/python3
"""Reloads class objects from file.json"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
