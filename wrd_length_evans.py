wrd = input = ("Enter some word")
wrd = str(wrd)

check = len(wrd)
if (check >= 10):
    print("That is a really long word!")
if (check <= 9) and (check >= 5):
    print("That is a somewhat long word...")
if (check <= 4):
    print("That is one short word!")
else:
    ("Hmmm, try again, the computer doesn't like your word.")
    
