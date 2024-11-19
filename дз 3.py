#1
def distance(x1, y1, x2, y2):
    print(y1-x1, y2-x2)


#2
def power(a, n):
  v = a
  while n > 1:
    a = a * v
    n = n - 1
  print(a)

#3
def capitalize(a):
  a = chr(ord(a[0])-32) + a[1:]
  return a

a = 'trcy vyb'
e = ''
a = a.split(' ')
for i in a:
  i = capitalize(i)
  e = e + str(i) + " "
print(e)

#4
def fctr(n):
    if n == 1:
        return 1
    return n * fctr(n-1)

#5
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

#6
def r():
  n = int(input())
  if n != 0:
    r()
    print(n)

r()

