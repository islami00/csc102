array = [1, 2, 3, 4, 5, 6]

# print("even Numbers", "\tOdd Numbers")
for element in array:
    # number test
    ev = 0
    od = 0
    if (element % 2) == 0:
        ev += 1
    else:
        od += 1
    evi = 0
    odi = 0
    evonly = False
    odonly = False
    evandodd = False
    evinonly = False
    odinonly = False
    evinandod = False
    # digit test
    for c in str(element):
        if (int(c) % 2) == 0:
            evi += 1
        else:
            odi += 1

    # print number test
    if (ev > 0) and (od == 0):
        evonly = True
        print("\t", element, "digits evenonly:", evonly)
    elif (ev == 0) and (od > 0):
        odonly = True
        print("\t", element, "digits oddonly:", odonly)
    else:
        evandodd = True
        print("\t", element, "digits even and odd:", evandodd)
    # print digit test

    if (evi > 0) and (odi == 0):
        evinonly = True
        print("\t", element, "digits evenonly:", evinonly)
    elif (evi == 0) and (odi > 0):
        odinonly = True
        print("\t", element, "digits oddonly:", odinonly)
    else:
        evinandod = True
        print("\t", element, "digits even and odd:", evinandod)
