# program used to rename filenames to numbers in succession
import os

def main():
    folders = ['white80circ','white80rect','black80circ','black80rect',]
    for folder in folders:
        for count, filename in enumerate(os.listdir(folder)):
            src = f'{folder}/{filename}'
            dst = f'{folder}/{str(count+1)}.jpg'
            print(src, " ", dst)
            if dst == src:
                continue

            os.rename(src, dst)

main()