def descending_order(num):
    tab = [int(x) for x in str(num)]
    tab.sort(reverse=True)
    result = ''
    for x in tab:
        result = result + str(x)
    return int(result)
	
try:
    from solution import Descending_Order as descending_order
except ImportError:
    from solution import descending_order

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(descending_order(0), 0)
        test.assert_equals(descending_order(15), 51)
        test.assert_equals(descending_order(123456789), 987654321)