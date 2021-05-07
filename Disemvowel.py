def disemvowel(string_):
    vowels = ('a','e','i','o','u')
    for letter in string_:
        if letter.lower() in vowels:
            string_ = string_.replace(letter,"")
        
    return string_
	
@test.describe("Fixed Tests")
def basic_tests():
    test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")