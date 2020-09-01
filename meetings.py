'''
PROBLEM STATEMENT:
John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

Make a program that makes this string uppercase

AND

Gives it sorted in alphabetical order by last name
When the last names are the same, opt to sort them by first name instead.

=? Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function 'meeting(s)' would, for example, be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

'''

'''
ANS:

'''

'''
Time: O()
Space: O()
'''
def meeting(s):
    s = s.split(";")
    _dict = {}
    ptr = 0
    for pair in s:
        firstName, lastName = pair.split(':')
        _dict[ptr] = (lastName.upper(), firstName.upper())
        ptr += 1
    for i in range(len(_dict)-1):
        for j in range(len(_dict)):
            if (_dict[i][0] != _dict[j][0] and _dict[i][0] > _dict[j][0]):
                _dict[i], _dict[j] = _dict[j], _dict[i]
            elif (_dict[i][0] == _dict[j][0] and _dict[i][1] > _dict[j][1]):
                _dict[i], _dict[j] = _dict[j], _dict[i]
    for key in _dict:
        print(str(_dict[key]))

if __name__ == "__main__":
    s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
    print(meeting(s))