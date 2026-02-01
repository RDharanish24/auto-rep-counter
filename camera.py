import cv2

class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        if not self.camera.isOpened():
            raise RuntimeError("Cannot open camera")

        self.width = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def get_frame(self):
        if not self.camera.isOpened():
            return False, None

        ret, frame = self.camera.read()
        if not ret:
            return False, None

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return True, frame

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()
