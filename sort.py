import sys
from pathlib import Path
from normalize import normalize
# словник з розширеннями файлів, що оброблюються
DICT_FOR_EXT = {'archives': ['ZIP', 'GZ', 'TAR'],
                  'video': ['AVI', 'MP4', 'MOV', 'MKV'],
                  'audio': ['MP3', 'OGG', 'WAV', 'AMR'],
                  'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
                  'images': ['JPEG', 'PNG', 'JPG', 'SVG']}

files_dict = DICT_FOR_EXT.copy()
path = Path('D:/Crap')
archives = DICT_FOR_EXT.get ('archives')
video = DICT_FOR_EXT.get ('video')
audio = DICT_FOR_EXT.get ('audio')
documents = DICT_FOR_EXT.get ('documents')
images = DICT_FOR_EXT.get ('images')
other = all_files = []
suff_used_known = set ()
suff_used_unknown = set()

# функція визначення типу файлу, виходячи зі словника
# визначає по розширенню файлу з крапкою перед ним ".ХХХ"
def filetype (suffix): 
    suffix = suffix.removeprefix ('.')
    for type, suffixes in DICT_FOR_EXT.items():
        for suff in suffixes:
            if suffix.lower() == suff.lower():
                 suff_used_known.add(suffix.upper())
                 return type
    suff_used_unknown.add(suffix.upper())
    return "other"

# функція власне сортування, параметр action - для другого прогону
# з нормалізацією та переміщенням
# перший прогон - тільки для інформації скільки і чого є 
def sorting (path, action = False):
    for file in path.iterdir():
#        print (file)
        if file.is_dir():
            sorting (file)
        else:
#            print (f'{file.name} its {filetype (file.suffix)}')
            all_files.append (filetype (file.suffix))
#            files_dict.update ({filetype (file.suffix), file.name})
    return all_files

# початок роботи програми - пишемо в консоль и виклик функції
if __name__ == '__main__':
    sorting (path)

#функція виводу результатів
    print (f'Вміст папки: {path}')
    print ('|{:^15}|{:^10}|'.format ('Типи файлів', 'Кількість'))
    print ('|{:<15}|{:^10}|'.format ('Зображення', all_files.count('images')))
    print ('|{:<15}|{:^10}|'.format ('Відео', all_files.count('video')))
    print ('|{:<15}|{:^10}|'.format ('Документи', all_files.count('documents')))
    print ('|{:<15}|{:^10}|'.format ('Музика', all_files.count('audio')))
    print ('|{:<15}|{:^10}|'.format ('Архіви', all_files.count('archives')))
    print ('|{:<15}|{:^10}|'.format ('Інші типи', all_files.count('other')))
    print ('')
    print (f'Знайдено наступні відомі типи файлів: {suff_used_known}')
    print (f'Знайдено наступні невідомі типи файлів: {suff_used_unknown}')
    print ('')
    yn = input ('Продовжити виконання завдання: перейменування файлів за \
допомогою транслітерації та їх переміщення у папки за типами \
(y - yes / n - no): ')
    while True:
        if yn not in 'yn':
            yn = input("Будь ласка, введіть 'y' або 'n': ") 
        else: break
    if yn == 'n':
        print ('Дякую за увагу!')
        print (normalize('Дякую за увагу! К:и%р;и!л№о123Kiriloc?'))
    else:
        sorting (path)