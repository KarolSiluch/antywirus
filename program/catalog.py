from program.file import File


class Catalog:
    def __init__(self, name: str, files: dict[str, File] | None = None):
        self._name = name
        self._files = files if files else {}

    @property
    def files(self):
        return self._files

    def add_file(self, file: File, parent_catalog: str | None = None):
        '''dodawanie plików do katalogu na podstawie ścieżki'''
        key = parent_catalog if parent_catalog else self._name
        key = f'{key}/{file.name}'
        self._files[key] = file

    def __bool__(self):
        return bool(self._files.values())

    def __iter__(self):
        return iter(self._files.items())

    def __len__(self):
        return len(self._files.values())

    def __str__(self):
        files_description = []
        if not self:
            return 'catalog is emty'
        for path, file in self._files.items():
            path_str = f'\nfull_path: {path}'
            files_description.append(str(file) + path_str)
        return '\n\n'.join(files_description)
