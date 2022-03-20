def solution(pegs):
    n = len(pegs)
    first_radius = [0] * 2
    s = []
    sigma = 0
    odd_or_even = 1
    for i in range(0, n - 1):
        s.append(pegs[i + 1] - pegs[i])
        if i % 2 == 0:
            odd_or_even = 1
        else:
            odd_or_even = -1
        sigma = sigma + s[i] * odd_or_even

    if n % 2 == 0:
        if (sigma % 3 == 0):
            first_radius[0] = (2 * sigma) / 3
            first_radius[1] = 1
        else:
            first_radius[0] = 2 * sigma
            first_radius[1] = 3
    else:
        first_radius[0] = 2 * sigma
        first_radius[1] = 1
    return ensure(s, first_radius, n)


def ensure(s, firstrad, n):
    check = firstrad[0] / firstrad[1]
    for i in range(0, n - 1):
        if s[i] - check < 1:
            return [-1, -1]
        check = s[i] - check
    return firstrad


print(solution([4, 30, 50]))