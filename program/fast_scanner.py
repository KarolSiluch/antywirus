from program.catalog import Catalog
from pathlib import Path
from program.support import get_hash, import_json_content
from program.file import File


class Scanner:
    def get_files(self, catalog_path: Path):
        catalog = Catalog(catalog_path.name)
        for file_path in catalog_path.rglob('*.*'):
            file = File(file_path.name, get_hash(file_path))
            catalog.add_file(file, str(file_path.parent))
        return catalog


class FastScanner:
    def new_edited_file(self, data: dict, hash: str, full_path: str):
        '''sprawdza, czy informacje o pliku znajdują się w indexsie'''
        file_data = data.get(full_path)
        if file_data is None:
            return True
        if not file_data['hash'] == hash:
            return True
        return False

    def get_files(self, catalog_path: Path, index: Path):
        '''zwraca katalog plików, które nie informacje nie znajdowały się w indexie'''
        catalog = Catalog(catalog_path.name)
        data = import_json_content(index)
        for file_path in catalog_path.rglob('*.*'):
            file_hash = get_hash(file_path)
            if not self.new_edited_file(data, file_hash, str(file_path)):
                continue
            new_file = File(file_path.name, file_hash)
            catalog.add_file(new_file, str(file_path.parent))
        return catalog
