def xor(xorlist):
    for i in range(len(xorlist)):
        if xorlist[i] % 4 == 1:
            xorlist[i] = 1
        elif xorlist[i] % 4 == 2:
            xorlist[i] = xorlist[i] + 1
        elif xorlist[i] % 4 == 3:
            xorlist[i] = 0


def solution(start, length):
    if length == 1:
        return start

    l = length - 1
    xorlist = []

    while l > -1:
        xorlist.append(start - 1)
        xorlist.append(start + l)
        start = start + length
        l = l - 1

    xor(xorlist)

    final_xor = 0

    for i in range(len(xorlist)):
        final_xor = final_xor ^ xorlist[i]

    return final_xor


print(solution(17, 200))
