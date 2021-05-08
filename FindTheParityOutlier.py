def find_outlier(integers):
    if ((integers[0]%2) == 0) and ((integers[1]%2) == 0) or ((integers[0]%2) == 0) and ((integers[2]%2) == 0) or ((integers[2]%2) == 0) and ((integers[1]%2) == 0):
        for x in integers:
            if (x%2 ==1):
                return x
    else:
        for x in integers:
            if (x%2 ==0):
                return x

test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)