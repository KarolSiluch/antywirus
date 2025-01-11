from program.file import File


def test_status_safe():
    file = File('plik.py', 'asfasfas')
    assert file.status is False


def test_status_virus():
    file = File('plik.py', '44d88612fea8a8f36de82e1278abb02f')
    assert file.status is True


def test_status_json():
    file = File('Turcja.txt', 'Kebab')
    assert file.json() == {'name': 'Turcja.txt', 'status': False, 'hash': 'Kebab'}


def test_str():
    file = File('święta.txt', '44d88612fea8a8f36de82e1278abb02f')
    text = 'name: święta.txt\nstatus: Suspicious File!!\nhash: 44d88612fea8a8f36de82e1278abb02f'
    assert str(file) == text
