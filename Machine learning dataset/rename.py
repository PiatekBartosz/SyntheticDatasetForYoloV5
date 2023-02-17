# program used to rename filenames to numbers in succession
import os

def main():
    folder = 'white50'
    for count, filename in enumerate(os.listdir(folder)):
        src = f'{folder}/{filename}'
        dst = f'{folder}/{str(count+1)}.jpg'
        print(src, " ", dst)
        if dst == src or not os.isdir(src):
            continue

        os.rename(src, dst)

main()