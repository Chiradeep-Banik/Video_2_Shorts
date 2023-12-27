from moviepy.editor import VideoFileClip,clips_array, AudioFileClip
import moviepy.video.fx.all as vfx
import os
import subprocess

video_path = "../video/demo.mp4"
mine_path = "../video/minecraft.mp4"
output_path = "../output"

main_video = VideoFileClip(video_path,target_resolution=(1080,960))
main_audio = AudioFileClip(video_path)
bottom_video = VideoFileClip(mine_path,audio=None,target_resolution=(960,1080)).subclip(0, 29)
print(main_video.duration)
print(bottom_video.duration)
print(main_audio.duration)

duration = int(main_video.duration)
timings = []
for i in range(0,duration,60):
    start,end = i,i+59
    if end < main_video.duration:
        timings.append([start,end])

def remove_mp3_files(directory="."):
    """
    Remove all MP3 files in the specified directory or the current directory.

    Parameters:
    - directory (str): The directory path. Default is the current directory.
    """
    # Get the specified or current directory
    current_directory = os.path.abspath(directory)

    # List all files in the directory
    files = os.listdir(current_directory)

    # Filter only the mp3 files
    mp3_files = [file for file in files if file.endswith(".mp3")]

    # Remove each mp3 file
    for mp3_file in mp3_files:
        file_path = os.path.join(current_directory, mp3_file)
        os.remove(file_path)



# target_resolution=(1920,1080)

def process_clip(start, end, main_video,main_audio,bottom_video, output_path,speed_factor=2):
    print(f'Doing this : {start}-{end}')
    top_clip = main_video.subclip(start, end)
    top_audio = main_audio.subclip(start, end)
    bottom_clip = bottom_video

    clips = [[top_clip],[bottom_clip]]
    final = clips_array(clips)

    final = final.fx(vfx.speedx,speed_factor)

    temp_video_path = os.path.join(output_path, f'temp_video_from_{start}_{end}_clip.mp4')
    final.write_videofile(temp_video_path)
    print(f'Finished this : {start}-{end}')
    return temp_video_path

def process_audio(start,end,temp_video_path,speed_factor=2):
    audio = AudioFileClip(temp_video_path)
    original_audio_path = f'audio_from_{start}_{end}_clip.mp3'
    audio.write_audiofile(original_audio_path)

    final_audio_path = f'audio_from_{start}_{end}_clip_final.mp3'


    # Construct the ffmpeg command
    ffmpeg_command = [
        "ffmpeg",
        "-i", original_audio_path,
        "-af", f"asetrate=44100*{1/speed_factor},aresample=44100,atempo={speed_factor}",
        final_audio_path
    ]

    # Run the ffmpeg command
    subprocess.run(ffmpeg_command)
    return final_audio_path

def create_final(temp_video_path,final_audio_path,result_path):
    video = VideoFileClip(temp_video_path)
    audio = AudioFileClip(final_audio_path)

    video.audio = audio
    video.write_videofile(result_path)


for start,end in timings:
    temp_video_path = process_clip(start,end,main_video,main_audio,bottom_video,output_path,2)
    print(temp_video_path)
    final_audio_path = process_audio(start,end,temp_video_path,2)
    print(final_audio_path)
    final_path = os.path.join(output_path,f'video_from_{start}_{end}_clip.mp4')
    create_final(temp_video_path,final_audio_path,final_path)
    os.remove(temp_video_path)
    remove_mp3_files()
    
    
    


