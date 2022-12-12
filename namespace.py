def namespace(s: str):
    s_obj = {}
    for k in reversed(s.split('.')):
        s_obj = {k : s_obj}
    return s_obj
   
