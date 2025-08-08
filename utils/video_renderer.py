import cv2
import numpy as np
import subprocess
import os

def draw_landmarks(frame, landmarks):
    for x, y, _ in landmarks:
        cv2.circle(frame, (int(x * frame.shape[1]), int(y * frame.shape[0])), 4, (0, 255, 0), -1)
    return frame

def generate_comparison_video(user_video_path, ref_video_path, alignment, user_poses, ref_poses):
    cap_user = cv2.VideoCapture(user_video_path)
    cap_ref = cv2.VideoCapture(ref_video_path)
    output_frames = []

    for u_idx, r_idx in alignment:
        cap_user.set(cv2.CAP_PROP_POS_FRAMES, u_idx)
        cap_ref.set(cv2.CAP_PROP_POS_FRAMES, r_idx)
        ret_u, frame_u = cap_user.read()
        ret_r, frame_r = cap_ref.read()
        if not ret_u or not ret_r:
            continue
        frame_u = draw_landmarks(frame_u, user_poses[u_idx])
        frame_r = draw_landmarks(frame_r, ref_poses[r_idx])
        combined = np.hstack((frame_r, frame_u))
        output_frames.append(combined)

    cap_user.release()
    cap_ref.release()

    if not output_frames:
        raise RuntimeError("No frames were processed.")

    height, width, _ = output_frames[0].shape
    temp_path = "temp.avi"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 30
    out = cv2.VideoWriter(temp_path, fourcc, fps, (width, height))

    for frame in output_frames:
        out.write(frame)
    out.release()

    final_path = "comparison_output.mp4"

    # Convert using libx264 (more commonly available and supported than libopenh264)
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-i", temp_path,
        "-vcodec", "libx264", "-crf", "23", "-preset", "veryfast", "-pix_fmt", "yuv420p",
        final_path
    ]
    subprocess.run(ffmpeg_cmd, check=True)

    os.remove(temp_path)
    return final_path
