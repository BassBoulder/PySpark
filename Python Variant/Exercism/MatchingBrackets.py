def is_paired(input_string):

    if input_string is None:
        return False

    collected = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in input_string:
        
        if char in bracket_map.values():
            collected.append(char)
            
        elif char in bracket_map.keys():
            if not collected or collected[-1] != bracket_map[char]:
                
                return False
                
            collected.pop()

    return len(collected) == 0