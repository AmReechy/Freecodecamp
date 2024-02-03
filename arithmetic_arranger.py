
def arithmetic_arranger(probs, show_ans= False):
    if len(probs) > 5:
        return "Error: Too many problems."
    soln_vals = []
    for q in probs:
        operator = '+' if '+' in q and '-' not in q else ('-' if '-' in q else "")
        if operator:
            #["9873-4156", "1072+ 5497", "2783 -7681", "2 + 9", "8 - 999"]
            #left_num = q[:q.index(operator)].strip() #"9873-4156"
            #right_num = q[q.index(operator)+1:].strip()
            #max_num_len = len(left_num) if len(left_num) > len(right_num) else len(right_num)
            left_num, right_num = [num.strip() for num in q.split(operator)]
            max_num_len = max([len(left_num), len(right_num)])
        else:
            return "Error: Operator must be '+' or '-'."
        if left_num.isdigit() and right_num.isdigit():
            if len(left_num)> 4 or len(right_num) > 4:
                return "Error: Numbers cannot be more than four digits."
            ans = eval(q)
            vals = (left_num, operator, right_num, max_num_len + 2, ans)
            soln_vals.append(vals)
        else:
            return "Error: Numbers must only contain digits."
    
    line1, line2, line3, line4 = "", "", "", ""
    for soln in soln_vals: #('9873', '-', '4156', 6, 5717)
        line1 += soln[0].rjust(soln[3]) + (" "*4)
        line2 += soln[1] + " " + soln[2].rjust(soln[3]-2) + (" "*4)
        line3 += "_"*(soln[3]) + (" "*4)
        line4 += str(soln[-1]).rjust(soln[3]) + (" "*4)

    #line1, line2, line3, line4 = [s.rstrip() for s in [line1, line2, line3, line4]]
    if show_ans:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + ''
         
           