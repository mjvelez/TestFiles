def PigLatin():
    print "Please Enter a word... Or else.....:"
    ordway = raw_input("ickpay ouryay ordsway")
    if len(ordway) > 0:
        if ordway.isalpha():
            print "Clean"
        else:
            print "Only use Letters, por fa please!"
            PigLatin()
    else:
        print "You need to enter a word.... You sloppy English Caniggit!"
        PigLatin()
PigLatin()