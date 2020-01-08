import pickle

path_list = [
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_16-52-32.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_16-57-35.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_16-59-11.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-01-02.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-02-45.pickle",
        
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-04-36.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-08-02.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-11-29.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-13-12.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-15-11.pickle",
        
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-18-31.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-20-22.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-22-18.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-25-37.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-28-49.pickle",
                                                                                           
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-32-08.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-33-59.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-35-42.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-37-33.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-39-16.pickle",
                                                                                           
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-42-28.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-45-42.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-47-33.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-49-16.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-52-36.pickle",
                                                                                           
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_17-55-56.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_18-12-12.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_18-15-25.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_18-17-16.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_18-18-59.pickle",
                                                                                           
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_18-20-50.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_22-33-36.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_22-35-30.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_22-37-16.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_22-40-42.pickle",
                                                                                           
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_22-44-01.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_22-48-12.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_23-23-41.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_23-25-28.pickle",
        "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_23-27-23.pickle"

        
        ]
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-00-33.pickle",
  #     
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-03-07.pickle",
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-04-11.pickle",
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-05-02.pickle",
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-05-57.pickle",
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-06-49.pickle",
  #     
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-07-43.pickle",
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-08-43.pickle",
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-09-36.pickle",
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-10-36.pickle",
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-11-27.pickle",
  #     
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-12-27.pickle",
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-13-21.pickle",
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-14-13.pickle",
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-15-09.pickle",
  #     "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-18_15-16-01.pickle"
          

#for flie_list in path_list :
#    with open(flie_list,"rb") as f :
#        data_list = pickle.load(f)
#
#
#    Frame = []
#    Status = []
#    Ballposition = []
#    PlatformPosition_1P = []
#    for i in range(0,len(data_list)):
#        Frame.append(data_list[i].frame)
#        Status.append(data_list[i].status)
#        Ballposition.append(data_list[i].ball)
#        PlatformPosition_1P.append(data_list[i].platform_1P)
#        PlatformPosition_2P.append(data_list[i].platform_2P)


for flie_list in path_list :
    with open(flie_list,"rb") as f :
        data_list = pickle.load(f)


    Frame = []
    Status = []
    Ballposition = []
    PlatformPosition_1P = []
    for i in range(0,len(data_list)):
        Frame.append(data_list[i].frame)
        Status.append(data_list[i].status)
        Ballposition.append(data_list[i].ball)
        PlatformPosition_1P.append(data_list[i].platform_1P)





import numpy as np
np.set_printoptions(threshold=np.inf)
PlatX = np.array(PlatformPosition_1P)[:,0][:,np.newaxis]
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

filename = "C:\\Users\\B510\\Desktop\\MLGame-master\\games\\pingpong\\ml\\knn_1P.sav"
pickle.dump(knn , open(filename,'wb'))


# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# scaler.fit(x_train)
# x_train_stdnorm = scaler.transform(x_train)
# knn.fit(x_train_stdnorm , y_train)
# x_test_stdnorm = scaler.transform(x_test)
# yknn_aft_scaler = knn.predict(x_test_stdnorm)#svm
# acc_knn_aft_scaler = accuracy_score(yknn_aft_scaler,y_test)

