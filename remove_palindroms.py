def remove_palindroms(spells):
    global new_list
    s = [i for i in spells]
    for i in range(len(s)):
        a = ("".join(s[i].split())).lower()
        if a == a[::-1] and s[i] in new_list:
            new_list.remove(s[i])
