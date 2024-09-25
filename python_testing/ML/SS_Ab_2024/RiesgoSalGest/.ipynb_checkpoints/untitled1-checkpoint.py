# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:50:45 2024

@author: Usuario Asignado
"""


import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, concatenate,Dropout
from tensorflow.keras.models import Model 
from tensorflow.keras.callbacks import ModelCheckpoint
import numpy as np
from tensorflow.keras.utils import plot_model
import pydot
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from tensorflow.keras.utils import to_categorical
import tensorflow.keras




import numpy as np
file_path=r'Base de datos materna.csv'
data=pd.read_csv(file_path,sep=';')

print(data.iloc[0:2,:12])

#separar clases minoritarias###############
data2=data[data['Estado materno']!=0]

#quitar variables no útilies
data2=data2.drop('Fecha',axis=1)
data2=data2.drop('ID',axis=1)

#aumento de datos con valores aleatorios se multiplicará por
#10 veces la cantidad de datos de las clases minoritaria
aumento=10
#filtramos a la salida y de las clases minoritaria
y_a=data2['Estado materno']
y_a=np.array(y_a)
#aumentamos los datos de y 10 veces y se guardan en yb
yb=np.concatenate([y_a]*aumento)

###para las característias x quitamos a las clases target estado materno y 
##estado fetal
data2=data2.drop('Estado materno',axis=1)
data2=data2.drop('Estado fetal',axis=1)

#obtenemos la forma o tamaño en ancho 'F' y alto 'C' de data2 (características x)
F,C=data2.shape
# creamos datos aleatorios con media de 0.2 y desviación estandar (sigma=0.1)
sigma=0.1
mu=0.2
ale=sigma * np.random.randn(aumento*(F),C) + mu

#aumentamos los datos x de las clases minoritarias 10 veces
data2=np.concatenate([data2]*aumento, axis=0)
#aquí añadimos los datos aleatorios para generar datos con diferentes
#valores

data2=data2+ale

#aquí es como estaba el código, esto es para la base de datos completa sin
#modificaciones data

#se dejan solo las características, se quitan targets y variables no útiles
x=data.drop('Estado materno',axis=1)
x=x.drop('Estado fetal',axis=1)
x=x.drop('Fecha',axis=1)
x=x.drop('ID',axis=1)
#se transforma a array
x=np.array(x)

#concatenamos los datos originales con los datos nuevos con ruido aleatorio
x=np.concatenate([x,data2], axis=0)

#se toma la salida o target del dataset original sin alterar y1
y1=data['Estado materno']
y2=data['Estado fetal']

#se convierte en arreglo
y1=np.array(y1)

#aquí concatenamos los targets originales con los targets
#de los datos x con ruido aleatorio
y1=np.concatenate([y1,yb])

#convertimos a y1 a categorical
y1c=to_categorical(y1)

#se hace la división de entrenamiento
x_train,x_test,y_train,y_test=train_test_split(x,y1,test_size=0.2, shuffle=True)

"""print('Entradas: ')
print(x.iloc[0:,:11])
print('  Salidas: ')
print(y.iloc[0:11])"""

#Se estandariza
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.fit_transform(x_test)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)



shape=x_train_scaled.shape[1]
input_layer=Input(shape=(shape,))


#modelo (con algunos ajustes, pueden probar otras configuraciones)
hidden_layer1=Dense(10,activation='sigmoid')(input_layer)
hidden_layer1=tf.keras.layers.Dropout(0.1)(hidden_layer1)
hidden_layer2=Dense(20,activation='sigmoid')(hidden_layer1)
h2=tf.keras.layers.Dropout(0.1)(hidden_layer2)
h2=Dense(10,activation='sigmoid')(h2)
outputlayer=Dense(3,activation='softmax')(h2)


model=Model(inputs=input_layer,outputs=outputlayer)


#esto de aquí es para balancear las clases
from sklearn.utils.class_weight import compute_class_weight
#usamos a y1 que contiene todos los datos y vemos las clases que contiene
classes = np.unique(y1)

print(classes)
#se calculan los pesos para cada clase que serán aplicados en la 
#función de costo
weights = compute_class_weight('balanced', classes=classes, y=y1)
#guardamos los pesos en un diccionario d que será usado en la función model.fit
d = dict(enumerate(weights, 0))

#se define la función de pérdida
cce=tf.keras.losses.CategoricalCrossentropy()
#se define el optimizador 
opt=tf.keras.optimizers.Adam(learning_rate=0.001)
#se compila el modelo
model.compile(optimizer=opt, loss=cce ,metrics=['accuracy'])

model.summary()

#se guarda el modelo con mejor desempeño en val_loss
checkpoint=ModelCheckpoint('Mejor_modelo_.keras',monitor='val_loss',verbose=1,save_best_only=True,mode='min')


#se entrena agregando el ajuste de class_weight o ponderación de clases
history=model.fit(x_train_scaled,y_train,epochs=200,class_weight=d,validation_data=(x_test_scaled,y_test),callbacks=[checkpoint],verbose=1)

test_loss,test_acc=model.evaluate(x_test_scaled,y_test)

print(f"Test accuracy: {test_acc}, test loss {test_loss}")

# model.save("red_materna.keras") este no es necesario ya se tiene el callback

#esto es para guardar el escalador que se usó en los datos
#se guarda las transformaciones usadas en scaler=StandardScaler()
import pickle
pickle.dump(scaler, open('scaler.pkl', 'wb'))

# esto no lo modifiqué:
import matplotlib.pyplot as plt

acc=history.history['accuracy']
val_acc=history.history['val_accuracy']
loss=history.history['loss']
val_loss=history.history['val_loss']

epochs=range(1,len(acc)+1)

plt.plot(epochs,acc, 'r',label='Precision de entrenamiento')
plt.plot(epochs,val_acc, 'b',label='Precision de validacion')
plt.title('Precision de entrenamiento y validacion')
plt.xlabel('Epocas')
plt.ylabel('Precision')

plt.legend()

plt.figure()

plt.plot(epochs,loss, 'r',label='Perdida de entrenamiento')
plt.plot(epochs,val_loss, 'b',label='Perdida de validacion')
plt.title('Perdida de entrenamiento y validacion')
plt.xlabel('Epocas')



#aquí cargamos el modelo entrenado para verificarlo
loaded_model = tf.keras.models.load_model("Mejor_modelo_.keras") 
#cargamos el escalador o normalizador de datos scaler=StandardScaler()
loaded_scaler = pickle.load(open('scaler.pkl', 'rb'))

#función para aplicar la normalización a los datos que se 
#alimenten al modelo, entran datos sin normalización y salen normalizados
def predict_output(input_data):
    input_data_scaled = loaded_scaler.transform(input_data)
    return input_data_scaled

#datos a verificar, aquí puse los de validación, pero pueden probar otros
x_a_probar=x_test # se puede cambiar a lo que quieran probar 
targets=y_test #se puede cambiar a lo que quieran probar 

#aquí se predicen las salidas del modelo
prediction=loaded_model(predict_output(x_a_probar))
prediction=np.array(prediction)
#se obtiene la clase ganadora con np.argmax
prediction_label=np.argmax(prediction,axis=1)
#también sacamos la clase del target
targets=np.argmax(targets,axis=1)


#función que calcula la matrix de confusión multiclase
def confusion_matrix(predictions, targets, num_classes):
 
    # Inicializa la matriz de confusión con ceros
    matrix = np.zeros((num_classes, num_classes), dtype=int)

    #actualiza la matriz de confusión
    for p, t in zip(predictions, targets):
        matrix[t, p] += 1

    return matrix


num_classes = 3
#alimentamos la matrix de confusión
matrix = confusion_matrix(prediction_label,targets , num_classes)
#se imprime
print(matrix)

#todo lo que sigue es para ver la matrix como un heatmap
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Calcula el porcentaje de precisión
accuracy = accuracy_score(targets, prediction_label) * 100

# Muestra el heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues", xticklabels=range(num_classes), yticklabels=range(num_classes))
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title(f'Confusion Matrix - Accuracy: {accuracy:.2f}%')
plt.show()