import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
tip_ids = [4, 8, 12, 16, 20]

gesture_dict = {
    "OPEN":  [1, 1, 1, 1, 1],
    "INDEX": [0, 1, 0, 0, 0],
    "THUMB": [1, 0, 0, 0, 0],
    "FIST":  [0, 0, 0, 0, 0]
}

gesture_password = ["OPEN", "THUMB"]
user_pattern = []
last_time = time.time()

cap = cv2.VideoCapture(1)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        finger_status = []

        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                lm_list = []
                h, w, _ = frame.shape

                for id, lm in enumerate(hand_landmark.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append((id, cx, cy))

                if len(lm_list) == 21:
                    # Thumb
                    if lm_list[tip_ids[0]][1] > lm_list[tip_ids[0] - 1][1]:
                        finger_status.append(1)
                    else:
                        finger_status.append(0)

                    # Other fingers
                    for i in range(1, 5):
                        if lm_list[tip_ids[i]][2] < lm_list[tip_ids[i] - 2][2]:
                            finger_status.append(1)
                        else:
                            finger_status.append(0)

                    current_time = time.time()
                    if current_time - last_time > 1.0:
                        for name, pattern in gesture_dict.items():
                            if finger_status == pattern:
                                if len(user_pattern) == 0 or user_pattern[-1] != name:
                                    user_pattern.append(name)
                                    last_time = current_time
                                    print("Gesture", name)

                    mp_draw.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)

        if len(user_pattern) == len(gesture_password):
            if user_pattern == gesture_password:
                print("✅ Access Granted")
                with open("status.txt", "w") as f:
                    f.write("UNLOCKED")
            else:
                print("❌ Access Denied")
                with open("status.txt", "w") as f:
                    f.write("LOCKED")
            user_pattern = []

        cv2.imshow("Gesture Lock", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
