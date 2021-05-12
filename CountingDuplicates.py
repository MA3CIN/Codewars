from collections import Counter
def duplicate_count(text):
    wynik = 0
    dict = Counter(text.lower())
    for key, value in dict.items():
        if value > 1:
            wynik += 1
    return wynik
     
	 
import codewars_test as test
from solution import duplicate_count

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(duplicate_count(""), 0)
        test.assert_equals(duplicate_count("abcde"), 0)
        test.assert_equals(duplicate_count("abcdeaa"), 1)
        test.assert_equals(duplicate_count("abcdeaB"), 2)
        test.assert_equals(duplicate_count("Indivisibilities"), 2)