import cv2
import mediapipe as mp

# 1. Inizializza MediaPipe Hands e il modulo per il disegno
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)

# 2. Carica l'immagine
img = cv2.imread("img/input.jpg")
if img is None:
    print("Errore: Immagine non trovata!")
    exit()

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 3. Processa l'immagine
results = hands.process(img_rgb)

# 4. Se trova le mani, disegna i punti
if results.multi_hand_landmarks:
    print(f"✋ Trovate {len(results.multi_hand_landmarks)} mani!")
    
    for hand_landmarks in results.multi_hand_landmarks:
        # DISEGNA QUI: Disegna i 21 punti e le connessioni tra loro
        mp_drawing.draw_landmarks(
            img, 
            hand_landmarks, 
            mp_hands.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=4), # Colore punti
            mp_drawing.DrawingSpec(color=(0,255|0), thickness=2) # Colore linee
        )

    # 5. Mostra l'immagine a video
    cv2.imshow("Mani Rilevate", img)
    print("Premi un tasto qualsiasi sull'immagine per chiudere.")
    cv2.waitKey(0) # Aspetta che premi un tasto
    cv2.destroyAllWindows()
else:
    print("❌ Nessuna mano rilevata")

hands.close()
