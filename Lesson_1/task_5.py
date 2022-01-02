"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import chardet
import subprocess

sites = ["yandex.ru", "youtube.com"]


def ping_func(site_for_ping):
    for line in subprocess.Popen(["ping", site_for_ping], stdout=subprocess.PIPE).stdout:
        result = chardet.detect(line)
        print(result)
        print(line.decode(result['encoding']).encode('utf-8').decode('utf-8'))
    return True


for site in sites:
    print(site.upper())
    ping_func(site)
    print('*' * 70, '\n')
