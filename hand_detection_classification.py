import cv2
import mediapipe as mp
from hagrid.detector.ssd_mobilenetv3 import SSDMobilenet
import torchvision
from PIL import Image, ImageOps
import torch
from torchvision.transforms import functional as func
import time

import sqlite3
conn = sqlite3.connect("Gesture_recognition")
c = conn.cursor()

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

COLOR = (0,255,0)
FONT = cv2.FONT_HERSHEY_COMPLEX

targets = {
    1: "call",
    2: "dislike",
    3: "fist",
    4: "four",
    5: "like",
    6: "mute",
    7: "ok",
    8: "one",
    9: "palm",
    10: "peace",
    11: "rock",
    12: "stop",
    13: "stop inverted",
    14: "three",
    15: "two up",
    16: "two up inverted",
    17: "three2",
    18: "peace inverted",
    19: "no gesture",
}

def load_model():    
    ssd_mobilenet = SSDMobilenet(num_classes=len(targets)+1)
    ssd_mobilenet.load_state_dict("SSDLite.pth",map_location="cpu")
    ssd_mobilenet.eval()
    return ssd_mobilenet


def preprocess(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    image = Image.fromarray(img)
    width,height = image.size

    image = ImageOps.pad(image,(max(width,height), max(width,height)))
    padded_width, padded_height = image.size
    image = image.resize((320,320))

    img_tensor = func.pil_to_tensor(image)
    img_tensor = func.convert_image_dtype(img_tensor)
    img_tensor = img_tensor[None, :, :, :]
    return img_tensor, (width, height), (padded_width,padded_height)

def det_class(detector):
    hands = mp.solutions.hands.Hands(
        model_complexity=0, static_image_mode=False,max_num_hands=2,min_detection_confidence=0.8
    )

    cap = cv2.VideoCapture(0)

    t1 = cnt = 0
    while cap.isOpened():
        delta = time.time() - t1
        t1 = time.time()

        ret, frame = cap.read()
        if ret:
            processed_frame, size, padded_size = preprocess(frame)
            with torch.no_grad():
                output = detector(processed_frame)[0]
            boxes = output["boxes"][:2]
            scores = output["scores"][:2]
            labels = output["labels"][:2]
            results = hands.process(frame[:,:,::-1])
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                                frame,
                                hand_landmarks,
                                mp.solutions.hands.HAND_CONNECTIONS,
                                mp_drawing_styles.DrawingSpec(color=[0, 255, 0], thickness=2, circle_radius=1),
                                mp_drawing_styles.DrawingSpec(color=[255, 255, 255], thickness=1, circle_radius=1),
                            )
            
            for i in range(min(2,len(boxes))):
                if scores[i] > 0.5:
                    width, height = size
                    padded_width,padded_height = padded_size
                    scale = max(width,height)/320
                    padding_w = abs(padded_width-width)//(2*scale)
                    padding_h  = abs(padded_height - height)//(2*scale)

                    x1 = int((boxes[i][0] - padding_w)*scale)
                    y1 = int((boxes[i][1] - padding_w)*scale)
                    x2 = int((boxes[i][2] - padding_w)*scale)
                    y2 = int((boxes[i][3] - padding_w)*scale)

                    cv2.rectangle(frame,(x1,y1),(x2,y2),COLOR,thickness=3)
                    cv2.putText(
                        frame,
                        targets[int(labels[i])],
                        (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0,0,255),
                        thickness = 3,
                    )
            fps = 1/delta
            cv2.putText(frame,f"FPS:{fps:02.1f}, Frame : {cnt}", (30,30), FONT ,1, COLOR,2)
            cnt+=1
            cv2.imshow("Frame",frame)
            key = cv2.waitKey(1)
            if key == ord("q"):
                return
        else:
            cap.release()
            cv2.destroyAllWindows()
if __name__ =="__main__":
    model = load_model()
    det_class(model)