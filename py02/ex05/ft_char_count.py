import sys


if len(sys.argv) != 2:
    print("Error! No string given")
else:
  # STRING TO LIST
  char_list = list(sys.argv[1])
  # ALPHABETICAL SORTING
  n = len(char_list)
  i = 0
  while i < n:
      j = 0
      while j < n - i - 1:
          if char_list[j] > char_list[j + 1]:
              char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]
          j += 1
      i += 1
  # LIST TO STRING
  result_string = ""
  for char in char_list:
      result_string += char
  #STRING TO DICT
  count = {}
  for s in result_string:
    if s in count:
      count[s] += 1
    else:
      count[s] = 1


  #PRINTING ALTERNATIVES:
  # ------------ 1 -----------------
  for key, value in count.items():
      print(f'{key} = {value}')

  # print("\n")
  # ------------ 2 -----------------
  # for i  in count:
  #   print(f'{i} = {count[i]}')

