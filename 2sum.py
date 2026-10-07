'''
➔ Дан отсортированный по возрастанию массив целых чисел
и некоторое число target.
➔ Необходимо найти два числа в массиве, которые в сумме дают
заданное значение target, и вернуть их индексы.
'''
def 2sum(arr, target):
  i = 0
  j = len(arr) - 1
  while i<j:
    s = arr[j] + arr[i]
    if s == target:
      return [i, j]
    elif s<target:
      i+=1
    else:
      j-=1
  return []
