def remove_palindroms(spells):
    global new_spells
    s = [i for i in spells]
    g = []
    for i in range(len(s)):
        k = 0
        a = ("".join(s[i].split())).lower()
        if a == a[::-1]:
            new_spells.remove(s[i])

        
new_spells = ["Dog", "Repaper", "Cat"]
remove_palindroms(new_spells)
print(new_spells)
