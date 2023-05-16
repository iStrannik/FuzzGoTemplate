import json
import re
from mutations import random_probability_change


def convert_cnt_to_probability(cnt):
    result = {}
    for key, value in cnt.items():
        total = 0
        if len(value.items()) == 0:
            continue
        for x, y in value.items():
            total += y
        if total == 0:
            continue
        result[key.lower()] = {}
        for x, y in value.items():
            result[key.lower()][x.lower()] = y / total
    return result


def decaying_probabilities_method(old_probabilities, new_probabilities, decay):
    for key, val in old_probabilities.items():
        #TODO Add all probabilities
        if key not in new_probabilities:
            new_probabilities[key] = val
            continue
        for key1, val1 in val.items():
            new_probabilities[key][key1] = val1 * (1 - decay) + new_probabilities[key].get(key1, 0) * decay
        for key1, val1 in new_probabilities[key].items():
            if key1 not in val:
                new_probabilities[key][key1] = val.get(key1, 0) * (1 - decay) + val1 * decay
    return new_probabilities


def create_grammar_with_probabilities(counter,
                                      grammar,
                                      probabilistic_grammar,
                                      need_mutation=False,
                                      old_probabilities=None,
                                      decay=1):
    with open(counter, 'r') as f:
        cnt = json.load(f)

    probabilities = convert_cnt_to_probability(cnt)

    if old_probabilities:
        probabilities = decaying_probabilities_method(old_probabilities, probabilities, decay)

    if need_mutation:
        probabilities = random_probability_change(probabilities)

    with open(grammar, 'r') as f:
        with open(probabilistic_grammar, 'w') as out:
            for i in f.readlines():
                i = i[:-1]
                tag = i.split(' =')[0].lower()

                if tag == 'text' and not old_probabilities:
                    out.write('Text = Href @@ 0.3| Default @@ 0.1 | Img @@ 0.1 | Style @@ 0.2 | Js @@ 0.3 ;\n')
                    continue

                if tag == 'name':
                    out.write(
                        'Name = "A " @@ 0.25 | "B " @@ 0.18 | "C " @@ 0.20 | "LocalName " @@ 0.02 | "D " @@ 0.15 | "E " @@ 0.10 | "F " @@ 0.10; \n')
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
                        if ')' in part and '")"' not in part and (part.find('(') == -1
                                                                  or part.find(')') < part.find('(')):
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
    return probabilities


def kek(out):
    out.write('''
Style = "<style>" GoAction "</style>" @@ 1.0;\n
Js = "<script>" GoAction "</script>" @@ 1.0;\n
Img = "<img src=xx:" GoAction ">" @@ 1.0;\n
Default = "<br>" GoAction "</br>" @@ 1.0;\n
Href = AStart GoAction AEnd @@ 0.5 | HrefStart GoAction HrefEnd @@ 0.5;\n
AStart = "<a href=\\"#\\">" @@ 1.0;\n
AEnd = "</a>" @@ 1.0;\n
HrefStart = "<a href=\\"" @@ 1.0;\n
HrefEnd = "\\">abc</a>" @@ 1.0;\n
                      ''')