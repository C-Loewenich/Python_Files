# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line

import os
import shutil
from zipfile import ZipFile

def main():
    clean_cache()
    cache_zip(r"C:\Users\Casper\WincBackend\files\data.zip", r"C:\Users\Casper\WincBackend\files\cache")
    #print(cached_files())
    print(find_password(cached_files()))


def clean_cache():
    cache_path = "./files/cache"
    try:
        os.mkdir(cache_path)
        print("Cache folder created")
    except FileExistsError:
        print("Cache folder already exist - Cleared cache!")
        for file in os.listdir(cache_path):
            path_to_delete = os.path.join(cache_path, file)
            try:
                shutil.rmtree(path_to_delete)
            except OSError:
                os.remove(path_to_delete)


def cache_zip(zip_path, cache_path):
    #???# is there a way to chagne the strings in to raw strings by use of a function so r does not need to be entered in the parameters. would make user input easier. tried to use repr() but could not get it to work. can of course change every \ in to \\ or / but find it very messy.
    with ZipFile(zip_path, "r") as zObject:
        zObject.extractall(cache_path)
    print("Files unpacked and moved to cache")


def cached_files():
    cache_path = r"C:\Users\Casper\WincBackend\files\cache"
    absolute_path_list = []
    for file in os.listdir(cache_path): #???# is there a way to iterate over the list in a mutable manner so i dont have to crate and append to the absolute_path_list but simply can place a return statement in front of the iteration and threby clean up the code
        absolute_path_list.append(os.path.join(cache_path, file))
    return absolute_path_list


def find_password(file_list):
    search_string = "password"
    for file_path in file_list:
        try:
            file = open(file_path)
            text = file.read()
            #file.close() #???# Does it give sence to close the file again in order to save memory?
            index = text.find(search_string)
            if index >= 0:
                text_lines = text.splitlines()
                for line in text_lines:
                    if search_string in line:
                        words = line.split(" ")
                        for i in range(len(words)):
                            if search_string in words[i]:
                                return words[i+1]
        except:
            print("An error occured!")
    return "no password found"


if __name__ == '__main__':
    main()

