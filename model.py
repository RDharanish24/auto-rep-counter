import cv2
import numpy as np
from sklearn.svm import LinearSVC

IMG_SIZE = 150
FEATURES = IMG_SIZE * IMG_SIZE

class Model:
    def __init__(self):
        self.model = LinearSVC(max_iter=5000)
        self.trained = False

    def preprocess(self, frame):
        if len(frame.shape) == 3:
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        else:
            gray = frame

        img = cv2.resize(gray, (IMG_SIZE, IMG_SIZE))
        return img.reshape(FEATURES)

    def train_model(self, counters):
        X = []
        y = []

        if counters[0] <= 1 or counters[1] <= 1:
            return

        for i in range(1, counters[0]):
            img = cv2.imread(f"1/frame{i}.jpg", cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            X.append(img.reshape(FEATURES))
            y.append(1)

        for i in range(1, counters[1]):
            img = cv2.imread(f"2/frame{i}.jpg", cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            X.append(img.reshape(FEATURES))
            y.append(2)

        if len(X) == 0:
            return

        X = np.array(X)
        y = np.array(y)

        self.model.fit(X, y)
        self.trained = True

    def predict(self, frame):
        if not self.trained:
            return 0

        img = self.preprocess(frame)
        return self.model.predict([img])[0]
