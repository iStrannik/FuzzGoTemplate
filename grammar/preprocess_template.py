import argparse
import os
import string
import random

parser = argparse.ArgumentParser()

parser.add_argument('--filename', dest='filename', default='1.tpl')

parser.add_argument('--directory-to-save', dest='directory', default='preprocessed_tests', required=False)

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

args = parser.parse_args()

directory = args.directory

filename = args.filename

if not os.path.isdir(directory):
    os.mkdir(directory)

with open(filename, 'r') as file:
    cur = 0
    result = 'TEXT\n'
    for line in file.readlines():
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
    with open(directory + '/' + randomword(5), 'w') as ans:
        ans.write(result)
    

