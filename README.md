# Video Chapter File Generator - Python Script

## DISCLAIMER (the readme.md and vast majority of the code have been generated with AI)

This script is designed to generate a `chapters.txt` file for video files in a folder. The purpose of this file is to provide a list of chapters (timestamps and titles) that can be directly used when merging videos and uploading them to platforms like **YouTube**, where they can serve as a chapter list in the video description.

---

## Purpose

When creating long videos, chapters help viewers navigate content efficiently. This script automates the generation of chapter lists by:

1. **Calculating Video Start Times**: Based on the cumulative durations of individual videos in a folder.
2. **Creating Chapter Descriptions**: A text file (`chapters.txt`) is created in the same folder as the videos, listing each video's title and its corresponding start time.
3. **Saving Time**: Eliminates manual calculation of timestamps for merging and uploading videos.

**YouTube Integration**: After merging your videos, copy the contents of `chapters.txt` into the description field on YouTube to provide an easy-to-navigate chapter list for your viewers.

---

## Example Workflow

### 1. Prepare Your Videos
Ensure your videos are named and organized in folders:
- Example folder: `D:\MyVideos\session1`
  ```
  video1.mp4 (2:30 minutes)
  video2.mp4 (3:15 minutes)
  ```

### 2. Run the Script
Run the script to generate `chapters.txt`.

### 3. Output
The script creates a `chapters.txt` file with the following content:
```
video1.mp4: 0:00
video2.mp4: 2:30
```

### 4. Merge Videos
Use video editing tools to merge the videos into one file:
- Example output file: `session1_merged.mp4`

### 5. Upload and Add Chapters
Copy the contents of `chapters.txt` into the YouTube description for easy navigation:
```
0:00 video1.mp4
2:30 video2.mp4
```

---

## Why Use Chapters on YouTube?

- **Improved Viewer Experience**: Viewers can jump directly to sections of interest.
- **Enhanced Video SEO**: Chapters improve searchability and engagement.
- **Professional Presentation**: Well-structured videos with chapters make your content look polished.


  ---

  # Video Chapter File Generator - Python Script

This script generates a chapter file (`chapters.txt`) for video files in specified folders, listing each video's start time based on cumulative durations. It allows users to define paths dynamically and supports various video formats.

---

## Features

- **Flexible Path Input**: Choose the base directory and subfolders dynamically during runtime.
- **Supported Formats**: Processes `.mp4`, `.avi`, and `.mov` files.
- **Natural Sorting**: Ensures files with numeric parts are sorted logically (e.g., `video2` before `video10`).
- **Chapter File**: Creates a `chapters.txt` file listing each video and its start time.
- **User-Friendly**: Guides users step-by-step and handles missing folders gracefully.

---

## Prerequisites

1. **Python 3.x**: Ensure you have Python installed. Download it from [Python.org](https://www.python.org/).
2. **OpenCV Library**: Install OpenCV for video file processing:
   ```bash
   pip install opencv-python
   ```

---

## How to Use

### 1. **Save the Script**
   Save the provided script as `generate_chapters.py`.

### 2. **Run the Script**
   Open a terminal or command prompt, navigate to the directory where `generate_chapters.py` is saved, and run:
   ```bash
   python generate_chapters.py
   ```

### 3. **Provide Input**
   - **Base Folder Path**:  
     By default, the script uses your desktop as the base folder. Press `Enter` to accept this default or input a custom path.
     - Example:
       ```
       Default base folder is: C:\Users\YourUsername\Desktop
       Enter the base folder path (or press Enter to use the default): D:\MyVideos
       ```
   - **Subfolder Names**:  
     Enter the names of subfolders within the base folder, separated by commas. These should contain the video files.
     - Example:
       ```
       Enter the names of subfolders (comma-separated, e.g., part1,part2): session1,session2
       ```

### 4. **Output**
   - For each subfolder:
     - The script processes all video files.
     - Creates a `chapters.txt` file in the subfolder listing the cumulative start time of each video.
   - If a folder does not exist, a warning is displayed.

---

## Example Walkthrough

### Folder Structure
```
D:\MyVideos
├── session1
│   ├── video1.mp4
│   ├── video2.mp4
├── session2
│   ├── intro.avi
│   ├── main.mov
```

### Input
- **Base Folder Path**: `D:\MyVideos`
- **Subfolders**: `session1,session2`

### Output
#### `session1/chapters.txt`
```
video1.mp4: 0:00
video2.mp4: 1:30
```
(*Assumes `video1.mp4` is 1 minute 30 seconds long.*)

#### `session2/chapters.txt`
```
intro.avi: 0:00
main.mov: 2:45
```
(*Assumes `intro.avi` is 2 minutes 45 seconds long.*)

---

## Notes

1. **File Handling**:
   - Hidden files and unsupported formats are ignored.
   - Each folder is processed independently.

2. **Error Handling**:
   - If a folder doesn’t exist, the script displays a warning and continues with the next folder.
   - If a video file cannot be processed (e.g., corrupted), it will be skipped.

3. **Customizing Formats**:
   - Add or remove video extensions in this line of the script:
     ```python
     [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.avi', '.mov'))]
     ```

---

## Troubleshooting

- **No Videos Processed**:
  - Ensure video files exist in the specified folders.
  - Check file extensions; only `.mp4`, `.avi`, and `.mov` are supported by default.

- **Error: OpenCV Not Found**:
  - Ensure OpenCV is installed:
    ```bash
    pip install opencv-python
    ```

- **Chapter File Not Created**:
  - Ensure the script has write permissions for the folders.

---

