#!/usr/bin/python3
from .engine.file_storage import FileStorage  # use relative import


storage = FileStorage()
storage.reload()
