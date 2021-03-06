import functools

def compute_problem(files):
  start = 0
  voo = [int(val) for val in open(files,"r").readlines()]
  lines = [0] + voo.copy()
  end = max(voo) 
  three_diff = 1
  one_diff = 0



  for i,voltage in enumerate(voo):
    if (start + 1) in voo:
      start += 1
      one_diff += 1
    elif (start + 3) in voo:
      start += 3
      three_diff += 1
    else:
      print("Hmmmmmmm")

  @functools.lru_cache(maxsize=None)
  def compute_split(m: int):
    sols = 0
    if m == end:
      return 1
    if (m + 1) in voo:
      sols += compute_split(m + 1)
    if (m + 2) in voo:
      sols += compute_split(m + 2)
    if (m + 3) in voo:
      sols += compute_split(m + 3)
    return sols

  lines.sort()
  out = compute_split(max(lines[0:1]))


  def count_out(x):
      if isinstance(x, int):
          return 0
      return 1 + sum(count_out(i) for i in x)
  print(f"Possible Outcomes: {out}")
  print(f"One Difference: {one_diff}\nThree Diff: {three_diff}\nMultiplied: {one_diff*three_diff}")

compute_problem("day10.txt")
#print(len(out[0][0]))
# base = [0]

# def compute_split(elm: int):
  
#   if (last_elm + 1) in voo:
#     l_a.append(last_elm + 1)
#   if (last_elm + 3) in voo:
#     l_b.append(last_elm + 3)
#   return [l_a,l_b]

# def combute_combinations(l: list):
#   for v in combute_split(l):

# print(compute_split(base))

# print(start)
# print(one_diff)
# print(three_diff)
# print(one_diff*three_diff)
