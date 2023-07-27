w = int(input())
def wer(w):
    if w == 2:
        return "NO"
    if w % 2 == 0:
        return "YES"
    return "NO"
print(wer(w))