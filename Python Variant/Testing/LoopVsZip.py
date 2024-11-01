class ListVsLoop:

    def appendViaList(names, ages):

        names_ages = []
    
        for i in range(len(names)):
    
            names_ages.append((names[i], ages[i]))

        print(names_ages)

    def appendViaZip(names, ages):

        names_ages_zip = list(zip(names, ages))

        print(names_ages_zip)



ListVsLoop.appendViaList(['Billy','Bobby'], [1,2])

ListVsLoop.appendViaZip(['Billy','Bobby'], [1,2])