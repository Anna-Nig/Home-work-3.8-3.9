# worker.py
import zipfile

def process_file(file1_path, zip1_path, zip2_path):  # ← 3 АРГУМЕНТА ОТДЕЛЬНО!
    """
    СТРОГО pool.starmap(): распаковывает (file1_path, zip1_path, zip2_path)
    """
    try:
        # 1. Читаем путь из path_8_8.zip
        with zipfile.ZipFile(zip1_path, 'r') as zip1:
            target_path = zip1.read(file1_path).decode('utf-8').strip()
        
        # 2. Читаем число из recursive_challenge_8_8.zip
        with zipfile.ZipFile(zip2_path, 'r') as zip2:
            number_str = zip2.read(target_path).decode('utf-8').strip()
        
        return int(number_str)
    except Exception as e:
        print(f"Ошибка {file1_path}: {e}")
        return 0