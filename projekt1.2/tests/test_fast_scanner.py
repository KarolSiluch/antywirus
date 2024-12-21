from program.fast_scanner import FastScanner
from pathlib import Path


def test_get_files():
    path = Path('./tests/test_files/test_catalog1')
    index = Path('./tests/test_files/index.json')
    file = Path('./tests/test_files/test_catalog1/plik1.txt')
    scanner = FastScanner()
    assert len(scanner.get_files(path, index)) == 0
    file = file.rename('./tests/test_files/test_catalog1/jeż.txt')
    assert len(scanner.get_files(path, index)) == 1
    file = file.rename('./tests/test_files/test_catalog1/plik1.txt')


def test_new_file():
    index = {"działka/jeż.txt": {"name": "jeż.txt", "status": False, "hash": "do kąd nocą tupta jeż"}}
    scanner = FastScanner()
    assert scanner.new_edited_file(index, "do kąd nocą tupta jeż", "działka/jeż.txt") is False
    assert scanner.new_edited_file(index, "mięsny jeż", "działka/gniazdo/jeże.txt") is True
    index["działka/gniazdo/jeże.txt"] = {"name": "jeże.txt", "status": False, "hash": "mięsny jeż"}
    assert scanner.new_edited_file(index, "mięsny jeż", "działka/gniazdo/jeże.txt") is False
