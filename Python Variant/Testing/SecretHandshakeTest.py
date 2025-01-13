def commands(binary_str):
    length_of_binary_str = len(binary_str)-1
    commands_array = []

    if binary_str[length_of_binary_str] == '1':
        commands_array.append('wink')
    
    if binary_str[length_of_binary_str-1] == '1':
        commands_array.append('double blink')

    if binary_str[length_of_binary_str-2] == '1':
        commands_array.append('close your eyes')

    if binary_str[length_of_binary_str-3] == '1':
        commands_array.append('jump')

    if binary_str[length_of_binary_str-4] == '1':
        commands_array.reverse()

    return commands_array


print(commands("11001"))
