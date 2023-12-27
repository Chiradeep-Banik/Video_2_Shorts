# Vid_2_Shorts 🎬

## YouTube Shorts Creation Tool 🚀

### Video Links
- **Main Video**: [EC320_1](https://youtu.be/e23KCzvKimc?si=vrE9dfJf6nVLGOoQ)
- **Shorts Playlist**: [PlayList](https://youtube.com/playlist?list=PL7-tvQtb_MvspdsrSFY5ncczeqM91gLYZ&si=TaAghDHn6KaX54oG)

### Project Overview
Automate YouTube shorts creation from a main video and bottom video. Tasks include zooming, adding subtitles, and making segments efficient.

### Usage

1. **Requirements**
   - Python 3.10
   - FFMPEG v >= 4.4
   - Install: `pip install moviepy`

2. **Execution**
   ```bash
   ./venv/bin/python3.10 src/script.py
   ```

### Project Structure

- `src/script.py`: Main script.
- `video/demo.mp4`: Main video.
- `video/minecraft.mp4`: Bottom video.
- `output/`: Processed videos.

### Functions

- `process_clip(start, end, main_video, bottom_video, output_path, speed_factor=2)`
  - Process video clips (speed up).

- `process_audio(start, end, temp_video_path, speed_factor=2)`
  - Process audio (adjust speed).

- `create_final(temp_video_path, final_audio_path, result_path)`
  - Combine processed video and audio.

### Notes
- Ensure proper library installation.
- Adjust parameters as needed.
- Generated files stored in `output/`.

### Future Work 🚧
- Zoom in the video to fit the screen (use `vfx.crop()` function).
- Add subtitles of the top video to the bottom video.
- Make the segments of the video more efficient
  - By analyzing the transcript.
  - Cut the video at the pauses.

### Disclaimer
Personal project; use at your own discretion. Contributions and feedback welcome! 👏