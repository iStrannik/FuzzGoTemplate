import argparse
import os
from os import listdir
from os.path import isfile, join
from shutil import rmtree
import subprocess
from enum import Enum
import random
import logging

import grammar
from add_probabilities import create_grammar_with_probabilities
from generate_test import get_coverage
from preprocess_template import preprocess_template, simple_preprocess_template
from parse_percents import get_percents
from mutations import random_probability_change

TREE_DEPTH = 10
NUMVER_OF_TESTS = 10
EPOCHS = 50000
EPOCHS_WITHOUT_NEW_COVERAGE = 1
SIMILARITY = 1.0


class Mutation(Enum):
    Random = 1
    Invert = 2


parser = argparse.ArgumentParser()

parser.add_argument('--random_mutation', action='store_true', default=False)
parser.add_argument('--invert_mutation', action='store_true', default=False)
parser.add_argument('--workingDir', dest='workingDir')
parser.add_argument('--decay', dest='decay', default=1.0, type=float)
parser.add_argument('--tree_depth', dest='tree_depth', default=10, type=int)
parser.add_argument('--generation', dest='generation', default=10, type=int)
parser.add_argument('--tribble', dest='tribble', default='../tribble/tribble.jar')

args = parser.parse_args()

if not os.path.exists(args.workingDir):
    os.mkdir(args.workingDir)
    os.system(f'cp -r ./start_data/* {args.workingDir}/')

TREE_DEPTH = args.tree_depth
NUMVER_OF_TESTS = args.generation


def read_template(filename):
    with open(filename, 'r') as file:
        result = file.readlines()
    return result


logging.basicConfig(filename=join(args.workingDir, 'example.log'), encoding='utf-8', level=logging.DEBUG)

mutations = []

if args.random_mutation:
    mutations.append(Mutation.Random)

if args.invert_mutation:
    mutations.append(Mutation.Invert)

logging.info(f'availiable mutations: {mutations}')

baseGrammarFile = join(args.workingDir, 'grammar.tribble')
pathToTemplates = join(args.workingDir, '0/templates/')

basetemplates = [
    read_template(join(pathToTemplates, f)) for f in listdir(pathToTemplates) if isfile(join(pathToTemplates, f))
]

basetemplates = [preprocess_template(tpl) for tpl in basetemplates]
updatedcoverage = {}

rounds_without_updates = 0
probabilities = None

if not os.path.exists(join(args.workingDir, 'possible_xss')):
    os.mkdir(join(args.workingDir, 'possible_xss'))

last_good_epoch = 1

with open(join(args.workingDir, 'history.csv'), 'w') as history:
    history.write('epoch\tcoverage\n')
    history.flush()
    for epoch in range(1, EPOCHS):
        logging.info(f'new epoch is {epoch}')
        logging.info(f'rouneds without updates {rounds_without_updates}')
        similarity = SIMILARITY
        current_mutation = None
        if rounds_without_updates >= EPOCHS_WITHOUT_NEW_COVERAGE:
            if not (len(mutations) == 0):
                current_mutation = random.choice(mutations)
        logging.info(f'current mutation is {current_mutation}')
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

        probabilistic_grammar = join(args.workingDir, f'{epoch}/probabilistic_grammar.tribble')
        probabilities = create_grammar_with_probabilities('counter.json',
                                                          baseGrammarFile,
                                                          probabilistic_grammar,
                                                          current_mutation is Mutation.Random,
                                                          old_probabilities=probabilities,
                                                          decay=args.decay)
        if epoch == 1:
            probabilities = random_probability_change(probabilities, 'globalfunctions')
        logging.info(f'probabilities are {probabilities}')
        os.rename('counter.json', join(args.workingDir, f'{epoch}/counter.json'))

        if current_mutation is Mutation.Invert:
            similarity = -1.0
        os.system(
            f'java -jar {args.tribble} generate --similarity={similarity} --mode={TREE_DEPTH}-probabilistic-{NUMVER_OF_TESTS} --out-dir={pathToTemplates} --suffix=.tpl --grammar-file={probabilistic_grammar}'
        )
        #_ = input('Waiting...')
        templates = [f for f in listdir(pathToTemplates) if isfile(join(pathToTemplates, f))]
        for tpl in templates:
            findNewCow, updatedcoverage = get_coverage(join(pathToTemplates, tpl),
                                                       '/root/go/src/go/src/html/template',
                                                       oldcoverage=updatedcoverage,
                                                       success_path=join(args.workingDir, 'possible_xss'))
            if findNewCow:
                os.rename(join(pathToTemplates, tpl), join(goodTemplates, tpl))

        #_ = input('Waiting...')
        with open('total_coverage.out', 'w') as cov:
            cov.write('mode: count\n')
            for i in updatedcoverage.items():
                cov.write(f'{i[0].replace("std/","")} {i[1][0]} {i[1][1]}')
        #_ = input('Waiting...')

        a = subprocess.Popen(
            ["scov", "--srcdir", "/root/go/src/go/src/", "--htmldir", args.workingDir, "total_coverage.out"])
        _ = a.wait()
        percents = get_percents(join(args.workingDir, 'index.html'))
        history.write(f'{epoch}\t{percents}\n')
        history.flush()
        basetemplates = [
            read_template(join(goodTemplates, f)) for f in listdir(goodTemplates) if isfile(join(goodTemplates, f))
        ]
        if len(basetemplates) == 0:
            pathToTemplates = join(args.workingDir, f'{last_good_epoch}/templates/')
            rounds_without_updates += 1
            basetemplates = [
                read_template(join(pathToTemplates, f)) for f in listdir(pathToTemplates)
                if isfile(join(pathToTemplates, f))
            ]
        else:
            last_good_epoch = epoch + 1
            rounds_without_updates = 0
        #basetemplates = [preprocess_template(tpl) for tpl in basetemplates]
        basetemplates = [simple_preprocess_template(tpl) for tpl in basetemplates]
