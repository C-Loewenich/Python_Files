# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line

import os
import shutil
from zipfile import ZipFile

root_path = os.getcwd()
cache_path = os.path.join(root_path, "files\cache")
zip_path = os.path.join(root_path, "files\data.zip")

print(cache_path)

def clean_cache():
    #Creates the cache folder and if it already exist catch the error in stead clear the folder.
    """ try: #This is a good optoin if it is important to keep the folder.
        os.mkdir(cache_path)
        print("Cache folder created")
    except FileExistsError:
        print("Cache folder already exist - Cleared cache!")
        for file in os.listdir(cache_path):
            path_to_delete = os.path.join(cache_path, file)
            try:
                shutil.rmtree(path_to_delete)
            except OSError:
                os.remove(path_to_delete) """
    if os.path.exists(cache_path): #this is a better option if the folder does not spelicit needs remain a part of the tree.
        print("Cache exist - Cache directory deleted")
        shutil.rmtree(cache_path)
    os.mkdir(cache_path)
    print("Cache directory created")


def cache_zip(zip_path, cache_path):
    #Unpack the Zip File and copies contained files to the cache folder.
    with ZipFile(zip_path, "r") as zObject:
        zObject.extractall(cache_path)
    print("Files unpacked and moved to cache")


def cached_files():
    #Lists the files in the cache.
    absolute_path_list = []
    for file in os.listdir(cache_path):
        absolute_path_list.append(os.path.join(cache_path, file))
    return absolute_path_list


def find_password(file_list):
    #Finds the document that contains the word password and extracts the actual password from the string.
    search_string = "password"
    for file_path in file_list:
        try:
            with open(file_path) as file:
                for line in file:
                    if search_string in line:
                        words = line.split(" ")
                        for i in range(len(words)): #iterates each word in string
                            if search_string in words[i]: #if the searchstring is in that word (this way it has no influence if the current word is password, password: or password=)
                                return words[i+1].replace("\n", "") #it returns the next word in the string and remove an possible line break.
        except:
            print("An error occured!")
    return "no password found"


if __name__ == '__main__':
    clean_cache()
    cache_zip(zip_path, cache_path)
    print(find_password(cached_files()))
