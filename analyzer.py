from utils.pose_extractor import extract_pose
from utils.video_sync import sync_poses
from utils.video_renderer import generate_comparison_video

def analyze_swing(user_video_path, reference_video_path):
    user_landmarks = extract_pose(user_video_path)
    ref_landmarks = extract_pose(reference_video_path)

    alignment = sync_poses(user_landmarks, ref_landmarks)

    comparison_video_path = generate_comparison_video(
        user_video_path, reference_video_path, alignment, user_landmarks, ref_landmarks
    )

    print(f"Comparison video saved at {comparison_video_path}")
    return comparison_video_path
