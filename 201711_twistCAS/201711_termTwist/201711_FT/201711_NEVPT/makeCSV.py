
import glob, re, csv

fullDict = {}

basisFile = ['ccpVDZ', 'ccpVTZ', 'augccpVDZ', 'augccpVTZ']
basisString = ['cc-pVDZ', 'cc-pVTZ', 'aug-cc-pVDZ', 'aug-cc-pVTZ']
basisDict = {}
for bas in basisString:
    basisDict[bas] = {}
for fol in glob.iglob("D*"):
    fullDict[fol] = basisDict.copy()
    for fol2 in fullDict[fol].keys():
        fullDict[fol][fol2] = [-1 for x in range(12)]
    endLoop = True
    for g in glob.glob(fol + '//*.out'):
        fileName = g.split("_")
        for isBas in fileName:
            if isBas in basisFile:
                basis = basisString[basisFile.index(isBas)]
                endLoop = False
        if endLoop:
            continue

        number = int(re.search(r'\d+', g.split("_")[-1]).group(0))
        with open(g, 'r') as myfile:
            data = 'None'
            for ln in myfile:
                if ln.startswith("Corrected WF-in-DFT"):
                    data = ln

        for num in data.split():
            try:
                storeNum = float(num)
            except ValueError as e:
                storeNum = 'None'
                pass

        fullDict[fol][basis][number-1] = storeNum


print fullDict


#Make CSV from the Dictionary of Data.
seperator = ['','','','','','','','','','','','','','','','','']
def makeMoleculeLists(molDict):
    basisString = ['cc-pVDZ', 'cc-pVTZ', 'aug-cc-pVDZ', 'aug-cc-pVTZ']
    rtnArray = [[]]
    for i in range(12):
        rtnList = [i + 1]
        for bas in basisString:
            val = molDict[bas][i]
            if val != -1:
                rtnList.append(val)
            else:
                rtnList.append('None')
        rtnArray.insert(i, rtnList)
    
    return rtnArray

headerVal = [''] + basisString

with open('data.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for molName in sorted(fullDict.keys(), key=lambda x: int(x[1:])):
        writer.writerow([molName.split("_")[-1]])
        writer.writerow(headerVal)
        rtnArray = makeMoleculeLists(fullDict[molName])
        for rList in rtnArray:
            writer.writerow(rList)
        

