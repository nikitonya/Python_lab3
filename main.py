# пузырьком + yaml
import json
from tqdm import tqdm


def bubble_sort(arr: list):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


class SortPeople:
    data: list

    def __init__(self, path) -> None:
        self.data = json.load(open(path, encoding='windows-1251'))


def bubblesort(data: list, flag: str) -> list:
    with tqdm(range(len(data) - 1)) as pbar:
        for j in range(len(data) - 1):
            for i in range(len(data) - 1 - j):
                # print(f"Сейчас сравниваются {data[i][flag]} от {data[i]['email']} и {data[i + 1][flag]} от {data[i+1]['email']}")
                if float(data[i][flag]) > float(data[i + 1][flag]):
                    # print("Смена")
                    data[i], data[i + 1] = data[i + 1], data[i]
            pbar.update(1)
    return data


valid_data = SortPeople("C:\\Users\\nikit\\PycharmProjects\\python_lab3\\output.txt")
sort_data = bubblesort(valid_data.data[0:100], 'height')

json.dump(
    sort_data,
    open(
        "C:\\Users\\nikit\\PycharmProjects\\python_lab3\\check.txt",
        "w",
        encoding="windows-1251"), indent=5, ensure_ascii=False,)
