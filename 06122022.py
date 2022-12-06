def tuner(file,noOfCharacters):
    with open(file) as f:
        signal = f.readline()
    for i in range(len(signal)-noOfCharacters-1):
            marker = signal[i:i+noOfCharacters]
            if len(set(marker)) < noOfCharacters:
                pass
            else:
                startOfPacketMarker = i+noOfCharacters
                break
    return startOfPacketMarker

filePath = r'C:\Users\Jake\Documents\06122022-DataSteam.txt'
print(tuner(filePath,4))
print(tuner(filePath,14))