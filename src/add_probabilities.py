import json
import re


def convert_cnt_to_probability(cnt):
    result = {}
    for key, value in cnt.items():
        total = 0
        for x, y in value.items():
            total += y
        result[key.lower()] = {}
        for x, y in value.items():
            result[key.lower()][x.lower()] = y / total
    return result


def create_grammar_with_probabilities(counter, grammar, probabilistic_grammar):
    with open(counter, 'r') as f:
        cnt = json.load(f)

    probabilities = convert_cnt_to_probability(cnt)

    with open(grammar, 'r') as f:
        with open(probabilistic_grammar, 'w') as out:
            for i in f.readlines():
                i = i[:-1]
                tag = i.split(' =')[0].lower()

                if tag == 'text':
                    out.write(
                        'Text = Href @@ 0.3| Default @@ 0.2 | Img @@ 0.3 | Style @@ 0.2;\n')
                    continue

                if tag == 'name':
                    out.write('Name = "A" @@ 1.0;\n')
                    continue
                if tag == 'digit' or tag == 'letter':
                    continue

                if i.find(' | ') == -1 or tag not in probabilities:
                    out.write(i[:i.rfind(';')] + ' @@ 1.0;\n')
                else:
                    a = i.split(' | ')
                    new_a = []
                    idx = 0
                    for part in a:
                        if ')' in part and '")"' not in part and (part.find('(') == -1 or part.find(')') < part.find('(')):
                            new_a.append(' | ' + part[:part.find(')')])
                            new_a.append(part[part.find(')'):])
                            idx = 0
                        else:
                            if idx > 0:
                                new_a.append(' | ' + part)
                            else:
                                new_a.append(part)
                            idx += 1
                    a = new_a
                    res = ''
                    add = False
                    for part in a:
                        p = 0.0
                        if not add and len(probabilities[tag].items()) == 0:
                            p = 1.0
                            add = True
                        for key, value in probabilities[tag].items():
                            if key in re.split(' |\(|\)', part.lower()):
                                p = value
                                break
                        if (';' in part and ')' in part[:2]):
                            res += part
                        else:
                            res += part + ' @@ ' + str(p)
                    idx = res.rfind(';')
                    res = res[:idx] + res[idx + 1:] + ' ;'
                    out.write(res + '\n')
            out.write('''
Style = "<style>" Template "</style>" @@ 1.0;\n
Img = "<img src=xx:" Template ">" @@ 1.0;\n
Default = "<br>" Template "</br>" @@ 1.0;\n
Href = AStart Template AEnd @@ 0.5 | HrefStart Template HrefEnd @@ 0.5;\n
AStart = "<a href=\\"#\\">" @@ 1.0;\n
AEnd = "</a>" @@ 1.0;\n
HrefStart = "<a href=\\"" @@ 1.0;\n
HrefEnd = "\\">abc</a>" @@ 1.0;\n
                      ''')
