import random
import string


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def preprocess_template(tpl):
    cur = 0
    result = 'TEXT\n'
    for line in tpl:
        start = 0
        end = len(line)
        while start < end:
            pos_open = line.find('{{', start)
            pos_close = line.find('}}', start)
            if pos_open == -1:
                pos_open = len(line)

            if pos_close == -1:
                pos_close = len(line)

            if pos_open <= pos_close:
                if pos_open == len(line):
                    break
                next_start = pos_open + 1
                cur += 1
                if cur > 1:
                    result += line[start - 1: next_start + 1]
            else:
                next_start = pos_close + 1
                if cur > 0:
                    result += line[start - 1: next_start + 1]
                cur -= 1
                if cur == 0:
                    result += '\nTEXT\n'
                cur = max(cur, 0)
            start = next_start

        if cur > 0:
            result += line[max(0, start - 1):]
    return result
