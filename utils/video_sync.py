from dtaidistance import dtw
import numpy as np

def sync_poses(user_landmarks, ref_landmarks):
    print("Landmark sample sizes:", len(user_landmarks), len(ref_landmarks))

    # Flatten each frame and reduce to scalar norm
    user_seq = [np.linalg.norm(np.array(frame).flatten()) for frame in user_landmarks]
    ref_seq = [np.linalg.norm(np.array(frame).flatten()) for frame in ref_landmarks]

    distance = dtw.distance(user_seq, ref_seq)
    path = dtw.warping_path(user_seq, ref_seq)

    print("DTW distance:", distance)
    print("Path sample:", path[:5])

    return path
