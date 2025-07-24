from PIL import Image # for creating images
import os # to handle files and metadata 
import time # to get access to the time metadata
import random
from pydub import AudioSegment # used for clipping audio segments
import shutil # checkes for dependencies 
from moviepy import VideoFileClip

def check_ffmpeg():
    if not shutil.which('ffmpeg'):
        raise EnvironmentError("FFmpeg is not installed or not found as a PATH variable. Make sure it is installed on your system 'brew install ffmpeg on macOS")

def main():
    directory_name = "MessyFolder"
    # creates images and sets the names to a list
    image_list = image_generator(directory_name)

    # takes the image list and randomizes the creation dates
    randomize_creation_time(image_list, directory_name)

    # generate sounds and videos
    sound_generator(directory_name)
    video_generator(directory_name)

"""Generates picture files to see how the file organizer works"""
def image_generator(directory_name):
    
    image_path_list = [] # store image paths
    # generate "dummy" images

    # make a new directory for the photos if it doesn't exist
    os.makedirs(directory_name, exist_ok=True)

    # create the dummy images and create list of their names
    image_extension = ['jpg', 'jpeg', 'png', 'gif']
    for dummy_image in range(8):
        n,m = 1080, 1920 # set size of image Length x Width
        # create a new image for each iteration
        image = Image.new('RGB', (n, m), color = (200,100,50))
    
        # create the files and join to the new directory
        image_filename = f'image{dummy_image}.{random.choice(image_extension)}'
        image_path = os.path.join(directory_name, image_filename)

        # save image to the directory
        image.save(image_path, "PNG")

        # append the full path to the image name list
        image_path_list.append(image_path)

    return image_path_list

"""Generates sound files to see how the file organizer works"""
def sound_generator(directory_name, audio_source="naughty_sounds.mp3"):
    sound_path_list = []
    os.makedirs(directory_name, exist_ok=True)
    sound_extensions = ['mp3', 'wav', 'flac']
    
    # Load source audio
    try:
        audio = AudioSegment.from_file(audio_source)
    except FileNotFoundError:
        print(f"Source audio {audio_source} not found. Place it in the same directory as this script.")
        return sound_path_list
    
    # Generate 8 dummy audio clips
    for dummy_audio in range(8):
        # Clip a random 5-second segment
        duration_ms = len(audio)
        start_ms = random.randint(0, max(0, duration_ms - 5000))  # Ensure doesn't exceed max audio length
        clip = audio[start_ms:start_ms + 5000]  # 5-second clip
        
        # Choose random extension
        ext = random.choice(sound_extensions)
        sound_filename = f'sound{dummy_audio}.{ext}'
        sound_path = os.path.join(directory_name, sound_filename)
        
        # Export clip in the chosen format
        clip.export(sound_path, format=ext)
        sound_path_list.append(sound_path)
    
    return sound_path_list

"""Generates video files to see how the file organizer works"""
def video_generator(directory_name, source_video="super_evil_video.mp4"):
    video_path_list = []
    os.makedirs(directory_name, exist_ok=True)
    video_extensions = ['mp4', 'mkv', 'mov']
    
    if VideoFileClip is None:
        print("Skipping video generation: moviepy not installed.")
        return video_path_list
    try:
        video = VideoFileClip(source_video)
    except FileNotFoundError:
        print(f"Source video {source_video} not found. Place it in the same directory as this script.")
        return video_path_list
    except Exception as e:
        print(f"Error loading video: {e}")
        return video_path_list
    
    try:
        for dummy_video in range(8):
            duration_s = video.duration
            start_s = random.uniform(0, max(0, duration_s - 5)) # ensure the clip isn't at the last 5 seconds of the video
            clip = video.subclipped(start_s, start_s + 5)
            ext = random.choice(video_extensions)
            video_filename = f'video{dummy_video}.{ext}'
            video_path = os.path.join(directory_name, video_filename)
            clip.write_videofile(video_path, codec="libx264", audio_codec="aac")
            video_path_list.append(video_path)
    except Exception as e:
        print(f"Error generating video clips: {e}")
    finally:
        video.close()
    
    return video_path_list

"""randomizes creation time of pictures"""
def randomize_creation_time(image_path_list, directory_name):
    # Get the current modification time
    # original_mod_time = os.path.getmtime('image0.png')
    # original_access_time = os.path.getatime('image0.png')

    # change access and mod times for each generated picture file
    for image_path in image_path_list:
         # Set the new modification and access times to January 1, 2024
        new_time = time.mktime(time.strptime(f"2024-{random.randint(1,12)}-{random.randint(1,28)}", "%Y-%m-%d"))
        os.utime(f'{image_path}', times=(new_time, new_time))  # Set both access and modification times


    #print(f"Original modification time: {time.ctime(original_mod_time)}")
    #print(f"Original access time: {time.ctime(original_access_time)}")

    # Verify the changes
    # new_mod_time = os.path.getmtime('image0.png')
    # new_access_time = os.path.getatime('image0.png')

    #print(f"New modification time: {time.ctime(new_mod_time)}")
    #print(f"New access time: {time.ctime(new_access_time)}")

if __name__ == "__main__":
    main()
