import argparse
import os
from os import listdir
from os.path import isfile, join
from shutil import rmtree
import subprocess

import grammar
from add_probabilities import create_grammar_with_probabilities
from generate_test import get_coverage
from preprocess_template import preprocess_template
from parse_percents import get_percents

parser = argparse.ArgumentParser()

parser.add_argument('--mutate', action='store_true', default=False)
parser.add_argument('--workingDir', dest='workingDir')
parser.add_argument('--tribble', dest='tribble',
                    default='../tribble/tribble.jar')

args = parser.parse_args()
print(args.mutate)

def read_template(filename):
    with open(filename, 'r') as file:
        result = file.readlines()
    return result


baseGrammarFile = join(args.workingDir, 'grammar.tribble')
pathToTemplates = join(args.workingDir, '0/templates/')

basetemplates = [read_template(join(pathToTemplates, f)) for f in listdir(
    pathToTemplates) if isfile(join(pathToTemplates, f))]

basetemplates = [preprocess_template(tpl) for tpl in basetemplates]
updatedcoverage = {}
tree_depth = 10
number_of_tests = 10
needMutation = False
with open('history.csv', 'w') as history:
    history.write('epoch\tcoverage\n')
    history.flush()
    for epoch in range(1, 1000000):
        if not args.mutate:
            needMutation = False
        if os.path.exists(join(args.workingDir, f'{epoch}/')):
            rmtree(join(args.workingDir, f'{epoch}/'))
        os.mkdir(join(args.workingDir, f'{epoch}/'))
        pathToTemplates = join(args.workingDir, f'{epoch}/templates/')
        goodTemplates = join(args.workingDir, f'{epoch}/goodTemplates/')
        os.mkdir(pathToTemplates)
        os.mkdir(goodTemplates)
        with open('counter.json', 'w') as file:
            file.write('{}')
        for tpl in basetemplates:
            grammar.listen_and_count(tpl)

        probabilistic_grammar = join(
            args.workingDir, f'{epoch}/probabilistic_grammar.tribble')
        create_grammar_with_probabilities(
            'counter.json', baseGrammarFile, probabilistic_grammar, needMutation)
        needMutation = False
        os.rename('counter.json', join(args.workingDir, f'{epoch}/counter.json'))
        os.system(
            f'java -jar {args.tribble} generate --mode={tree_depth}-probabilistic-{number_of_tests} --out-dir={pathToTemplates} --suffix=.tpl --grammar-file={probabilistic_grammar}')
        #_ = input('Waiting...')
        templates = [f for f in listdir(
            pathToTemplates) if isfile(join(pathToTemplates, f))]
        for tpl in templates:
            findNewCow, updatedcoverage = get_coverage(
                join(pathToTemplates, tpl), '/home/strannik/go/src/go/src/html/template', oldcoverage=updatedcoverage)
            if findNewCow:
                os.rename(join(pathToTemplates, tpl), join(goodTemplates, tpl))
        #_ = input('Waiting...')
        with open('total_coverage.out', 'w') as cov:
            cov.write('mode: count\n')
            for i in updatedcoverage.items():
                cov.write(f'{i[0].replace("std/","")} {i[1][0]} {i[1][1]}')
        a = subprocess.Popen(
                    ["scov", "--srcdir", "/home/strannik/go/src/go/src/", "total_coverage.out"])
        _ = a.wait()
        percents = get_percents('index.html')
        history.write(f'{epoch}\t{percents}\n')
        history.flush()
        basetemplates = [read_template(join(goodTemplates, f)) for f in listdir(
            goodTemplates) if isfile(join(goodTemplates, f))]
        if len(basetemplates) == 0:
            needMutation = True
            basetemplates = [read_template(join(pathToTemplates, f)) for f in listdir(
                pathToTemplates) if isfile(join(pathToTemplates, f))]
        basetemplates = [preprocess_template(tpl) for tpl in basetemplates]
