#!/usr/bin/python
#renames files to their parent folder name

import os, sys
from os.path import dirname, abspath, basename, exists, splitext
from os.path import join as joinPath
import json
from shutil import copyfile

GENRE_AMOUNT = 100 #sorts only for 100 most popular genres in lastfm dataet

def flattenFiles(here):
    for root, dirs, files in os.walk(here, topdown=False):
        if root != here:
            for name in files:
                source = joinPath(root, name)
                target = joinPath(here, basename(root) + ".npz")
                if exists(target):
                    os.remove(target)
                os.rename(source, target)

        for name in dirs:
            os.rmdir(joinPath(root, name))


def sorter(song_folder, info_folder, sorted_folder, tags_file):
    info_folder_list = os.listdir(info_folder)

    #import list of tags that are desired from stripped lastfm file
    with open(tags_file) as file:
        tags_list = file.read().splitlines()
        for i in tags_list:
            tags_list[i] = tags_list[i].split(" ")[0]

        tags_list = tags_list[:GENRE_AMOUNT]

    #run through list of songs that we can from lpd_5_cleansed list that was stripped to only songs that we have info for usinf strip.py
    for file in os.listdir(song_folder):
        #find corresponding info file for songs npz file
        song_msd = file.split(".")[0]
        song_msd = song_msd + ".json"
        song_msd_path = joinPath(info_folder, song_msd)

        #check to see if there is an info file for the song that is being checked
        if song_msd in info_folder_list:
            #open json file
            with open(song_msd_path) as info_json:
                parsed_info = json.load(info_json)
                #find tags (genres) from json file
                info_tags = parsed_info['tags']

                #check if current tag is part of desired tags list
                for tag in info_tags:
                    genre = tag[0]

                    if genre in tags_list:
                        #clean genre string for placing into folders
                        genre = genre.lower().replace(" ", "_")
                        genre_folder_path = joinPath(sorted_folder, genre)

                        #make folder for genre if it doesnt exist
                        if not os.path.isdir(genre_folder_path):
                            os.makedirs(genre_folder_path)

                        #copy each song to every desired genre's folder that it is tagged as
                        source = joinPath(song_folder, file)
                        target = joinPath(genre_folder_path, file)
                        copyfile(source, target)


if __name__=='__main__':
    song_folder = abspath(sys.argv[1])
    info_folder = abspath(sys.argv[2])
    sorted_folder = abspath(sys.argv[3])
    tags_file = abspath(sys.argv[4])

    flattenFiles(song_folder)
    flattenFiles(info_folder)

    sorter(song_folder, info_folder, sorted_folder, tags_file)
