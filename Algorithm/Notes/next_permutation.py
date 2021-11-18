def next_permutation(arr):
    if type(arr) == str:
        arr = list(arr)

    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return False

    j = len(arr) - 1
    while arr[i] >= arr[j]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    result = arr[:i + 1]
    result.extend(list(reversed(arr[i + 1:])))

    return result


print(next_permutation('HELLO'))
print(next_permutation('DRINK'))
print(next_permutation('SHUTTLE'))
print(next_permutation('ZOO'))

