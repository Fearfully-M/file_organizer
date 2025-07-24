from PIL import Image # for creating images
import os # to handle files and metadata 
import time # to get access to the time metadata
import random

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
def sound_generator(directory_name):
    sound_path_list = [] # store sound paths
    # generate "dummy" sounds

    # make a new directory for the photos if it doesn't exist
    os.makedirs(directory_name, exist_ok=True)

    # create the dummy sounds and create list of their names
    sound_extension = ['mp3', 'wav', 'flac', 'aac']
    for dummy_image in range(8):
        n,m = 1080, 1920 # set size of image Length x Width
        # create a new image for each iteration
        image = Image.new('RGB', (n, m), color = (200,100,50))
    
        # create the files and join to the new directory
        image_filename = f'image{dummy_image}.{random.choice(sound_extension)}'
        image_path = os.path.join(directory_name, image_filename)

        # save image to the directory
        image.save(image_path, "PNG")

        # append the full path to the image name list
        sound_path_list.append(image_path)

    return sound_path_list
    audio_extension = ['mp3', 'wav', 'flac', 'aac']

"""Generates video files to see how the file organizer works"""
def video_generator(directory_name):
    video_path_list = [] # store video paths
    # generate "dummy" videos

    # make a new directory for the videos if it doesn't exist
    os.makedirs(directory_name, exist_ok=True)

    # create the dummy videos and create list of their names
    video_extension = ['mp4', 'mkv', 'mov']
    for dummy_image in range(8):
        n,m = 1080, 1920 # set size of image Length x Width
        # create a new image for each iteration
        image = Image.new('RGB', (n, m), color = (200,100,50))
    
        # create the files and join to the new directory
        image_filename = f'image{dummy_image}.{random.choice(video_extension)}'
        image_path = os.path.join(directory_name, image_filename)

        # save image to the directory
        image.save(image_path, "PNG")

        # append the full path to the image name list
        video_path_list.append(image_path)

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
