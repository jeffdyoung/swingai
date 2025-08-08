import cv2
import mediapipe as mp

# Optional: indices of selected landmarks to reduce dimensionality
SELECTED_LANDMARK_INDICES = [
    11, 12, 23, 24  # shoulders and hips (left/right)
]

def extract_pose(video_path):
    pose = mp.solutions.pose.Pose()
    cap = cv2.VideoCapture(video_path)
    landmarks = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.pose_landmarks:
            all_landmarks = results.pose_landmarks.landmark
            if len(all_landmarks) == 33:
                # Use full body landmarks or a selected subset
                frame_landmarks = [
                    (lm.x, lm.y, lm.z)
                    for idx, lm in enumerate(all_landmarks)
                    if idx in SELECTED_LANDMARK_INDICES
                ]
                landmarks.append(frame_landmarks)
            else:
                print("Skipped frame with missing landmarks")
    cap.release()
    return landmarks
