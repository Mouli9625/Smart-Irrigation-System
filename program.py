
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import rainbow

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets, linear_model
from sklearn.metrics import accuracy_score, make_scorer
import serial
import numpy as np
from sklearn.preprocessing import StandardScaler
import time
time.sleep(2)

# Open the serial port
ser = serial.Serial('COM7', 9600)

# Create a scaler to preprocess the data
scaler = StandardScaler()

def takeInput():
    
    while True:
        # Read data from the serial port
        data = ser.readline().decode().strip()
        print(data)
        
        # Preprocess the data
##        print('Enter folloing')
##        print()
##        v=input('TEMP:')
##        x=input('HUMD:')
##        y=input('RAIN:')
##        z=input('MOI:')
##       
##        print('')
##        data=str(v)+','+str(x)+','+str(y)+','+str(z)
##        
        if(data is not None):
            X = np.array([data.split(',')], dtype=np.float32)
            #X = scaler.transform(X)
            print(X)
            # Make a prediction
            y_pred = regr.predict(X)
           
            print(y_pred)
            
            if y_pred == 1:
                print('Pump On')
                ser.write("1".encode())
            elif y_pred == 0:
                print('Pump off')
                ser.write("2".encode())
           
            
        
data = pd.read_csv("mydata.csv")
y = data['Result']
X = data.drop(['Result'], axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)
knn_classifier = KNeighborsClassifier(n_neighbors = 4)
knn_classifier.fit(X_train, y_train)


knn_preds = knn_classifier.predict(X_test)
knn_acc = accuracy_score(y_test, knn_preds)
print("Accuracy with KNN: ", accuracy_score(y_test, knn_preds))


svc_clf = SVC(gamma='scale')
svc_clf.fit(X_train,y_train)
svc_preds = svc_clf.predict(X_test)
svc_acc = accuracy_score(y_test, svc_preds)
print("Accuracy with SVC: ", accuracy_score(y_test, svc_preds))

regr = LogisticRegression(solver="liblinear").fit(X_train,y_train)
regr_preds = regr.predict(X_test)
regr_acc = accuracy_score(y_test, regr_preds)
print("Accuracy with LR: ", accuracy_score(y_test, svc_preds))


from sklearn.metrics import accuracy_score, precision_score
import matplotlib.pyplot as plt
import numpy as np

# Generate some random binary classification data
y_true = np.random.randint(0, 2, size=100)
y_pred = np.random.randint(0, 2, size=100)

# Calculate accuracy and precision for different threshold values
thresholds = np.linspace(0, 1, num=101)
accuracy = []
precision = []
for t in thresholds:
    y_pred_t = (y_pred >= t).astype(int)
    accuracy.append(accuracy_score(y_true, y_pred_t))
    precision.append(precision_score(y_true, y_pred_t))



from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

# Generate some random binary classification data
y_true = np.random.randint(0, 2, size=100)
y_pred = np.random.randint(0, 2, size=100)

# Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Plot confusion matrix
plt.imshow(cm, cmap=plt.cm.Blues)
plt.colorbar()
plt.title('Confusion Matrix')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.xticks(np.arange(2), ('Negative', 'Positive'))
plt.yticks(np.arange(2), ('Negative', 'Positive'))
plt.show()

# Plot accuracy-precision curve
plt.plot(precision, accuracy)
plt.xlabel('Precision')
plt.ylabel('Accuracy')
plt.title('Accuracy-Precision Curve')
plt.show()
takeInput()
 
