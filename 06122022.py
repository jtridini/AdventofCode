def tuner(file,noOfCharacters):
    with open(file) as f:
        signal = f.readline()
    for i in range(len(signal)-noOfCharacters-1):
            marker = signal[i:i+noOfCharacters]
            if len(set(marker)) == noOfCharacters:
                print(i + noOfCharacters)
                break

filePath = r'C:\Users\Jake\Documents\06122022-DataSteam.txt'
tuner(filePath,4)
tuner(filePath,14)