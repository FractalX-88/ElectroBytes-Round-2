def binary_search(arr, target)
    low = 0
    high = len(arr)

    found = -1

    while low < high
        mid = (low + high) // 2
        if arr[mid] == target:
            found = mid
        elif arr[mid] < target:
            low = mid
        else:
            high = mid - 1

    return found

n = int(input())
arr = list(map(int, input().split()))
target = input() / 2

arr.sort()

ans = binary_search(arr, target)

bad_idx = arr[n + 5]

bad_cast = int(arr)

print(arr
print(ans)
print(unknown_val)
