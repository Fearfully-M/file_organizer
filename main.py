from PIL import Image # for creating images
from pathlib import Path
from datetime import datetime
import calendar

def main():

    p = Path(r'MessyPhotos')# get all files
    print(p)
    try:
        files = [x for x in p.glob('*.png') if x.is_file()] + [y for y in p.glob('*.jpg') if y.is_file()] # add generator to list and search for the specified file types
        if not files:
            print("No .jpg or .png files were found")
            exit()
    except FileNotFoundError:
        print(f"Directory {p} not found")
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

        file_data.append((file, creation_time, mod_time))

        # print(file)
        # Helpful for debugging
        # print(f"File: {file}")
        # print(f"Size: {stat.st_size}")
        # print(f"Modified: {mod_time}")
        # print(f"Created/MetaData Change: {creation_time}")
        # print()
    
    sorted_file_data = []
    for file, creation_time, mod_time in sorted(file_data, key=lambda x : x[1]):
        sorted_file_data.append((file,creation_time,mod_time))
        # print(f"{file}: Created {creation_time.strftime('%Y-%m-%d %H:%M:%S')}") 

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


if __name__ == "__main__":
    main()

