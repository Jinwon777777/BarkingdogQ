while True:
    s = input()
    if s == ".":
        break
    a = "yes"
    ans = []
    for st in s:
        if st == ".":
            break
        if st == "(" or st == "[":
            ans.append(st)
        elif st == ")":
            if not ans or ans[-1] != "(":
                a = "no"
                break
            else:
                ans.pop()
        elif st == "]":
            if not ans or ans[-1] != "[":
                a = "no"
                break
            else:
                ans.pop()
    if ans:
        a = "no"
    print(a, end='\n')