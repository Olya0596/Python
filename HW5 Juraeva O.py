import os
import re

# функция, возвращающая максимальную глубину папки
def max_depth():
    depth = 0
    for dirpath in dir_paths():
        depth.append(dirpath.count(str(os.sep)))
    return max_depth


# функция, которая считает папки с кириллическими названиями
def cyrillic_names():
    counter = 0
    for i in os.walk():
        for dir_name in i[1]:
            if re.match(r'^[А-ЯЁа-яё]+(\s?([А-ЯЁа-яё]+)?)*$', dir_name):
                counter += 1
    return cyrillic_names


#функция считает файлы с более частотным расширением
def max_extension():
    extensions = []
    for fl in file_names():
        fl, file_extension = os.path.splitext(fl)
        if file_extension.startswith('.'):
            extensions.append(file_extension)
    max_extension = ''
    for i in extensions:
        if extensions.count(i) == max_count(extensions):
            max_extension = i
    return max_extension

#функция, которая возвращает самую частотную первую букву в названиях папок
def fist_letter():
    first_letters = []
    for root, dirs, files in os.walk('.'):
        for directory in dirs:
            first_letters.append(directory[0])
    for i in first_letters:
        if first_letters.count(i) == max_count(first_letters):
            return first_letter
        
#функция, которая возвращает информацию о количестве файлов в папке
def max_files():
    max_len = 0
    dirname = ''
    for i in os.walk():
        if len(i[2]) > max_len:
            max_len = len(i[2])
            dirname = i[0][i[0].rindex(os.sep)+1:]
    return max_files



#функция записывает результат в файл
def main():
   f = open('filename.txt', 'w+')
   path = os.path.dirname(file_name)
   f.write('Максимальная глубина ' + str(get_max_depth(path)) + '\n')
   f.write('Папки с полностью кириллическими названиями' + str(get_number_of_cyrillic_names(path)) + '\n')
   f.write('Количество файлов с частотным расширением' + get_most_common_extension(path) + '\n')
   f.write('Частотная первая буква в названиях\'%s\'' % get_most_common_first_letter(path) + '\n')
   f.write('Разных названий файлов (без учёта расширений)' + str(get_number_of_dif_filenames(path)) + '\n')
   f.write('Несколько файлов с одним и тем же расширением втречается в %s папках ' % get_number_of_dirs(path) + '\n')
   f.write('Больше всего файлов в папке \'%s\'' % get_dir_with_max_number_of_files(path) + '\n')
   f.close()

if __name__ == '__main__':
   main()
        