from pathlib import Path
import json


class File:
    def __init__(self, name: str, hash: str):
        self._name = name
        self._hash = hash
        self._status = self.scan()

    @property
    def name(self):
        return self._name

    @property
    def hash(self):
        return self._hash

    @property
    def status(self):
        return self._status

    def scan(self):
        '''True -> virus    False -> not a virus'''
        with Path('program/virus_database.json').open() as file:
            viruses = json.load(file)
            return True if self._hash in viruses else False

    def json(self):
        return {
            'name': self._name,
            'status': self._status,
            'hash': self._hash}

    def __str__(self):
        file_data = self.json()
        file_data['status'] = 'Suspicious File!!' if file_data['status'] else 'Safe'
        text = '\n'.join(f'{title}: {content}' for title, content in file_data.items())
        return text
