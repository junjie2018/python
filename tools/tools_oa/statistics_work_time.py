with open('input.txt', encoding='utf-8') as file:
    time = 0.0
    for line in file.readlines():
        segments = line.split('\t')
        time += float(segments[4][:-1])

    print('overtime:', time)
