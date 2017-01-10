maxGridColumnsByWidth = 1
class thumbnailGridView:
    count = 0

class Math:
    min = min


def calculateColumnCount():
    # respect screenGeometry
    c = Math.min(thumbnailGridView.count, maxGridColumnsByWidth)

    residue = thumbnailGridView.count % c
    if residue == 0:
        gridColumns = c
        return gridColumns

    # start greedy recursion
    gridColumns = columnCountRecursion(c, c, c - residue)
    return gridColumns


# step for greedy algorithm
def columnCountRecursion(prevC, prevBestC, prevDiff):
    c = prevC - 1

    # don't increase vertical extent more than horizontal
    # and don't exceed maxHeight
    if prevC * prevC <= thumbnailGridView.count + prevDiff:
        # Ignored maxHeight check: maxHeight < Math.ceil(thumbnailGridView.count / c) * thumbnailGridView.cellHeight
        return prevBestC
    
    residue = thumbnailGridView.count % c
    # halts algorithm at some point
    if residue == 0:
        return c
    
    # empty slots
    diff = c - residue

    # compare it to previous count of empty slots
    if diff < prevDiff:
        return columnCountRecursion(c, c, diff)
    elif diff == prevDiff:
        # when it's the same try again, we'll stop early enough thanks to the landscape mode condition
        return columnCountRecursion(c, prevBestC, diff)

    # when we've found a local minimum choose this one (greedy)
    return columnCountRecursion(c, prevBestC, diff)


for y in range(1, 30):
    maxGridColumnsByWidth = y
    for x in range(1, 30):
        thumbnailGridView.count = x
        c = calculateColumnCount()
        if not (c == y or x <= y):
            print("{} / {} = {}".format(x, y, c))

