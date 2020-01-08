import numpy as np
import operator

##給出訓練資料以及對應的類別
def create_dataset():
    group = np.array([[1.0, 2.0], [1.2, 0.1],
                      [0.1, 1.4], [0.3, 3.5]])
    labels = ['A','A','B','B']
    return group, labels

##通過KNN進行分類
def classify(input, dataSet, label, k):
    dataSize = dataSet.shape[0]
    ## 重複input為dataSet的大小
    diff = np.tile(input, (dataSize, 1)) - dataSet
    sqdiff = diff**2
    ## 列向量分別相加，得到一列新的向量
    squareDist = np.array([sum(x) for x in sqdiff])
    dist = squareDist**0.5
    
    ## 對距離進行排序
    ## argsort()根據元素的值從大到小對元素進行排序，返回下標
    sortedDistIndex = np.argsort(dist)
    
    classCount = {}
    for i in range(k):
        ## 因為已經對距離進行排序，所以直接迴圈sortedDistIndx
        voteLabel = label[sortedDistIndex[i]]
        ## 對選取的k個樣本所屬的類別個數進行統計
        ## 如果獲取的標籤不在classCount中，返回0
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    ## 選取出現的類別次數最多的類別
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key
    
    return classes

data, labels = create_dataset()
input = [1.0, 2.0]
print(classify(input,data,labels,2))