from PIL import Image
import glob
import os
import sys
import getopt

converted_n = 0
skipped_n = 0
deleted_n = 0

directory = "./"
delete_after = False
jpg_quality = 95
file_list = []
total_n = 0

def main(argv):
    global file_list
    global total_n
    global delete_after
    global jpg_quality
    global directory

    try:
        opts, args = getopt.getopt(argv, "hi:dq:", ["indir=","delete","quality="])
    except getopt.GetoptError:
        print_usage()
    for opt, arg in opts:
        if opt == "-h":
            print_usage()
            sys.exit(2)
        elif opt in ("-i", "--indir"):
            directory = arg
        elif opt in ("-d", "--delete"):
            delete_after = True
        elif opt in ("-q" "--quality"):
            if arg < 20:
                jpg_quality = arg
            elif arg > 100:
                jpg_quality = 100
            else:
                jpg_quality = arg
    
    if directory[-1] != "\\" and directory[-1] != "/":
        print("Error: the target directory " + directory + " should end in a slash")
        sys.exit(2)

    print("Gathering PNG file names from " + directory)
    print("They'll be converted to JPGs with " + str(jpg_quality) + "% quality")
    if (delete_after):
        print("Converted PNGs will be deleted afterwards.")

    file_list = glob.glob(directory+"*.png")
    total_n = len(file_list)

    process_folder()
    


def process_folder():
    global converted_n
    global skipped_n
    global deleted_n

    print("Found " + str(total_n) + " potential png's to convert in " + directory)

    for file in file_list:
        # check if the jpg version alaready exists
        if glob.glob(file.replace("png", "jpg")):
            print("Already converted" + file + " so skipping conversion")
            skipped_n = skipped_n + 1
        else:
            im = Image.open(file)
            rgb_im = im.convert('RGB')
            rgb_im.save(file.replace("png", "jpg"), quality=jpg_quality)
            converted_n = converted_n + 1
            potential_left = total_n - skipped_n
            print("Converted file " + file + ", so far we've done " + str(converted_n) + " of " + str(potential_left))

        if delete_after:
            if glob.glob(file.replace("png", "jpg")):
                delete_worked = False
                try:
                    delete_worked = True
                    os.remove(file)
                except OSError as ex:
                    delete_worked = False
                    print(ex)
                if delete_worked:
                    deleted_n = deleted_n + 1
                    print("- deleted original png")

    delete_str = "."
    if delete_after:
        delete_str = " and " + str(deleted_n) + " files were deleted afterwards."

    print("out of a possible " + str(total_n) + " files, " + str(converted_n) + " were converted" + delete_str)

def print_usage():
    print ("Usage:")
    print ("  python3 png2jpg.py")
    print ("    converts all unconverted PNGs to JPGs with 95 quality in the script folder")
    print ("  python3 png2jpg.py -d OR --delete")
    print ("    converts and also deletes all converted PNGs")
    print ("  python3 png2jpg.py -q OR --quality N")
    print ("    changes JPG quality from 20 to 100. Only applies to unconverted PNGs")
    print ("  python3 png2jpg.py -i OR -indir DIRECTORY_PATH")
    print ("    converts PNGs in the directory path given to JPGs")

if __name__ == "__main__":
    main(sys.argv[1:])