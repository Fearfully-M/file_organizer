from PIL import Image # for creating images
from pathlib import Path
from datetime import datetime
import calendar # converting int to str for the months
import argparse # for command line arguments

def main():
    parser = argparse.ArgumentParser(description="Photo and File Type Organizer")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d","--by-date", action="store_true", help="Sort photos by date into YYYY/MMMM folders")
    group.add_argument("-t","--by-type", action="store_true", help="Sort photos by file type into PNG/JPG/.MP4/etc. folders")
    parser.add_argument("-f","--folder", required= True, help="Folder to organize (default: current directory)")
    args = parser.parse_args()

    folder_path = Path(args.folder) # take user inputted path and send to Path
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Error: {folder_path} is not a valid directory")
        return

    if args.by_date:
        sort_by_date(folder_path)
    elif args.by_type:
        sort_by_type(folder_path)



"""Sorts the metadat of files, creates appropriate directories, and moves files to newly created directories"""
def sort_by_date(folder_path):

    try:
        # files = [x for x in folder_path.glob('*.png') if folder_path.is_dir()] + [y for y in folder_path.glob('*.jpg') if y.dir()] # add generator to list and search for the specified file types
        files = list(folder_path.glob('*.[jp][pn][gf]'))  # Matches .jpg, .jpeg, .png
        if not files:
            print("No .jpg or .png files were found")
            exit()
    except FileNotFoundError:
        print(f"Directory {folder_path} not found")
        exit()

    file_data = []
    # get the metadata for each file
    for file in files:
        stat = file.stat()
        mod_time = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

        # try to get the creation time
        try: 
            creation_time = datetime.fromtimestamp(stat.st_birthtime)
            # creation_time = datetime.fromtimestamp(stat.st_birthtime).strftime('%Y-%m-%d %H:%M:%S')
            # print(creation_time)

        # if on Windows do this or if it's a metadata change then do this on Linux/MacOS
        except AttributeError:
            creation_time = datetime.fromtimestamp(stat.st_ctime)
            # creation_time = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            # print(creation_time)
        
        except Exception as e:
            print(f"Error couldn't get metadata from files: {e}")
            exit()

        # append metadata to later be sorted
        file_data.append((file, creation_time, mod_time))

    # sort the file data
    sorted_file_data = []
    for file, creation_time, mod_time in sorted(file_data, key=lambda x : x[1]):
        sorted_file_data.append((file,creation_time,mod_time))
        # print(f"{file}: Created {creation_time.strftime('%Y-%m-%d %H:%M:%S')}") 

    # get the metadata from the sorted files
    for file_path in sorted_file_data:
        # get the year and month
        year = file_path[1].year 
        month = calendar.month_name[file_path[1].month]

        # create the target organized folder
        target_folder = Path("Organized") /str(year)/month
        target_folder.mkdir(parents=True,exist_ok=True)

        # Build target path
        target_path = target_folder / file_path[0].name
    
        # Handle duplicates
        counter = 1
        while target_path.exists():
            base, ext = file_path[0].stem, file_path[0].suffix
            target_path = target_folder / f"{base}_{counter}{ext}" # keep incrementing if it exists
            counter += 1
        
        # Move file - rename renames and moves files
        file_path[0].rename(target_path)

def sort_by_type(folder_path):
    try:
        files = list(folder_path.glob('*'))  # find all file types
        # files = [x for x in folder_path.glob('*') if folder_path.is_file()] # add generator to list and search for the specified file types
        if not files:
            print("No files were found")
            exit()
    except FileNotFoundError:
        print(f"Directory {folder_path} not found")
        exit()
    except Exception as e:
        print(f"Error processing files: {e}")
        exit()

    created_directories = []
    for file_path in files:
        
        # get the stem and suffix for each file
        #file_stem = file_path.stem
        file_suffix = file_path.suffix 

        folder_name_suffix = file_suffix[1:].lower()
        #print(folder_name)

        # ensure created directory is not created each time the same file type is found
        if folder_name_suffix not in created_directories:created_directories.append(folder_name_suffix)

        # create the target organized folder
        target_folder = Path("") /folder_name_suffix
        target_folder.mkdir(parents=True,exist_ok=True)

        # Build target path
        target_path = target_folder / file_path.name
    
        # Handle duplicates
        counter = 1
        while target_path.exists():
            base, ext = file_path.stem, file_path.suffix
            target_path = target_folder / f"{base}_{counter}{ext}" # keep incrementing if it exists
            counter += 1
        
        #Move file - rename renames and moves files
        file_path.rename(target_path)



if __name__ == "__main__":
    main()

