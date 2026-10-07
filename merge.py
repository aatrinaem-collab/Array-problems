'''
Слияние двух
отсортированных
массивов
➔ Дано два отсортированных массива.
➔ Необходимо написать функцию которая объединит
эти два массива в один отсортированный.
'''
def merge(a,b):
  c = []
  i, j = 0, 0 
  n, m  = len(a), len(b)
  while i<n and j< m:
    if a[i]<b[j]:
      c.append(a[i])
      i+=1
    else:
      c.append(b[j])
      j+=1
  while i<n:
    c.append(a[i])
    i+=1
  while j<m: 
    c.append(b[j])
    j+=1
  return c


