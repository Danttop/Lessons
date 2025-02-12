def flick_switch(lst):
    flag = True
    return [flag := not flag if word == "flick" else flag for word in lst]
