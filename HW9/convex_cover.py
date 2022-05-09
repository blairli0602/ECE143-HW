"""
Given a irregular, closed, convex polygon
P with n−1 sides and m circle-centers {(xi,yi)}mi contained within that polygon, compute the radii, 0≤ri, of m circles
centered at those m points such that the sum of the areas of the circles is minimized (approximately) and that
any vertex in P is also contained in at least one of the m circles.
Here is the function signature: find_convex_cover(pvertices,clist) where pvertices is a
(n−1)-long iterable of polygon vertices and clist is a list of (xi,yi) tuples of circle-centers.
The output of find_convex_cover is a m long list of radii, ri, corresponding to the m circle-centers.
Example:
->>> pvertices = array([[ 0.573,  0.797],
                        [ 0.688,  0.402],
                        [ 0.747,  0.238],
                        [ 0.802,  0.426],
                        [ 0.757,  0.796],
                        [ 0.589,  0.811]])

 ->>> clist = [(0.7490863467660889, 0.4917635308023209),
              (0.6814339441396109, 0.6199470305156477),
              (0.7241617773773865, 0.6982813914515696),
              (0.6600700275207232, 0.7516911829987891),
              (0.6315848053622062, 0.7730550996176769),
              (0.7348437356868305, 0.41342916986639894),
              (0.7597683050755328, 0.31729154508140384)]

 ->>> find_convex_cover(pvertices,clist) # note some radii == 0
 [0, 0, 0.10297280518543134, 0, 0.06374182913818943, 0.0684588720095565, 0.07987784828713643]

Hints:
m can be very large so use Numpy broadcasting effectively.
For your own understanding, use Matplotlib to visualize the polygons and circles.
Numpy is the only third-party module you can use with this assignment.
Since the n-polygon is closed, the first and last vertices are the same so that only n−1
vertices need be specified.
Your solution can be an approximation to the minimum.
"""

import numpy as np
from collections import defaultdict

def find_convex_cover(pvertices,clist):
    '''
    find_convex_cover
    pvertices
    clist
    '''
    assert isinstance(clist, list)
    for item in clist:
        assert isinstance(item,tuple)
        assert len(item) == 2
        for num in item:
            assert isinstance(num,(int,float))
    for pitem in pvertices:
        assert len(pitem) == 2
        for num in pitem:
            assert isinstance(num,(int,float))

    ver = np.array(pvertices)
    center = np.array(clist)

    r = ver[:, None] - center
    D = np.apply_along_axis(np.linalg.norm, -1, r)

    mins = np.argmin(D, -1)
    radii = defaultdict(int)

    for i, argmin in enumerate(mins):
        radii[argmin] = max(D[i, argmin], radii[argmin])

    result = []
    for i in range(len(center)):
        if i in list(radii.keys()):
            result.append(radii[i])
        else:
            result.append(0)

    return result

pvertices = np.array([[ 0.573,  0.797],
                        [ 0.688,  0.402],
                        [ 0.747,  0.238],
                        [ 0.802,  0.426],
                        [ 0.757,  0.796],
                        [ 0.589,  0.811]])

clist = [(0.7490863467660889, 0.4917635308023209),
              (0.6814339441396109, 0.6199470305156477),
              (0.7241617773773865, 0.6982813914515696),
              (0.6600700275207232, 0.7516911829987891),
              (0.6315848053622062, 0.7730550996176769),
              (0.7348437356868305, 0.41342916986639894),
              (0.7597683050755328, 0.31729154508140384)]

result = find_convex_cover(pvertices, clist)

print(result)
