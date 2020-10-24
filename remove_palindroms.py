def remove_palindroms(spells):
    global new_spells
    s = [i for i in spells]
    g = []
    for i in range(len(s)):
        k = 0
        a = ("".join(s[i].split())).lower()
        if a == a[::-1] and s[i] in new_list:
            new_list.remove(s[i])
