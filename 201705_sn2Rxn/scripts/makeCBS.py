
import glob, re, csv

fullDict = {}

basisFile = ['ccpVDZ', 'ccpVTZ']
basisString = ['cc-pVDZ', 'cc-pVTZ']
basisDict = {}
for bas in basisString:
    basisDict[bas] = {}
for fol in glob.iglob("*[ue]*ane"):
    fullDict[fol] = basisDict.copy()
    for fol2 in fullDict[fol].keys():
        fullDict[fol][fol2] = {"reactant hfindft":[-1 for x in range(10)], "reactant corr":[-1 for x in range(10)], "transition state hfindft":[-1 for x in range(10)], "transition state corr":[-1 for x in range(10)]}
    r = re.compile("(.*)freezeAndThaw")
    for f in filter(r.match, glob.glob(fol + '//*react*//*')):
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
                    if ln.startswith("CCSD(T) Correlation"):
                        corrData = ln
                    if ln.startswith("Corrected WF-in-DFT"):
                        fulldata = ln

            for num in fulldata.split():
                try:
                    wfindft = float(num)
                except ValueError as e:
                    wfindft = 0
                    pass

            for num in corrData.split():
                try:
                    wfcorr = float(num)
                except ValueError as e:
                    wfcorr = 0
                    pass

            hfindft = wfindft-wfcorr
            fullDict[fol][basis]["reactant hfindft"][number-1] = hfindft
            fullDict[fol][basis]["reactant corr"][number-1] = wfcorr


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
                    if ln.startswith("CCSD(T) Correlation"):
                        corrData = ln
                    if ln.startswith("Corrected WF-in-DFT"):
                        fulldata = ln

            for num in fulldata.split():
                try:
                    wfindft = float(num)
                except ValueError as e:
                    wfindft = 0
                    pass

            for num in corrData.split():
                try:
                    wfcorr = float(num)
                except ValueError as e:
                    wfcorr = 0
                    pass

            hfindft = wfindft-wfcorr
            fullDict[fol][basis]["transition state hfindft"][number-1] = hfindft
            fullDict[fol][basis]["transition state corr"][number-1] = wfcorr


#Make CSV from the Dictionary of Data.
seperator = ['','','','','','','','','','','','','','','','','']
def makeMoleculeLists(molDict):
    basisString = ['cc-pVDZ', 'cc-pVTZ']
    rtnArray = [[]]
    for i in range(10):
        rtnList = [i + 1]
        for bas in basisString:
            valreacthfindft = molDict[bas]["reactant hfindft"][i]
            valreactwfcorr = molDict[bas]["reactant corr"][i]
            valtranshfindft = molDict[bas]["transition state hfindft"][i]
            valtranswfcorr = molDict[bas]["transition state corr"][i]
            rtnList.append(valreacthfindft)
            rtnList.append(valreactwfcorr)
            rtnList.append(valtranshfindft)
            rtnList.append(valtranswfcorr)
        rtnArray.insert(i, rtnList)
    
    return rtnArray

headerVal2 = ["reactant hf-in-dft", "reactant corr" , "transition state hf-in-dft", "transiton state corr"] * len(basisString)
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

with open('data_cbs.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for molName in fullDict.keys():
        writer.writerow([molName.split("_")[-1]])
        writer.writerow(headerVal)
        writer.writerow(headerVal2)
        rtnArray = makeMoleculeLists(fullDict[molName])
        for rList in rtnArray:
            writer.writerow(rList)
        
