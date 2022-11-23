def sockMerchant(n, ar):
    # Function counts the number of pairs of elements that occur in an input array, ar, of length n.
    basicCount = 0
    basicColors = [] # need the unique colors
    pairSum = 0
    pairCount = []
    
    for sock in ar: # time and space ineff.
        if sock not in basicColors:
            basicCount += 1
            basicColors.append(sock)
            pairCount.append(ar.count(sock))
    
    for item in pairCount:
        item = math.floor(item / 2)
        pairSum += item
    
    return pairSum