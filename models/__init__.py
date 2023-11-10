#!/usr/bin/python3
from .engine.file_storage import FileStorage  # use relative import


storage = FileStorage()
# create a unique FileStorage instance for my application
storage.reload()
