import argparse
import os
from os import listdir
from os.path import isfile, join
from shutil import rmtree

import grammar
from add_probabilities import create_grammar_with_probabilities
from generate_test import get_coverage
from preprocess_template import preprocess_template

parser = argparse.ArgumentParser()

parser.add_argument('--workingDir', dest='workingDir')
parser.add_argument('--tribble', dest='tribble',
                    default='../tribble/tribble.jar')

args = parser.parse_args()


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

for epoch in range(1, 3):
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
        'counter.json', baseGrammarFile, probabilistic_grammar)
    os.rename('counter.json', join(args.workingDir, f'{epoch}/counter.json'))
    os.system(
        f'java -jar {args.tribble} generate --mode=10-probabilistic-10 --out-dir={pathToTemplates} --suffix=.tpl --grammar-file={probabilistic_grammar}')
    _ = input('Waiting...')
    templates = [f for f in listdir(
        pathToTemplates) if isfile(join(pathToTemplates, f))]
    for tpl in templates:
        canRun, findNewCow, updatedcoverage = get_coverage(
            join(pathToTemplates, tpl), '/home/strannik/go/src/go/src/html/template', oldcoverage=updatedcoverage)
        if findNewCow:
            os.rename(join(pathToTemplates, tpl), join(goodTemplates, tpl))
    _ = input('Waiting...')
    basetemplates = [read_template(join(goodTemplates, f)) for f in listdir(
        goodTemplates) if isfile(join(goodTemplates, f))]
