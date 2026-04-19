import zipfile

def process_file(args):
    """pool.starmap()"""
    file1_path, zip1_path, zip2_path = args
    
    try:
        # 1. Читаем путь из path_8_8.zip
        with zipfile.ZipFile(zip1_path, 'r') as zip1:
            target_path = zip1.read(file1_path).decode('utf-8').strip()
        
        # 2. Читаем число из recursive_challenge_8_8.zip
        with zipfile.ZipFile(zip2_path, 'r') as zip2:
            number_str = zip2.read(target_path).decode('utf-8').strip()
        
        return int(number_str)
    except:
        return 0