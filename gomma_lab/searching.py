def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    target = 30

    print("Array:", arr)
    print("Target:", target)
    print("Linear Search Result:", linear_search(arr, target))
    print("Binary Search Result:", binary_search(arr, target))
