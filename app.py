import tkinter as tk
import os
import PIL.Image
import PIL.ImageTk
import cv2
import camera
import model

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bicep Curl Counter")
        self.state = "extended"

        self.counters = [1, 1]
        self.rep_counter = 0

        

        self.counting_enabled = False
        self.camera = camera.Camera()
        self.model = model.Model()

        self.init_gui()
        self.delay = 15
        self.update()

        self.window.attributes("-topmost", True)
        self.window.mainloop()

    def init_gui(self):
        self.canvas = tk.Canvas(
            self.window,
            width=self.camera.width,
            height=self.camera.height
        )
        self.canvas.pack()

        self.btn_toggle = tk.Button(
            self.window,
            text="Toggle Counting",
            width=50,
            command=self.counting_toggle
        )
        self.btn_toggle.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_one = tk.Button(
            self.window,
            text="Extended",
            width=50,
            command=lambda: self.save_for_class(1)
        )
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_two = tk.Button(
            self.window,
            text="Contracted",
            width=50,
            command=lambda: self.save_for_class(2)
        )
        self.btn_class_two.pack(anchor=tk.CENTER, expand=True)

        self.btn_train = tk.Button(
            self.window,
            text="Train",
            width=50,
            command=self.train_model_safe
        )
        self.btn_train.pack(anchor=tk.CENTER, expand=True)

        self.btn_reset = tk.Button(
            self.window,
            text="Reset",
            width=50,
            command=self.reset
        )
        self.btn_reset.pack(anchor=tk.CENTER, expand=True)

        self.counter_label = tk.Label(
            self.window,
            text=str(self.rep_counter),
            font=("Arial", 24),
            width=50
        )
        self.counter_label.pack(anchor=tk.CENTER, expand=True)

    def update(self):
        if self.counting_enabled:
            self.predict()

       

        self.counter_label.config(text=str(self.rep_counter))

        ret, frame = self.camera.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(
                image=PIL.Image.fromarray(frame)
            )
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update)

    def predict(self):
        if not self.model.trained:
            return

        ret, frame = self.camera.get_frame()
        if not ret:
            return

        prediction = self.model.predict(frame)

        if prediction == 2 and self.state == "extended":
            self.state = "contracted"

        elif prediction == 1 and self.state == "contracted":
            self.rep_counter += 1
            self.state = "extended"


    def counting_toggle(self):
        self.counting_enabled = not self.counting_enabled

    def reset(self):
        self.rep_counter = 0
        self.counter_label.config(text="0")

    def train_model_safe(self):
        if self.counters[0] <= 1 or self.counters[1] <= 1:
            return
        self.model.train_model(self.counters)

    def save_for_class(self, class_num):
        ret, frame = self.camera.get_frame()
        if not ret:
            return

        if not os.path.exists("1"):
            os.mkdir("1")
        if not os.path.exists("2"):
            os.mkdir("2")

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        img = cv2.resize(gray, (150, 150))

        path = f"{class_num}/frame{self.counters[class_num - 1]}.jpg"
        cv2.imwrite(path, img)

        self.counters[class_num - 1] += 1
