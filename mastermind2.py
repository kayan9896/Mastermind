sett = {None}
co = ["A", "B", "C", "D", "E", "F","G","H"]


# Recursively generate all possible codes
def gen(c, s, cur):
    if len(c) == 6:
        s.add(c)
        return
    for i in range(cur, cur + 8):
        tmp = c + co[i % 8]
        gen(tmp, s, i % 8)
    return


gen("", sett, 0)


# Compare two codes and return the result
def judge(g1, g2):
    r = 0
    w = 0
    h1 = {}
    h2 = {}
    rd = {}
    v = {None}
    for i in range(6):
        if g1[i] in h1:
            h1[g1[i]] += 1
        else:
            h1[g1[i]] = 1
        if g2[i] in h2:
            h2[g2[i]] += 1
        else:
            h2[g2[i]] = 1
        if g1[i] == g2[i]:
            if g1[i] in rd:
                rd[g1[i]] += 1
            else:
                rd[g1[i]] = 1
            r += 1
    for i in range(6):
        if g1[i] in g2 and g1[i] not in v:
            w += min(h1[g1[i]], h2[g1[i]])
            if g1[i] in rd:
                w -= rd[g1[i]]
            v.add(g1[i])
    return [r, w]


# Run the game
def game():
    sett2 = list(sett)
    sett2.remove(None)
    sett3 = {None}
    wrong = {}
    used = 1
    while sett:
        guess = input("type the wrong guess: ")
        red = input("type the number of red: ")
        white = input("type the number of white: ")
        code = [int(red), int(white)]
        wrong[guess] = code
        print("Guess is", guess, wrong[guess][0], "Red,", wrong[guess][1], "White.")
        for t in sett:
            if t not in sett3 and t != None:
                for i in wrong:
                    arr = judge(i, t)
                    if arr != wrong[i]:
                        sett2.remove(t)
                        sett3.add(t)
                        break
        print(sett2)
        used += 1
    return sett2


game()
