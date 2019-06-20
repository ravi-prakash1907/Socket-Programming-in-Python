# pickle example i.e. serialization

import pickle

exDict = {1:"A", 2:"B", 3:"C"}

#creating pickle
def writeData():
    pickleOut = open("exDict.pickle", "wb")
    pickle.dump(exDict, pickleOut)
    pickleOut.close()
    print("Written Successfully!!")

#loading pickle
def readData():
    pickleIn = open("exDict.pickle", "rb")
    pickleDict = pickle.load(pickleIn)

    print(pickleDict)
    print(pickleDict[3])

writeData()
readData()


'''

    1. Objacts can be pickled
    2. Pickles don't ensure the security
    3. Can be helpful to send or recieve the data/objects through sockets

'''
