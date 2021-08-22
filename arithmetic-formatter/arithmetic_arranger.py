def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = [''] * 4 if answer else [''] * 3
    for problem in problems:
        n1, op, n2 = problem.split()

        if op not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not (n1.isdigit() and n2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(n1) > 4 or len(n2) > 4:
            return "Error: Numbers cannot be more than four digits."

        length = max(len(n1), len(n2)) + 2

        arranged_problem = [n1.rjust(length),  # first line
                            op + n2.rjust(length - 1),  # second line
                            '-' * length]  # third line
        if answer:
            arranged_problem.append(str(eval(n1 + op + n2)).rjust(length))  # fourth line

        for i, line in enumerate(arranged_problem):
            arranged_problems[i] += line + ' ' * 4 if problem != problems[-1] else line

    return "\n".join(arranged_problems)
