def palindrome1(word):
    list1 = []
    for i in word:
        list1.append(i)
    list2 = []
    for j in word[::-1]:
        list2.append(j)
    if list1 == list2:
        return True
    else:
        return False

def palindrome2(word):
    return True if word == word[::-1] else False

print(palindrome1('лепсспел'))
print(palindrome1('абвг'))
print(palindrome2('лепсспел'))
print(palindrome2('абвг'))