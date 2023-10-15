import random


def main():
    while True:
        try:
            length = int(input("Введите длину списка: "))
            if length <= 0:
                print("Длина списка должна быть больше 0!")
                continue
        except ValueError:
            print("Длина списка должна быть целым числом!")
            continue

        arr = generate_list(length=length)
        print("Перед: ", arr)
        sort(arr)
        print("После: ", arr)
        print()


def generate_list(length: int):
    return [
        random.randint(0, 1000)
        for i in range(length)
    ]


def sort(arr: list[int]):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]


if __name__ == '__main__':
    main()
