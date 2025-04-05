def merge_files(file_names, result_file):
    # Список для хранения кортежей: (имя файла, количество строк, список строк)
    files_data = []
    
    # Читаем каждый файл и сохраняем его данные
    for file in file_names:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            files_data.append((file, line_count, lines))
    
    # Сортируем файлы по количеству строк (от меньшего к большему)
    files_data.sort(key=lambda item: item[1])
    
    # Записываем итоговый файл
    with open(result_file, 'w', encoding='utf-8') as out:
        for file_name, count, lines in files_data:
            # Записываем служебную информацию: имя файла и количество строк
            out.write(f"{file_name}\n")
            out.write(f"{count}\n")
            # Записываем содержимое файла
            out.writelines(lines)
            # Можно добавить дополнительный перевод строки для разделения файлов (опционально)
            out.write("\n")

if __name__ == "__main__":
    # Предполагаем, что имена файлов известны заранее
    files = ["1.txt", "2.txt", "3.txt"]  # Замените на реальные имена файлов
    merge_files(files, "result.txt")
