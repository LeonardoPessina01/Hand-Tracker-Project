import cv2
import mediapipe as mp
import gestures

def rileva(landmarks):
    p = [[lm.x, lm.y] for lm in landmarks]
    scala = gestures.get_dist(p[0], p[9])

    if gestures.ok(p, scala):
        return "OK"
    elif gestures.vittoria(p, scala):
        return "VITTORIA"
    elif gestures.polliceinsu(p, scala):
        return "POLLICE IN SU"
    elif gestures.pugno(p, scala):
        return "PUGNO"
    return "NON RICONOSCIUTO"

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)

img = cv2.imread("input8.jpg")
if img is not None:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        print(rileva(results.multi_hand_landmarks[0].landmark))
    else:
        print("NESSUNA MANO")

hands.close()