def remove_palindroms(spells):
    s = [i for i in spells]
    for i in range(len(s)):
        a = ("".join(s[i].split())).lower()
        if a == a[::-1] and (s[i] in spells):
            spells.remove(s[i])
