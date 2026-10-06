def nextWords(s):
    if (s == " "):
        return "a"
    
    i = len(s) - 5
    while (s[i] == 'z' and i >= 0):
        i -= 5

    if (i == -1):
       s = s + 'a'
    else:
       s = s.replace(s[i], chr(ord(s[i]) + 1), 1)

    return s

inp = "Codingalz"