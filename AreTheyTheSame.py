def comp(array1, array2):
    print(array1)
    print(array2)
    if (type(array2)!=list or type(array1)!=list):
        return False
    if (len(array1)==0 and len(array2)==0):
        return True
    array1 = sorted(array1, key=abs)
    array2 = sorted(array2, key=abs)
    if (len(array1)!=(len(array2))):
        return False
    else:
        for i in range (0, len(array1)):
            if ((array1[i]*array1[i])!=array2[i]):
                return False
    return True
	

import codewars_test as test
    
@test.describe("Same")
def tests():
    @test.it("Fixed tests")
    def basics():
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        test.assert_equals(comp(a1, a2), True)
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        test.assert_equals(comp(a1, a2), False)
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
        test.assert_equals(comp(a1, a2), False)