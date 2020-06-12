def balancedOrNot(myStr): 
    stack = [] 
    _map = {')':'(',']':'[','}':'{'}
    for i in myStr: 
        if i in _map.values(): 
            leftParanthesis = i
            stack.append(leftParanthesis)
        elif i in _map.keys():
            rightParanthesis = i 
            associatedLeftParanthesis = _map[rightParanthesis]
            if (len(stack) > 0 and (associatedLeftParanthesis == stack[len(stack) - 1])):
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
    return "Unbalanced"

print(balancedOrNot('{'))