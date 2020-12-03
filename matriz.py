# To know the direction you're facing at the end, count the turning points
# You will turn right at every point in which the distance between the nearest
# vertical boder is the same than the neares horizontal border. Except when the point is on 
# the top left part of the matrix, in which case, you will turn if the distance to the top border is the same
# as the distance to the left border plus 1 (this is true for a starting point in the top left corner).
# Then we just count the turning points and return the direction at the end based on the result

def isTurningPont(n,m,i,j):
    # Take the minimun between (j and m-1-j) and (i and n-1-i)
    # if j and i are themselves the minima, then the point is
    # on the top left part of the matrix, so we compare j and i-1.
    # Otherwise we compare both minima. Whichever the case, if the results are equals
    # this is a turning point (so we can turn right).

    auxJ = j
    auxI = i
    distanceToBorderH = min(auxI, n-1-auxI)
    distancetoBorderV = min(auxJ, m-1-auxJ)
    if(distanceToBorderH == auxI and distancetoBorderV == auxJ):
        distanceToBorderH-=1
    return distanceToBorderH == distancetoBorderV #This function also treats the final point as a turning point


def getNumberOfTurningPoints(n,m):
    turningPoints = 0
    for i in range(n):
        for j in range(m):
            #iterate every point to find out how many turning points there are
            if(isTurningPont(n,m,i,j)):
                turningPoints+=1
    return turningPoints

def getDirectionAtEndWalk(n,m):
    if(n == m and n%2):
        #Square odd matrices always end right
        return "R"
    turningPoints = getNumberOfTurningPoints(n,m) - 1 # We don't turn on the final point 
    if(turningPoints%4 == 0):
        return "R"
    if(turningPoints%4 == 1):
        return "D"
    if(turningPoints%4 == 2):
        return "L"
    return "U"