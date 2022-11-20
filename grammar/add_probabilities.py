import json

def convert_cnt_to_probability(cnt):
    result = {}
    for key, value in cnt:
        total = 0
        for x, y in value:
            total += y
        result[key] = {}
        for x, y in value:
            result[key][x] = y / total
    return result

with open('counter.json', 'r+') as f:
    cnt = json.load(f)

probabilities = convert_cnt_to_probability(cnt)
print(probabilities)

with open('grammar.tribble', 'r') as f:
    with open('probabilities_grammar.tribble', 'r') as out:
        for i in f.readlines():
            if i.find(' | ') == -1:
                out.write(i[:-1] + ' @@ 1.0;\n')
            else:
                tag = i.split(' =')[0].lower()
                if tag == 'template':
                    pass
                else:
                    a = i.split(' | ')
                    idx = 0
                    for _, value in probabilities[tag]:
