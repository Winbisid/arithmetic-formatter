# def arithmetic_arranger(problems, solve=False):
#   if len(problems) > 5:
#     return "Error: Too many problems"
#   topRow = ''
#   bottomRow = ''
#   dashes = ''
#   dashLength = 0
#   solution = ''
#   for problem in problems:
#     if problem.find('-') != -1:
#       index = problem.find('-')
#     elif problem.find('+') != -1:
#       index = problem.find('+')
#     else:
#       return "Error: Operator must be '+' or '-'"
#     firstPart = problem[:index].strip()
#     operator = problem[index]
#     secondPart = problem[index + 1:].strip()
#     try:
#       firstPartInt = int(firstPart)
#       secondPartInt = int(secondPart)
#     except:
#       return "Numbers must only contain digits"
#     inDashes = '-'
#     space = ' '
#     dashLength = max(len(firstPart), len(secondPart)) + 2

#     if (len(secondPart) > 4 or len(firstPart) > 4):
#       return "Numbers cannot be more than four digits"

#     if (solve == False):
#       solution = ''
#     elif (operator == '-'):
#       solSpace = space * \
#           (dashLength - len(str(firstPartInt - secondPartInt)))
#       solution += solSpace + str(firstPartInt - secondPartInt) + '\t'
#     else:
#       solSpace = space * \
#           (dashLength - len(str(firstPartInt + secondPartInt)))
#       solution += solSpace + str(firstPartInt + secondPartInt) + '\t'

#     topSpace = space * (dashLength - len(firstPart))
#     bottomSpace = space * (dashLength - len(secondPart) - 1)

#     topRow += topSpace + firstPart + "\t"
#     bottomRow += operator + bottomSpace + secondPart + "\t"
#     dashes += inDashes * dashLength + '\t'

#   return (f"{topRow}\n{bottomRow}\n{dashes}\n{solution}")


def arithmetic_arranger(problems, *args):
  if len(problems) > 5:
    return "Error: Too many problems."

  result = []

  for problem in problems:
    operation = problem.split()

    if operation[0].isnumeric() is False or operation[2].isnumeric() is False:
      return "Error: Numbers must only contain digits."

    if len(operation[0]) > 4 or len(operation[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    if operation[1] != "+" and operation[1] != "-":
      return "Error: Operator must be '+' or '-'."

    longest_number = max(len(operation[0]), len(operation[2]))
    width = int(longest_number + 2)

    line1 = f"{operation[0]:>{width}}"
    line2 = operation[1] + f"{operation[2]:>{width -1}}"
    dashes = '-' * width
    operation_result = int(operation[0]) + int(
      operation[2]) if operation[1] == "+" else int(operation[0]) - int(
        operation[2])
    operation_result = f"{operation_result:>{width}}"

    try:
      result[0] += (" " * 4) + line1
    except IndexError:
      result.append(line1)

    try:
      result[1] += (" " * 4) + line2
    except IndexError:
      result.append(line2)

    try:
      result[2] += (" " * 4) + dashes
    except IndexError:
      result.append(dashes)

    if args:
      try:
        result[3] += (" " * 4) + operation_result
      except IndexError:
        result.append(operation_result)

  arranged_problems = f"{result[0]}\n{result[1]}\n{result[2]}"
  arranged_problems = arranged_problems + f"\n{result[3]}" if args else arranged_problems

  return arranged_problems
