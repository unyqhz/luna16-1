import pandas as pd
for folderNumber in xrange(10):
    print("*"*100)
    print(folderNumber)
    train0 = pd.read_csv("CSVFILES/subset"+str(folderNumber)+"/candidatesClass0Train.csv")
    train1 = pd.read_csv("CSVFILES/subset"+str(folderNumber)+"/candidatesClass1Train.csv")
    test0 = pd.read_csv("CSVFILES/subset"+str(folderNumber)+"/candidatesClass0Test.csv")
    test1 = pd.read_csv("CSVFILES/subset"+str(folderNumber)+"/candidatesClass1Test.csv")
    testFull = pd.read_csv("CSVFILES/subset"+str(folderNumber)+"/candidatesTest.csv")
    for data in [train0,train1,test0,test1,testFull]:
        subsetValue = data.seriesuidFullPath.apply(lambda x: x.split("/")[4])
        print(subsetValue.value_counts())

