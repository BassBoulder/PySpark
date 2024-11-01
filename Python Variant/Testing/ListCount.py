student_scores = [10,40,41,100]
  
def failPass(student_scores):

    i = 0
    
    for value in student_scores:
        if value < 40:
            i += 1
        
    return i


print(failPass(student_scores))