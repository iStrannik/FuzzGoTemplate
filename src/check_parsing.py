from preprocess_template import preprocess_template
import grammar

from os import listdir
from os.path import isfile, join

def read_template(filename):
    with open(filename, 'r') as file:
        result = file.readlines()
    return result

baseGrammarFile = 'start_data/grammar.tribble'
pathToTemplates = 'start_data/templates/'

basetemplates = [read_template(join(pathToTemplates, f)) for f in listdir(
    pathToTemplates) if isfile(join(pathToTemplates, f))]

basetemplates = [preprocess_template(tpl) for tpl in basetemplates]


with open('counter.json', 'w') as file:
    file.write('{}')
for tpl in basetemplates:
    grammar.listen_and_count(tpl)
