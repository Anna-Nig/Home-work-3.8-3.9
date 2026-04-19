import zipfile #запускаем в терминале чтение файлов

def process_file(file1_path, zip1_path, zip2_path):
    try:
        with zipfile.ZipFile(zip1_path, 'r') as zip1:
            raw_path = zip1.read(file1_path).decode('utf-8').strip()
        
        target_path = raw_path.replace('\\', '/') #убираем лишнее
        
        with zipfile.ZipFile(zip2_path, 'r') as zip2:
            number_str = zip2.read(target_path).decode('utf-8').strip()
        
        return int(number_str)
    except:
        return 0
