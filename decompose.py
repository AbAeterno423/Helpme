# lectura de archvos y carga de datos
fileName = '/home/zodiac/Downloads/prpk_ind4.txt'
fileHandler = open(fileName, 'r')
clusterDict = {}

for line in fileHandler:
    line = line.strip('\n').strip('\r').split(',')

    clusterKey = line[-1]
    clusterData = [int(line[0])] + [float(data) for data in line[1:-1]]

    if clusterKey not in clusterDict.keys():
        clusterDict.update({clusterKey: []})

    clusterDict[clusterKey].append(clusterData)

fileHandler.close()

# escritura de archvos
baseFileName = 'prpk_ind4_cl{0:}_{1:}.txt'
availableClusters = len(clusterDict.keys())

for ID, clusterKey in enumerate(clusterDict.keys()):
    clusterFileName = baseFileName.format(ID, availableClusters)
    clusterFileHandler = open(clusterFileName, 'w')

    for Ind, dataArray in enumerate(clusterDict[clusterKey]):
        dataText = ('{:>8d}' + '{:>10d}' + (len(dataArray) - 1)*'{:>12.3f}' + '\n').format(Ind, *dataArray)
        clusterFileHandler.write(dataText)

    clusterFileHandler.close()
