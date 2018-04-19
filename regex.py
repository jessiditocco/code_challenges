########################### Without Regex #################################

def is_phone(s):
    """Match phone like 4155551212?
    
        >>> is_phone('4155551212')
        True
        
        >>> is_phone('415ABCDEFG')
        False
    """

    if len(s) == 10 and s.isdigit():
        return True

    return False

def is_phone_dashes(s):
    """Match phone, allowing dashes.
    
        >>> is_phone_dashes('4155551212')
        True
        
        >>> is_phone_dashes('415-555-1212')
        True
    """
    # is digit takes a string.. if all of the 
    # charecters in the string are digits, returns true
    if len(s) == 10 and s.isdigit():
        return True

    if (s[3] == "-" and s[7] == "-" and len(s) == 12 
        and s[0:3].isdigit() and s[4:7].isdigit() 
        and s[8:].isdigit()):

        return True

    return False

def is_phone_dashes_intl(s):
    """Match phone, allowing dashes and leading 1.
    
        >>> is_phone_dashes_intl('14155551212')
        True
        
        >>> is_phone_dashes_intl('1-415-555-1212')
        True
    """

    if s.startswith("1-"):
        s = s[2:]
    elif s.startswith("1"):
        s = s[1:]

    if len(s) == 10 and s.isdigit():
        return True

    if (s[3] == "-" and s[7] == "-" 
        and len(s) == 12 and s[0:3].isdigit()
        and s[4:7].isdigit() and s[8:].isdigit()):

        return True

    return False

########################### With Regex #################################
import re

# match_obj = re.search(r"[0-9]+", "a 123 b")   # note r"pattern"

# if match_obj:             # None if no match!

#     print match_obj.start()     # Index position in string == 2
#     print match_obj.end()       # Index position in string == 5
#     print match_obj.group()     # "123"


email = "jessica@hackbrightacademy.com"
match_obj = re.search(r"(\w+)\@(\w+\.com)", email)

print match_obj.group() # jessica@hackbrightacademy.com
print match_obj.group(1) # jessica
print match_obj.group(2) # hackbrightacademy.com




########################### Doctest #################################

# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print "All tests passed"