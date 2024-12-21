import hashlib
from pathlib import Path
import json


def get_hash(file_path: Path):
    '''hashes: md5'''
    with file_path.open(mode='rb') as file:
        digest = hashlib.file_digest(file, 'md5')
        return digest.hexdigest()


def import_json_content(index: Path):
    '''importuje plik json'''
    with index.open() as f:
        return json.load(f)
