def tree(n):
    if not isinstance(n, int) and not isinstance(n, str) or not n.isdigit():
        return 'TYPE_ERROR'
    n = int(n)
    if n < 3:
        return none
    else:
        n = int(n)
        k_st = 1
        k_sp = n*2 - 2
        s=''
        for i in range(1,n):
            s += k_sp // 2 * ' ' + k_st * '*' + k_sp // 2 * ' ' + '\n'
            k_st += 2
            k_sp -= 2
        s+= (n - 1) * ' ' + '|' + (n-1) * ' '
        return s
