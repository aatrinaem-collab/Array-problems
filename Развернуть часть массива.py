'''
Развернуть
часть массива
➔ Дан массив целых чисел.
➔ Необходимо повернуть (сдвинуть) справа налево
часть массива, которая указана вторым параметром.
➔ Сделать это надо за линейное время
без дополнительных аллокаций

'''
def rev(arr, l , r):
  while l<r:
    arr[l], arr[r] = arr[r], arr[l]
    l+=1
    r-=1
  return arr
def rev_partly (arr, k):
  k=k%len(arr)
  rev(arr, 0, len(arr)-1)
  rev(arr, 0, k-1)
  rev(arr, k, len(arr) - 1)
  return arr
