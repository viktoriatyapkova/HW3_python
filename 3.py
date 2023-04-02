a = input().split()
b=a.pop(len(a)-1)
a.insert(0, b)
c = " ".join(a)
print(c)
# по-другому я не понимаю 