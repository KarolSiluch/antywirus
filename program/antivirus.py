from pathlib import Path
import program.errors as errors
from program.fast_scanner import FastScanner, Scanner
import json


class Antivirus:
    def __init__(self, path: Path):
        '''ścieżka do skanowanego folderu'''
        if not path.exists():
            raise FileNotFoundError
        if not path.is_dir():
            raise errors.NotADirError
        self._path = path

    def get_catalog_of_all_files(self):
        '''zrwraca katalog wszystkich plików z wybranego wcześniej folderu'''
        return Scanner().get_files(self._path)

    def fast_scan(self):
        '''podaje informacje o wszystkich nowych lub zmienionych plikach.
        szybkie skanowanie działa na podstawie pliku index.json znajdującego
        się w folderze tego programu'''
        index_path = Path('program/index.json')
        if not index_path.exists():
            self.update_index()
        new_catalog = FastScanner().get_files(self._path, index_path)
        print(new_catalog if new_catalog else '_______No files to scan_______')

    def create_index(self, index_path: Path):
        '''tworzy plik index.json w wybranym folderze'''
        data = {}
        for path, file in self.get_catalog_of_all_files():
            data[path] = file.json()
        index_path /= 'index.json'
        with index_path.open('w') as f:
            json.dump(data, f)

    def update_index(self):
        '''tworzy plik index.json w folderze programu'''
        self.create_index(Path('./program'))

    def scan(self):
        '''wypisuje informacje o wszystkich plikach wybranym folderze'''
        print(self.get_catalog_of_all_files())

    def repair_catalog(self):
        '''pozwala na usunięcie podejrzanych plików'''
        for path, file in self.get_catalog_of_all_files():
            if not file.status:
                continue
            decision = input(f'delete {file.name}? (Y/n): ')
            if not decision.lower() == 'y':
                continue
            file_path = Path(path)
            file_path.unlink()
            print('file has been succesfuly removed')
