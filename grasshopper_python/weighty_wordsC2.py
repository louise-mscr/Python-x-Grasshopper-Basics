import rhinoscriptsyntax as rs
from Grasshopper.Kernel.Data import GH_Path
import ghpythonlib.components as ghc

# x is in data access, Type hint= int

# To try:
# https://developer.rhino3d.com/guides/rhinopython/grasshopper-datatrees-and-python/


def circles_words(*args):
    b = []
    for list_words in args:
        a = [list(a) for a in x.Branches] #data tree into nested lists (to access index of lists)
        for i in a:
            ind = a.index(i)
            for iol in range(len(i)):
                circle = rs.AddCircle((iol*10,ind*20,0),i[iol])
                b.append(circle)

circles_words(x)