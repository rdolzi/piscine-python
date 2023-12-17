import sys


# if len(sys.argv) < 2:
#     print("Error! No string given")
# else:


count = {}
for s in sorted(sys.argv[1]):
  if s in count:
    count[s] += 1
  else:
    count[s] = 1





# ------------ 1 -----------------
for key, value in sortedd.items():
    print(f'{key} = {value}')

print("\n")
# ------------ 2 -----------------
for i  in count:
  print(f'{i} = {count[i]}')

