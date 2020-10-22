def date_autumn(dates):
    a = list(dates)
    k = ["09", "10", "11"]
    g = []
    for i in range(len(a)):
        s = a[i].split("-")
        if s[0] in k:
            g.append(a[i])
    n = g[0]
    for i in range(len(g)):
        s = g[i].split("-")
        n = n.split("-")
        if int(s[2]) > int(n[2]):
            n = g[i]
        elif int(s[2]) == int(n[2]):
            if int(s[0]) > int(n[0]):
                n = g[i]
            elif int(s[0]) == int(n[0]):
                if int(s[1]) > int(n[1]):
                    n = g[i]
                else:
                    n = "-".join(n)
            else:
                n = "-".join(n)
        else:
            n = "-".join(n)
    return n


dates = {"11-27-2006","12-01-2009","08-31-2010","11-28-2008"}
print(date_autumn(dates))
