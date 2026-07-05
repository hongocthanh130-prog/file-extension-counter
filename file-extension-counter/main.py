from counter import count_extensions

folder = input('Folder path: ')
counts = count_extensions(folder)

print('File extensions:')
for ext, total in counts.items():
    print(f'{ext}: {total}')
