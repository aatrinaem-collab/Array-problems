'''
Минимальный размер
подмассива
Дан массив положительных целых чисел nums и
положительное целое число target. Верните
подмассив минимальной длины, сумма элементов
которого больше или равна target. Если такого
подмассива не существует, верните 0.

'''
def min_sub_array(nums, target):
    L = float('inf')   
    l = 0
    cur_sum = 0

    for r in range(len(nums)):
        cur_sum += nums[r]

        while cur_sum >= target:
            size = r - l + 1
            if size < L:
                L = size
            cur_sum -= nums[l]
            l += 1

    return L if L != float('inf') else 0
