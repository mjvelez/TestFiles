def PigLatin():
    pyg = "ay"
    print "Please Enter a word... Or else.....:"
    ordway = raw_input("ickpay ouryay ordsway: ")
    if len(ordway) > 0:
        if ordway.isalpha():
            First = ordway[0].lower()
            Translation = ordway + First + pyg
            Translation = Translation[1:]
            print Translation
        else:
            print "Only use Letters, por fa please!"
            PigLatin()
    else:
        print "You need to enter a word.... You sloppy English Caniggit!"
        PigLatin()
PigLatin()