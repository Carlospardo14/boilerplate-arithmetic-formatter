def arithmetic_arranger(problems, solve=False):

  math_list = list()
  math_list.append(problems)
  left = list()
  operator = list()
  rigth = list()
  top_list = list()
  mid_list = list()
  row_list = list()
  resul_list = list()
  top_row = ''
  second = ''
  third = ''
  fourth = ''
  string = ''
  full_num = ''
  
  for problem in problems:
    num_problems = len(problems)

    if num_problems > 5:
      return ('Error: Too many problems.')

    for op in problem:
      if op.find('*') > -1 or op.find('/') > -1: 
        return ("Error: Operator must be '+' or '-'.")

    left.append(problem[:problem.find(' ')])
    operator.append(problem[problem.find(' ') + 1:problem.find(' ') + 2])
    rigth.append(problem[problem.find(' ') + 3:])

    full_num = left +  rigth

  for num in full_num:
    if len(num) > 4 :
      return ('Error: Numbers cannot be more than four digits.')
  for num in full_num:
    if num.isdigit() is False:
      return ('Error: Numbers must only contain digits.')
  
  for x, i in enumerate(left):
    maxlen = max(len(rigth[x]), len(i)) +2
    solution = eval(i+operator[x]+rigth[x])
    top = str(i).rjust(maxlen)
    mid = operator[x] + str(rigth[x]).rjust(maxlen -1)
    rows = maxlen*('-')
    bottom = str(solution).rjust(maxlen)
    top_list.append(top)
    mid_list.append(mid)
    row_list.append(rows)
    resul_list.append(bottom)

  for x in top_list:
    top_row += x + '    '

  for x in mid_list:
    second += x + '    '
  
  for x in row_list:
    third += x + '    '
  
  for  x in resul_list:
    fourth += x + '    '

  top_row = top_row[:len(top_row)-4]
  second = second[:len(second)-4]
  third = third[:len(third)-4]
  fourth = fourth[:len(fourth)-4]
    
  if solve :
      string = '\n'.join((top_row, second, third, fourth))
  else :
      string = '\n'.join((top_row, second, third))
  return string