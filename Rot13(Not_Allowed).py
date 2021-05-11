import codecs
def rot13(message):
    return codecs.encode(message, 'rot_13')

test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")