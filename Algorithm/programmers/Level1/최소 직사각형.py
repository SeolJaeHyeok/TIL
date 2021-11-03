def solution(sizes):
    sizes = [sorted(size, reverse=True) for size in sizes]
    width = [size[0] for size in sizes]
    height = [size[1] for size in sizes]

    return max(width) * max(height)