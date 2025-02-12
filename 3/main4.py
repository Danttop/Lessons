def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count = sums = 0
    for number in arr:
        if number > 0:
            count += 1
        elif number < 0:
            sums += number
    return [count, sums]
