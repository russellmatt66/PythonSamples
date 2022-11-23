def jumpingOnClouds(c):
    # c is an array of integers representing spaces in a game
    # c[i] = 1 -> not a safe space
    # c[i] = 0 -> safe space, can land
    # Player can choose to move either 1 or 2 spaces
    # Determine minimum number of jumps to win
    thunderHeads = [i for i in range(len(c)) if c[i]]
    curPos = 0
    finalPos = len(c) - 1
    end = 0
    nJumps = 0
    while (not end):
        nJumps += 1
        jumpLen = 2
        nextPos = curPos + jumpLen
        if (nextPos not in thunderHeads): 
            curPos += jumpLen
        else:
            jumpLen = 1
            curPos += jumpLen    
        if curPos >= finalPos:
            end = 1    
    return nJumps