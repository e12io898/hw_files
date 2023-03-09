buffer = {}

for i in range(3):
    file_name = f'{i + 1}.txt'
    with open(file_name, encoding='utf-8') as f:
        buffer[file_name] = f.readlines()

sort_buffer = sorted((buffer.items()), key=lambda x: len(x[1]))

with open('sorted.txt', 'a', encoding='utf-8') as text:
    for f_name, f_text in sort_buffer:
        text.write(f'{f_name}\n')
        text.write(f'{str(len(f_text))}\n')
        for line in f_text:
            text.write(line)
        text.write('\n')