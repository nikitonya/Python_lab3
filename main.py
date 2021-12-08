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
    with tqdm(total=len(data) - 1,desc='Sort', ncols=150) as progress_bar:
        for j in range(len(data) - 1):
            for i in range(len(data) - 1 - j):
               #print(f"Сейчас сравниваются {data[i][flag]} от {data[i]['email']} и {data[i + 1][flag]} от {data[i+1]['email']}")
               progress_bar.update(1)
               if float(data[i][flag]) > float(data[i + 1][flag]):
                   # print("Смена")
                   data[i], data[i + 1] = data[i + 1], data[i]
    return data


valid_data = SortPeople("C:\\Users\\nikit\\PycharmProjects\\python_lab3\\output.txt")
bubblesort(valid_data.data, 'height')
