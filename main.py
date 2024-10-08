import os
import random
import string

# Параметры
folder_name = "files"
file_count = 20
file_size = 15 * 1024 * 1024  # Размер файла 15 МБ в байтах
chunk_size = 1024 * 1024  # Размер куска, чтобы не записывать всё сразу (для экономии памяти)

# Создание папки
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Функция для генерации случайных строк
def generate_random_string(size):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=size))

# Создание файлов
for i in range(1, file_count + 1):
    file_path = os.path.join(folder_name, f'file_{i}.txt')
    
    with open(file_path, 'w') as f:
        written_size = 0
        while written_size < file_size:
            # Генерация строки длиной равной chunk_size или оставшемуся размеру файла
            chunk = generate_random_string(min(chunk_size, file_size - written_size))
            f.write(chunk)
            written_size += len(chunk)
    
    print(f"Создан файл {file_path}, размером {file_size / (1024 * 1024)} MB")

print(f"Все файлы созданы в папке '{folder_name}'.")

