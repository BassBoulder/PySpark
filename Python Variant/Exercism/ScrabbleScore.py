def score(word):

    result = 0;
    
    for char in word.upper(): 
        
        match char :
            case 'A' | 'E' | 'I' | 'O' | 'U' | 'L' | 'N' | 'R' | 'S' | 'T':
                result += 1;
        
            case 'D' | 'G':
                result += 2;
        
            case 'B' | 'C' | 'M' | 'P':
                result += 3;
        
            case 'F' | 'H' | 'V' | 'W' | 'Y':
                result += 4;
        
            case 'K':
                result += 5;
        
            case 'J' | 'X':
                result += 8;
        
            case 'Q' | 'Z':
                result += 10;
            
    return result;