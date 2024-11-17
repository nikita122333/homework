#дз 1.1
sum = 0
N = int(input())
for i in range(2, N + 1):
  f = 0
  for t in range(1, i):
    if i%t == 0:
      f = f+1
  if f == 1:
    sum = sum + i
print(sum)

#дз 1.2
s = 'он дивен, палиндром, и ни морд ни лап не видно'
s = s.replace(' ', '')
s = s.replace(',', '')

f = 0
left = 0
right = len(s) - 1

while left < right:
  if s[left] != s[right]:
    f = 1
  left += 1
  right -= 1

if f == 0:
  print("True")
else:
  print("False")


  #дз 1.3
s = ["3", "5", '*', '5', "+"]
stack = []
for t in s:
  if t.isdigit():
    stack.append(int(t))
  else:
    b = stack.pop()
    a = stack.pop()
    if t == '+':
      res = a + b
    elif t == '-':
      res = a - b
    elif t == '*':
      res = a * b
    elif t == '/':
      res = int(a / b)

    stack.append(res)

print(stack[-1])


ДЗ 1.4

|Str      | Сложность| Пояснение |
|------------- | ------ | ------------|
|Получение элемента, s[i]  |O(1)| выполняется за константное время|
|Размер списка, len(s)  |O(1)| выполняется за константное время|
|Получение среза, s[a:b] |O(b-a) или O(1)| при указывании обоих переменных - за константное время, если s[:] - то по линейной зависимости от длины строки|
  



| Set                                      | Сложность| Пояснение |
|------------------------------------------| -------------| ---------|
| Размер множества, len(s)                 | O(1)| выполняется за константное время|
| Добавление элемента, s.add(x)            | O(1)| выполняется за константное время|
| Проверка наличия значения, x in/not in s | O(1)| выполняется за константное время|
| Перебор множества, for v in s:           | O(N)| Линейная зависимость от длины set|
| Объединение (union), s \| t              | O(len(s)+len(t))| Линейная зависимость от суммы длин set1 и set2 |

