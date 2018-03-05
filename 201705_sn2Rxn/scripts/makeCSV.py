
import glob, re, csv

fullDict = {}

basisFile = ['321g', '6311g', 'ccpVDZ', 'ccpVTZ', 'augccpVDZ']
basisString = ['3-21g', '6-311g', 'cc-pVDZ', 'cc-pVTZ', 'aug-cc-pVDZ']
basisDict = {}
for bas in basisString:
    basisDict[bas] = {}
for fol in glob.iglob("*ane"):
    fullDict[fol] = basisDict.copy()
    for fol2 in fullDict[fol].keys():
        fullDict[fol][fol2] = {"reactant":[-1 for x in range(10)], "transition state":[-1 for x in range(10)]}
    r = re.compile("(.*)freezeAndThaw")
    for f in filter(r.match, glob.glob(fol + '//*react*//*')):
        endLoop = True
        for g in glob.glob(f + '//*.out'):
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

            fullDict[fol][basis]["reactant"][number-1] = storeNum

    for f in filter(r.match, glob.glob(fol + '//*trans*//*')):
        for g in glob.glob(f + '//*.out'):
            endLoop = True
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

            fullDict[fol][basis]["transition state"][number-1] = storeNum

#Make CSV from the Dictionary of Data.
seperator = ['','','','','','','','','','','','','','','','','']
def makeMoleculeLists(molDict):
    basisString = ['3-21g', '6-311g', 'cc-pVDZ', 'cc-pVTZ', 'aug-cc-pVDZ']
    rtnArray = [[]]
    for i in range(10):
        rtnList = [i + 1]
        for bas in basisString:
            valReact = molDict[bas]["reactant"][i]
            valTrans = molDict[bas]["transition state"][i]
            if valReact != -1:
                rtnList.append(valReact)
            else:
                rtnList.append('None')
            if valTrans != -1:
                rtnList.append(valTrans)
            else:
                rtnList.append('None')
        rtnArray.insert(i, rtnList)
    
    return rtnArray

headerVal2 = ["reactant", "transition state"] * len(basisString)
headerVal2.insert(0,'')
headerVal = []
break1 = True
while break1:
    try:
        headerVal.append(seperator.pop(0))
    except IndexError:
        break1 = False

    try:
        headerVal.append(basisString.pop(0))
    except IndexError:
        pass

with open('data.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for molName in fullDict.keys():
        writer.writerow([molName.split("_")[-1]])
        writer.writerow(headerVal)
        writer.writerow(headerVal2)
        rtnArray = makeMoleculeLists(fullDict[molName])
        for rList in rtnArray:
            writer.writerow(rList)
        

