"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""


import yaml

data_to_yaml = {'items': ['bread', 'meat', 'water', 'tomato', 'butter'],
                'items_quantity': 5,
                'items_ptice': {'bread': '2 €',
                                'meat': '5 €',
                                'water': '1 €',
                                'tomato': '2.5 €',
                                'butter': '3 €'}
           }

with open('file.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data_to_yaml, f, default_flow_style=False, allow_unicode=True)

with open("file.yaml", 'r', encoding='utf-8') as f_out:
    data_from_yaml = yaml.load(f_out, Loader=yaml.SafeLoader)

print("Данные совпадают" if data_to_yaml == data_from_yaml else "Данные не совпадают")
