print("Введите пять чисел, два из которых повторяется два раза")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a == c and b == d:
    print("повторяется один раз", e)
if a == b and c == d:
    print("повторяется один раз", e)
if a == d and b == c:
    print("повторяется один раз", e)
if a == e and b == c or b == e and a == c or c == e and a == b:
    print("повторяется один раз", d)
if a == e and b == d or a == d and b == e or a == b and d == e:
    print("повторяется один раз", c)
if a == c and d == e or a == d and c == e or a == e and c == d:
    print("повторяется один раз", b)
if b == c and d == e or b == d and c == e or b == e and c == d:
    print("повторяется один раз", a)

