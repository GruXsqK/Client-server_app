"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

word_list = ['разработка', 'администрирование', 'protocol', 'standard']
encode_list = [elm.encode("utf-8") for elm in word_list]
decode_list = [elm.decode("utf-8") for elm in encode_list]

for i in range(len(word_list)):
    print(f"word = '{word_list[i]}'\nencode = {encode_list[i]}\ndecode = {decode_list[i]}\n")
