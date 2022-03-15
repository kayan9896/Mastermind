code0 = input()
sett = {None}
co = ["A", "B", "C", "D", "E", "F", "G"]

# Recursively generate all possible codes
def gen(c, s, cur):
    if len(c) == 4:
        s.add(c)
        return
    for i in range(cur, cur + 7):
        if co[i % 7] not in c:
            tmp = c + co[i % 7]
            gen(tmp, s, (i + 1) % 7)
    return


gen("", sett, 0)

# Compare two codes and return the result
def judge(g1, g2):
    r = 0
    w = 0
    for i in range(4):
        if g1[i] in g2:
            if g1[i] == g2[i]:
                r += 1
            else:
                w += 1
    return [r, w]

# Run the game with the first guess and the input code
def game(guess, code):
    sett2 = list(sett)
    # Explanation: wrong includes the wrong guesses with their displayed result
    wrong = {}
    used = 1
    # Explanation: when the current guess is not the answer, it finds a new guess
    while guess != code:
        # Explanation: the current guess is added to the wrong guesses with its result returned from judge function
        wrong[guess] = judge(guess, code)
        print("Guess is", guess, wrong[guess][0], "Red,", wrong[guess][1], "White.")
        # Explanation: it keeps eliminating impossible guesses from the set until it finds a possible one
        while 1:
            # Get a code from the set
            t = sett2.pop()
            if t == None:
                t = sett2.pop()
            # Explanation: f is a flag. 1 represents a possible guess is found and exit the loop.
            # -1 means t cannot be the answer and the loop should continue
            f = 1
            # Explanation: Traverse each wrong guess and compare the result.
            # Assumed that t is the answer, the result of comparing t with each wrong guess (X Red, Y White)
            # should be the same as the result stored in wrong[i]
            # If not, f will become -1 and stop traversing the wrong guesses. It will get another code from the set and try again.

            for i in wrong:
                arr = judge(i, t)
                if arr != wrong[i]:
                    f = -1
                    break
            # When a possible code is found, it exits the inner while loop and uses this code for the next guess.
            if f == 1:
                guess = t
                break
        used += 1
    print("The answer is", guess)
    print(used, "guesses are used\n")
    return used


if code0 not in sett:
    print("Invalid code\n")
else:
    print(game("ABCD", code0))

mx = 0
mn = 840
ct = 0
k = 0
for i in sett:
    if i != None:
        ct += 1
        sc = game("ABCD", i)
        mx = max(mx, sc)
        mn = min(mn, sc)
        k += sc
avg = k / ct
print(ct, "cases are tested")
print(mn, "is the minimum number of guesses")
print(avg, "is the average number of guesses")
print(mx, "is the maximum number of guesses")
