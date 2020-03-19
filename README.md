# png2jpg
A script to convert pngs in a folder to jpgs, mainly for video game screenshot folders.

Requires python3 and Pillow forked from Python Imaging Library (PIL)
* https://www.python.org/downloads/
* https://pypi.org/project/Pillow/

Usage:
> python3 png2jpg.py

Will gather all the PNGs in the same directory as the script and convert them to JPGs at 95% quality. The converted PNGs will not be deleted afterwards.

> python3 png2jpg.py -i ./Screenshots/ -q 50 -d

Will gather all the PNGs in ./Screnshots/ and convert them to JPGs at 50% quality, then delete the PNGs. When using -d, any PNG that has a corresponding JPG will be deleted.

If a PNG already has a JPG version when running the script, the conversion will be skipped. It will still delete converted PNGs if you have that option turned on.

-d can be --delete

-q can be --quality

-i can be --indir

-h will print the usage.
