import math
def solution(area):
    current = area
    sol = []
    while(current > 1):
        num = math.sqrt(current)
        num = math.floor(num)
        num = num ** 2
        sol.append(int(num))
        current = current - num
    if current == 1:
      sol.append(1)
    return sol
print(solution(15134))