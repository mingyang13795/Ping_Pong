import pickle

path_list = [
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_16-50-55_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_16-54-08_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_16-55-44_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-06-11_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-09-38_2P.pickle",
        
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-16-48_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-23-54_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-27-13_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-30-26_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-40-52_2P.pickle",
        
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-44-06_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-50-53_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-54-13_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_18-10-29_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_18-13-49_2P.pickle",
                                                                                           
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_22-30-18_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_22-31-57_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_22-38-56_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_22-42-21_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_23-30-50_2P.pickle",
                                                                                           
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_23-41-39_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_23-45-06_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_23-50-19_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_23-52-00_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_23-53-19_2P.pickle",
                                                                                           
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_23-55-27_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_23-57-06_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-19_00-06-14_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_22-10-13_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_22-43-10_2P.pickle",
                                                                                           
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_22-44-51_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_22-46-34_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_22-48-15_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_22-55-20_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_23-13-35_2P.pickle",
                                                                                           
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_23-15-16_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_23-16-57_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_23-27-51_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_23-40-50_2P.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-23_23-46-10_2P.pickle"
        ]
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-00-33.pickle",
 #      
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-03-07.pickle",
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-04-11.pickle",
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-05-02.pickle",
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-05-57.pickle",
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-06-49.pickle",
 #      
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-07-43.pickle",
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-08-43.pickle",
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-09-36.pickle",
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-10-36.pickle",
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-11-27.pickle",
 #      
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-12-27.pickle",
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-13-21.pickle",
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-14-13.pickle",
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-15-09.pickle",
 #      "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-16-01.pickle"
          
for flie_list in path_list :
    with open(flie_list,"rb") as f :
        data_list = pickle.load(f)


    Frame = []
    Status = []
    Ballposition = []
    PlatformPosition_2P = []
    for i in range(0,len(data_list)):
        Frame.append(data_list[i].frame)
        Status.append(data_list[i].status)
        Ballposition.append(data_list[i].ball)
        PlatformPosition_2P.append(data_list[i].platform_2P)

import numpy as np
np.set_printoptions(threshold=np.inf)
PlatX = np.array(PlatformPosition_2P)[:,0][:,np.newaxis]
PlatX_next = PlatX[1:,:]
instruct = (PlatX_next - PlatX[0:len(PlatX_next),0][:, np.newaxis])/5

BallX=np.array(Ballposition)[:,0][:,np.newaxis]
BallX_next=BallX[1:,:]
vx=(BallX_next-BallX[0:len(BallX_next),0][:,np.newaxis])

BallY=np.array(Ballposition)[:,1][:,np.newaxis]
BallY_next=BallY[1:,:]
vy=(BallY_next-BallY[0:len(BallY_next),0][:,np.newaxis])

Ballarray = np.array(Ballposition[:-1])

x = np.hstack((Ballarray , PlatX[0:-1,0][:,np.newaxis],vx,vy))
y = instruct

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x , y, test_size = 0.2,random_state = 999)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
knn = KNeighborsClassifier(n_neighbors = 3)

knn.fit(x_train,y_train)

yknn_bef_scaler = knn.predict(x_test)
acc_knn_bef_scaler = accuracy_score(yknn_bef_scaler , y_test)

filename = "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\ml\\knn_2P.sav"
pickle.dump(knn , open(filename,'wb'))
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# scaler.fit(x_train)
# x_train_stdnorm = scaler.transform(x_train)
# knn.fit(x_train_stdnorm , y_train)
# x_test_stdnorm = scaler.transform(x_test)
# yknn_aft_scaler = knn.predict(x_test_stdnorm)#svm
# acc_knn_aft_scaler = accuracy_score(yknn_aft_scaler,y_test)