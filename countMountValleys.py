def countingValleys(steps, path):
    # steps - numbers of steps taken on hike
    # path - record of hike, e.g., [DUUDD]
    # A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
    numVal = 0
    numMount = 0 # why not count mountains too
    elev = 0
    tempPath = [] # record our path through the mountain or valley
    
    for step in path:
        if (step == 'D'):
            elev -= 1
            tempPath.append(step)
        elif (step == 'U'):
            elev += 1
            tempPath.append(step)
        if ((len(tempPath) > 1) and (elev == 0)): # by the book
            if (tempPath[0] == 'D'):
                numVal += 1
            elif (tempPath[0] == 'U'):
                numMount += 1
            tempPath = []
          
    return numVal 