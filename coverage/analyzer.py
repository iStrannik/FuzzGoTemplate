import argparse
import os
import json
import random

parser = argparse.ArgumentParser()

parser.add_argument('--newreport', dest='newreport', default='new.out')
parser.add_argument('--oldreport', dest='oldreport', default='old.out')
parser.add_argument('--merge', dest='merge', default='merged.out')

args = parser.parse_args()

newreport = args.newreport
oldreport = args.oldreport
merge = args.merge

def parse_report_file(filename):
    result = {}
    with open(filename, 'r') as file:
        for i in file.readlines()[1:]:
            a = i.split(' ')
            if int(a[2]) > 0:
                result[a[0]] = 1
    return result

def merge_reports(oldreport, newreport):
    result = False
    for key, _ in newreport.items():
        if key not in oldreport:
            result = True
            oldreport[key] = 1
    return oldreport, result


with open(oldreport, 'r') as f:
    oldcoverage = json.load(f)

newcoverage = parse_report_file(newreport)

updatedcoverage, res = merge_reports(oldcoverage, newcoverage)

if res:
    print('Find new coverage')

with open(merge, 'w') as f:
    json.dump(updatedcoverage, f)
