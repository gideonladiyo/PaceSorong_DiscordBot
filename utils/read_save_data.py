import json

def read_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
        return data

def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)