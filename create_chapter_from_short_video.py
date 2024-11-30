import os
import cv2  # OpenCV is required to get video length
import re

# Function to calculate the duration of a video
def get_video_length(video_path):
    video = cv2.VideoCapture(video_path)  # Open video file
    fps = video.get(cv2.CAP_PROP_FPS)  # Frames per second
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)  # Total number of frames
    duration = frame_count / fps  # Calculate duration in seconds
    video.release()  # Release video resource
    return duration

# Function to format duration in hh:mm:ss or mm:ss format
def format_duration(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    if hours > 0:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes}:{seconds:02d}"

# Function to create a natural sort key for sorting files with numbers
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

# Function to generate a chapter file based on video durations
def generate_chapter_file(folder_path):
    # List video files in the folder, filtering by extension and sorting naturally
    video_files = sorted(
        [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.avi', '.mov'))],
        key=natural_sort_key
    )
    chapter_file_path = os.path.join(folder_path, "chapters.txt")

    # Open the chapter file for writing, ensuring proper encoding
    with open(chapter_file_path, 'w', encoding='utf-8') as chapter_file:
        total_duration = 0.0  # Track cumulative video durations
        
        for i, video in enumerate(video_files):
            video_path = os.path.join(folder_path, video)
            video_length = get_video_length(video_path)  # Get video length
            
            # Write chapter information to the file
            if i == 0:
                chapter_file.write(f"{video}: {format_duration(0)}\n")
            else:
                chapter_file.write(f"{video}: {format_duration(total_duration)}\n")
            
            total_duration += video_length  # Update total duration

    print(f"Chapter file created: {chapter_file_path}")

# Main script logic
if __name__ == "__main__":
    # Prompt the user for the base folder path or use default
    base_folder = os.getenv("USERPROFILE")  # Use user's home directory as a default
    print(f"Default base folder is: {base_folder}\\Desktop")
    base_folder = input("Enter the base folder path (or press Enter to use the default): ").strip() or f"{base_folder}\\Desktop"

    # Ask the user to provide subfolder names
    folder_names = input("Enter the names of subfolders (comma-separated, e.g., part1,part2): ").split(',')

    # Process each folder
    for folder in folder_names:
        folder_path = os.path.join(base_folder, folder.strip())  # Build full path
        if os.path.exists(folder_path):
            print(f"Processing folder: {folder_path}")
            generate_chapter_file(folder_path)
        else:
            print(f"Warning: Folder does not exist - {folder_path}")
