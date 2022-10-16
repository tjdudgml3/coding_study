#2차방정식을 완전탐색으로 풀어봄. 범위가 작아서 완전탐색으로 써도 될것같아 완전탐색으로 했다.
a,b = input().split(" ")

def sol(a,b):
  answer = []
  for x in range(200):
    xx = x- 100
    if xx**2 + 2*int(a)*xx + int(b) == 0:
      answer.append(xx)
  return answer
answer = sol(a,b)
for a in answer:
  print(a,end = " ")
