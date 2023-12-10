import json

def readJsonFile(filename):
    with open(filename, 'r') as target_file:
        target_data = json.load(target_file)
        return target_data

if __name__ == '__main__':
    target = readJsonFile('./target.json')
    print(target)