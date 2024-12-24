import zipfile

with zipfile.ZipFile('a_file.zip') as z:
    print(f'total files size={sum(e.file_size for e in z.infolist())}')
