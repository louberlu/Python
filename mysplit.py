def mysplit(strng):
    mylist = []
    mych = ""
    for ch in strng:
        if ch == " ":
            if mych != "":
                mylist.append(mych)
                mych = ""
        else:
            mych += ch
    else:
        if mych != "":
                mylist.append(mych)
                mych = ""
    return mylist


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
    