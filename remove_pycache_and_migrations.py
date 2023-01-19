import os
import shutil


if __name__ == '__main__':
    path = os.getcwd()
    for path, folders, files in os.walk(path):
        for folder in folders:
            if '__pycache__' in folder:
                shutil.rmtree(os.path.join(path, folder))

    print('removed all pycache folders')

    for path, folders, files in os.walk(path):
        for file in files:
            if ('000' in file or '001' in file or '002' in file or '003' in file or '004' in file or '005' in file or
                    '006' in file or '007' in file or '008' in file or '009') and '.py' in file:
                os.remove(os.path.join(path, file))

    print('removed all migrations files')

