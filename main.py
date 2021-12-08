# пузырьком + yaml
import json

def bubble_sort(arr: list):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


class sort_people:

    data : list

    def __init__(self, path):
        self.data = json.load(open(path, encoding = 'utf-8'))


