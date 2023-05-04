a = input().split()
b=a.pop(len(a)-1)
a.insert(0, b)
c = " ".join(a)
print(c)
# по-другому я не понимаю 

правильное выполнение:
  def shift(arr):
    buff = arr[-1]
    for i in range(len(arr)-1, 0, -1):
      arr [i] = arr [i - 1]
    arr [0] = buff
    return arr
print(shift([1, 2, 3, 4, 5]))  
