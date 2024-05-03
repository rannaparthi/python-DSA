def arraysintersection(arr1, arr2, arr3):
    def search(arr, x):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            elif arr[mid] > x:
                right = mid - 1
            else:
                return mid
        return -1

    result = []

    for i in range(len(arr1)):
        if search(arr2, arr1[i]) != -1 and search(arr3, arr1[i]) != -1:
            result.append(arr1[i])
    return result

