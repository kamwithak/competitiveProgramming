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
def meeting(s):
    s = s.upper().split(';')
    arr = []
    
    for i in s:
        i = i.split(':')
        arr.append(f'({i[1]}, {i[0]})')
    arr.sort()

    output = ''
    for j in arr:
        output += j
    return output

if __name__ == "__main__":
    s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
    print(meeting(s))