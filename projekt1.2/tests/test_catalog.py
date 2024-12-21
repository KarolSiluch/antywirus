from program.file import File
from program.catalog import Catalog
from pytest import raises


def test_bool():
    catalog = Catalog('katalog')
    assert bool(catalog) is False
    catalog.add_file(File('FortniteBattlepass.com', '1+1=3'))
    assert bool(catalog) is True


def test_add_file():
    catalog = Catalog('katalog')
    assert len(catalog) == 0
    test = File('KFC.com', 'ಥ_ಥ')
    catalog.add_file(test)
    assert len(catalog) == 1
    catalog.add_file(File('بحان الله، سبحان الله', 'لا يمكنك تجاوز مرساة أو مسار فارغ'))
    assert len(catalog) == 2


def test_files():
    catalog = Catalog('Warszawa')
    file1 = File('way_to_answer', '何を信じて生きる')
    catalog.add_file(file1)
    file2 = File('piwo.piwo', 'piwo tesco')
    catalog.add_file(file2)
    assert catalog.files['Warszawa/way_to_answer'] == file1
    assert catalog.files['Warszawa/piwo.piwo'] == file2
    with raises(KeyError):
        catalog.files['szczupak król wód']


def test_str():
    catalog = Catalog('styrta')
    assert str(catalog) == 'catalog is emty'
    file1 = File('pali', '1111-2222')
    catalog.add_file(file1, 'styrta/się')
    text1 = 'name: pali\nstatus: Safe\nhash: 1111-2222\nfull_path: styrta/się/pali'
    assert str(catalog) == text1
    file2 = File('dopala', '2222-3333')
    catalog.add_file(file2, 'styrta/się/już')
    text2 = 'name: dopala\nstatus: Safe\nhash: 2222-3333\nfull_path: styrta/się/już/dopala'
    assert str(catalog) == f'{text1}\n\n{text2}'
