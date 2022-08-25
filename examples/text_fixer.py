PATH = 'txts/audio4.txt'
with open(PATH, 'r') as f:
    res_text = ''
    for line in f:
        if line == '':
            continue
        try:
            cut = line.split('] ', 1)[1]
            cut = cut.rsplit('.  [', 1)[0] + '.'
            if res_text != '' and res_text.endswith('.'):
                res_text += ' '
            res_text += cut
        except Exception as ex:
            continue
print(res_text)

