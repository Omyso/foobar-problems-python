def solution(xs):
  n = len(xs)
  if n == 1:
    return str(xs[0])
  positives = []
  negatives = []
  zero_counter = 0
  answer = 1
  for i in xs:
    if i > 0:
      positives.append(i)
    if i == 0:
      zero_counter +=1
    if i < 0:
      negatives.append(i)


  if len(negatives) == 1 and zero_counter > 0 and zero_counter + len(negatives) == n:
    return str(0)
  if zero_counter == n:
    return str(0)

  negatives.sort()
  if len(negatives) % 2 == 1:
    negatives.pop(len(negatives)-1)
  for i in positives:
    answer = answer * i
  for i in negatives:
    answer = answer * i
  return str(answer)
print(solution([696, 254, 707, 730, 252, 144, 18, -678, 921, 681, -665, 421, -501, 204, 742, -609, 672, -72, 339, -555, -736, 230, -450, 375, 941, 50, 897, -192, -912, -915, 609, 100, -933, 458, -893, 932, -590, -209, 107, 473, -311, 73, 68, -229, 480, 41, -235, 558, -615, -289, -643]))