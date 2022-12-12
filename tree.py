def tree(n:int):
    if isinstance(n, int) or isinstance(n, str) and n.isdigit():
        if n < 3:
            return 'Null'
        else:
            n = int(n)
            k_st = 1
            k_sp = n*2 - 2 
            s=''
            for i in range(1,n):
                s += k_sp // 2 * ' ' + k_st * '*' + k_sp // 2 * ' ' + '\n'
                k_st+=2
                k_sp-=2
            s+= (n - 1) * ' ' + '|' + (n-1) * ' '
            return s
    else: return 'TYPE_ERROR'
