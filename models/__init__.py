#!/usr/bin/python3
"""Initializing the models directory using the __init__ magic method."""
from models.engine.file_storage import FileStorage

# Creating an instance of FileStorage and reloading it for data retrieval
storage = FileStorage()
storage.reload()
