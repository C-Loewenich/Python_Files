# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line

import os
import shutil
from zipfile import ZipFile

root_path = os.getcwd()
cache_path = os.path.join(root_path, "files/cache")
zip_path = os.path.join(root_path, "files/data.zip")


def clean_cache():
    #Creates the cache folder and if it already exist catch the error in stead clear the folder.
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
    #Unpack the Zip File and copies contained files to the cache folder.
    with ZipFile(zip_path, "r") as zObject:
        zObject.extractall(cache_path)
    print("Files unpacked and moved to cache")


def cached_files():
    #Lists the files in the cache.
    cache_path = r"C:\Users\Casper\WincBackend\files\cache"
    absolute_path_list = []
    for file in os.listdir(cache_path):
        absolute_path_list.append(os.path.join(cache_path, file))
    return absolute_path_list


def find_password(file_list):
    #Finds the document that contains the word password and extracts the actual password from the string.
    ## I choose to do it this way because i did not want to expect that there was an ":" after the password. With this option the only recuriment is that the actual password is stated after the word "password". but this option is of course a few more lines of code.
    search_string = "password"
    for file_path in file_list:
        try:
            file = open(file_path)
            text = file.read()
            file.close()
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
    clean_cache()
    cache_zip(zip_path, cache_path)
    print(find_password(cached_files()))
