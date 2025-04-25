import pathlib
import os
import json
import sys

os.path.realpath(__file__)
testsFile = sys.argv[1] # tests.json
valuesFile = sys.argv[2] # values.json
reportJson = sys.argv[3] # report.json

def readAll(filePath):
    with open(filePath, "r", encoding="utf-8") as f:
        return f.read()

def get_status(values, id):
    for value in values['values']:
        if id == value['id']:
            return value['value']
    return 'not found'

def get_values(tests, statusValues):
    for test in tests:
        if test.get('values') is not None:
            get_values(test['values'], statusValues)
            test['value'] = get_status(statusValues, test['id'])
        else:
            test['value'] = get_status(statusValues, test['id'])
    return tests


if __name__=="__main__":
    values = json.loads(readAll(valuesFile))
    tests = json.loads(readAll(testsFile))
    results = get_values(tests['tests'], values)
    with open(reportJson, 'w') as outfile:
        json.dump(results, outfile)

