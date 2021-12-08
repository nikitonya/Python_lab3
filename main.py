# пузырьком + yaml
import json
import yaml
from tqdm import tqdm


class ValidPeople:
    data: list

    def __init__(self, path) -> None:
        self.data = json.load(open(path, encoding='windows-1251'))


def bubblesort(data: list, flag: str) -> list:
    with tqdm(range(len(data) - 1), colour="Blue", ncols = 150) as pbar:
        for j in range(len(data) - 1):
            for i in range(len(data) - 1 - j):
                if str(data[i][flag]) > str(data[i + 1][flag]):
                    data[i], data[i + 1] = data[i + 1], data[i]
            pbar.update(1)
    return data


def write_yaml(sort_data, path):
    with open(path, 'w') as write_file:
        yaml.dump(sort_data, write_file)


def read_yaml(path):
    with open(path, 'r') as read_file:
        return yaml.safe_load(read_file)


valid_data = ValidPeople("C:\\Users\\nikit\\PycharmProjects\\python_lab3\\output.txt")
sort_data = bubblesort(valid_data.data, "height")

json.dump(
    sort_data,
    open(
        "C:\\Users\\nikit\\PycharmProjects\\python_lab3\\check.txt",
        "w",
        encoding="windows-1251"), indent=5, ensure_ascii=False)

write_yaml(sort_data, 'serialization.yaml')
read = read_yaml('serialization_all.yaml')

print(read)
