buffer = {}

for i in range(3):
    file_name = f'{i + 1}.txt'
    with open(file_name, encoding='utf-8') as f:
        buffer[file_name] = f.readlines()

sort_buffer = sorted((buffer.items()), key=lambda x: len(x[1]))

with open('sorted.txt', 'a', encoding='utf-8') as text:
    for key, i in sort_buffer:
        text.write(f'{key}\n')
        text.write(f'{str(len(i))}\n')
        for _ in i:
            text.write(_)
        text.write(f'\n')