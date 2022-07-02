import argparse
import os
import tempfile
import json

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--key', default='')
    parser.add_argument ('--val', default='')
    return parser

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
data = {}


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    if not os.path.exists(storage_path) :
        with open(storage_path, 'w') as f:
            f.write(json.dumps({'defaultkey':['defaultvalue']}))
    with open(storage_path, 'r') as f:
        data = dict(json.load(f))
    if bool(namespace.val) :
        if namespace.key not in data :
                data[namespace.key] = list()
        data[namespace.key].append(namespace.val)
        with open(storage_path, 'w') as f:
            f.write(json.dumps(data))
    else :
        print(', '.join(data.get(namespace.key, '')))
