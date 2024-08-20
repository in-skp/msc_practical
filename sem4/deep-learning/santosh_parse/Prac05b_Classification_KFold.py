from sklearn.datasets import make_classification
from sklearn.model_selection import KFold
import keras
from keras import models
from keras import layers
from keras import utils
from sklearn.metrics import accuracy_score
X, y = make_classification(n_samples=100, n_features=20, n_informative=2,
                           n_redundant=0, n_classes=2, n_clusters_per_class=2, random_state=42)
y = utils.to_categorical(y)
n_splits = 5
kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(X.shape[1],)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])
fold_accuracies = []
for train_index, val_index in kf.split(X):
    X_train, X_val = X[train_index], X[val_index]
    y_train, y_val = y[train_index], y[val_index]
    model.fit(X_train, y_train, epochs=10, batch_size=32,
              validation_data=(X_val, y_val))
    y_pred_prob = model.predict(X_val)
    y_pred = y_pred_prob.argmax(axis=1)
    accuracy = accuracy_score(y_val.argmax(axis=1), y_pred)
    fold_accuracies.append(accuracy)
mean_accuracy = sum(fold_accuracies) / len(fold_accuracies)
print(f'Mean accuracy: {mean_accuracy:.2f}')
