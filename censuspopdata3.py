import os
import censuspopdata2

censuspopdata2.alldata["AL"]["Baldwin"]
baldwinPop = censuspopdata2.alldata["AL"]["Baldwin"]["pop"]
print("The 2010 population of Baldwin was " + str(baldwinPop))