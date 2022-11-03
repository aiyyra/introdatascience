import re

def arithmetic_arranger(problems, solve = False):

        ##make it only take 4 question max
    if (len(problems)>5):
      return "Error: Too many problems."
      
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""

        ## make sure all the problem only related to + and - problem
        ## also make sure that the question only have digit number + "try making it clear to only send integer only problem"
    for problem in problems :
      if(re.search("[^\s0-9.+-]",problem)):
        if(re.search("[/]",problem) or re.search("[*]",problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."

        ## break the problem to its respected grp
      firstn = problem.split(" ")[0]
      oper = problem.split(" ")[1]
      secondn = problem.split(" ")[2]
      
        ## specify to only take 3 digit number
      if(len(firstn) > 4 or len(secondn) > 4):
        return "Error: Numbers cannot be more than four digits."

        # declare sum variable to store answer
      sum = ""
      if(oper == "+"):
        sum = str( int(firstn) + int(secondn) )
      elif(oper == "-"):
        sum = str( int(firstn) - int(secondn) )

        # designing the layout to present answer
      length = max(len(firstn),len(secondn)) + 2
      top = str(firstn).rjust(length)
      bottom = oper + str(secondn).rjust(length -1)
      line = ""
      res = str(sum).rjust(length)
      
      for s in range(length):
        line += "-"

      if problem != problems[-1]:
        first += top + "    "
        second += bottom + "    "
        lines += line + "    "
        sumx += res + "    "
      else :
        first += top
        second += bottom
        lines += line
        sumx += res

      if solve:
        string = first + "\n" + second + "\n" + lines + "\n" +sumx
      else :
        string = first + "\n" + second + "\n" + lines 
        
    return string

##can take max 4 question in a time
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))