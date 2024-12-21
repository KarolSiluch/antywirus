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
        status = self._hash in {'44d88612fea8a8f36de82e1278abb02f'}
        return status

    def json(self):
        return {
            'name': self._name,
            'status': self._status,
            'hash': self._hash}

    def __str__(self):
        file = self.json()
        file['status'] = 'Indian technical support!!' if file['status'] else 'Safe'
        text = '\n'.join(f'{title}: {content}' for title, content in file.items())
        return text
