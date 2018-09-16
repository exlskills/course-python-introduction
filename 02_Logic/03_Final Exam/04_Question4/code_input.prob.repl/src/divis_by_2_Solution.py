def divis_by_2_solution(lst):
    s = 0
    for value in lst:
        if value % 2 == 0:
            s += value
    return s
