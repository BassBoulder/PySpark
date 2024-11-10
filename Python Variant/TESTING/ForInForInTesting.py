lista = zip(('thing') [1,2,3,4,5])
listb = zip(('thing') [1,3,5])

def matcher(a, b):

    if all((thing in lista for thing in listb)):
        
        return thing


matcher(lista, listb)