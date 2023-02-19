import os
# REPLACE EVERY SQUARE BRACKETS WITH APPROPRIATE VALUE.

# Function to rename multiple files
def main():
    folder = r"[SHOW LOCATION]"
    i = 1
    season = "[SEASON]"
    for count, filename in enumerate(os.listdir(folder)):
        new_filename = f"[SHOW NAME] - S{season}E{'0' + str(i) if len(str(i)) < 2 else str(i)}.mkv"
        src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst = f"{folder}/{new_filename}"
        i += 1

        # rename() function will rename all the files
        os.rename(src, dst)

if __name__ == '__main__':
    main()