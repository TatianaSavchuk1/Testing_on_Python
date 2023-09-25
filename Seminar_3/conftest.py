from checks import checkout
import pytest
import yaml
from datetime import time


with open ('config.yaml') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def make_folders():
    return checkout (f'mkdir -p {data["folderin"]} {data["folderout"]} {data["folderext"]}', '')


@pytest.fixture()
def make_files():
    return checkout (f'cd {data["folderin"]}; touch file1 file2', '')

# Дополнить проект фикстурой, которая после каждого шага теста дописывает в заранее созданный файл stat.txt строку вида:
# время, кол-во файлов из конфига, размер файла из конфига, статистика загрузки процессора из файла /proc/loadavg (можно писать просто всё содержимое этого файла).

@pytest.fixture()
def make_log():
    with open ('stat.txt', 'w', encoding='utf-8') as s:
        s.write(time)

    