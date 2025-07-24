# Photo, File, and File Category Organizer

A Python command-line tool to organize image files, video, and/or audio files into folders by date or file type or by media category.

Also includes an additional script for optional dummy file generation to test organization capabilties of the program
This requires dependencies unlike the main program which only uses standard Python modules
## Features
- Sort images by date into `Organized/YYYY/MMMM/` folders (e.g., `Organized/2024/December/`).
- Sort images by file type into `Organized/PNG/`, `Organized/JPG/`, etc.
- Handles duplicate filenames by appending `_1`, `_2`, etc.
- Requires the user to submit a specific folder to prevent accidental operations on critical directories (i.e. organizing system32 LOL)

## Requirements
- Python 3.6 or higher
- For `main.py`: No external dependencies (uses standard libraries: `pathlib`, `datetime`, `calendar`, `argparse`)
- For `image_generator.py`:
  - Pillow library for image generation
  - Pydub library for audio generation
  - Moviepy library for video generation
  - FFmpeg for audio and video processing (see Installation)

## Installation 
1. Download `main.py` to your computer.
2. Ensure Python 3.6+ is installed (`python3 --version` to check). 
This is all that's needed for the organization file. If you want to generate files to text then you'll need the following in the next section:

## Installation for file generation
1. Clone or download the repository:
   ```bash
   git clone https://github.com/Fearfully-M/file_organizer.git
   cd file_organizer





Ensure Python 3.6+ is installed:

```python3 --version```



Create and activate a virtual environment (recommended):

```python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```



Install Python dependencies for image_generator.py:

```pip install -r requirements.txt```



Install FFmpeg for audio and video generation in image_generator.py:





macOS:

```brew install ffmpeg```



Ubuntu/Linux:

```sudo apt-get install ffmpeg```



Windows:





Download ffmpeg from https://www.gyan.dev/ffmpeg/builds/ (e.g., ffmpeg-git-full.7z).



Extract to a folder (e.g., C:\ffmpeg).



Add C:\ffmpeg\bin to your system PATH (search "edit environment variables" in Windows).



Verify FFmpeg installation:

ffmpeg -version



Note: Audio formats supported are MP3, WAV, and FLAC. Other formats may require additional FFmpeg codecs.

## Usage
Run the script from the command line, specifying a sorting mode and folder:

- Sort by date:
  ```bash
  python3 main.py -d -f MessyPhotos

  Organizes 'mp4', 'mkv', 'mov', 'avi', 'wmv', 'flv', 'webm', 'mpeg', '3gp', 'm4v' 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'webp', 'heic', 'svg' files in MessyPhotos into ./Organized/YYYY/MMMM/.

Sort by file type:
```python3 main.py -t -f MessyPhotos```
Organizes files into ./Organized/PNG/, ./Organized/JPG/, etc.

Sort by category :
```python3 main.py -c -f MessyPhotos```
Organizes related files (ex .png .jpg as images or .mov and .mp4 as videos) into ./Organized/Music/, ./Organized/Videos/, ./Organized/Images/, ./Organized/Other/


View help:
python3 main.py --help

Options:

-d[ate], --by-date: Sort by date.
-t[ype], --by-type: Sort by file type.
-f[older], --folder: Folder to organize (required).

Safety Notes

Warning: This script moves files, which cannot be easily undone. Always back up your files before running.
The -f/--folder argument is required to prevent accidental operations on critical directories (e.g., root, system32).
There is no default directory to help prevent this.

**Always verify the folder path before running (e.g., -f MessyPhotos).**

Contributing
Found a bug or want to add a feature (e.g., adding more pictures, recursively sort within subdirectories)? Feel free to suggest improvements or share feedback!```