def likes(names):
    
    sentence = ""

    if len(names) == 0:
        sentence = "no one likes this"
        return(sentence)

    elif len(names) == 1:
        sentence = names[0] + " likes this"
        return(sentence)

    elif len(names) == 2:
        sentence = names[0] + " and " + names[1] + " like this"
        return(sentence)
    
    elif len(names) == 3:
        sentence = names[0] + ", " + names[1] + " and " + names[2] + " like this"
        return(sentence)
    else:
        sentence = names[0] + ", " + names[1] + " and " + str(len(names)-2) + " others like this"
        return(sentence)   

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


Test.assert_equals(likes([]), 'no one likes this')
Test.assert_equals(likes(['Peter']), 'Peter likes this')
Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')