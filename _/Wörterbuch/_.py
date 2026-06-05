import os
import re

def process_files(root_dir):
    """
    Рекурсивно обрабатывает все файлы, преобразуя строки с — в ссылки
    """
    for root, _, files in os.walk(root_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            
            # Пропускаем скрипт и бинарные файлы
            if filename == os.path.basename(__file__) or is_binary_file(filename):
                continue
                
            try:
                process_single_file(filepath)
            except Exception as e:
                print(f"Ошибка при обработке {filepath}: {e}")

def process_single_file(filepath):
    """
    Обрабатывает один файл, заменяя строки с — на ссылки
    """
    # Получаем имя файла без расширения
    filename_without_ext = os.path.splitext(os.path.basename(filepath))[0]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Заменяем строки, начинающиеся с —
    new_content = re.sub(
        r'^(—+)(.*)$',
        lambda m: f'[{m.group(1)}](https://www.verben.de/?w={filename_without_ext})',
        content,
        flags=re.MULTILINE
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Обновлен: {filepath}")

def is_binary_file(filename):
    """
    Проверяет, является ли файл бинарным по расширению
    """
    binary_exts = {'.png', '.jpg', '.jpeg', '.gif', '.pdf', '.zip', '.exe'}
    return os.path.splitext(filename)[1].lower() in binary_exts

if __name__ == "__main__":
    print("=== Преобразование строк с — в ссылки ===")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    process_files(current_dir)
    print("\nГотово! Все файлы обработаны.")