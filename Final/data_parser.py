import pypianoroll
import os, sys
from os.path import dirname, abspath, basename, exists, splitext, join
import numpy as np
from CONFIG import *

BEATS_PER_SET = BEATS_PER_BAR*NUM_BARS

def parse_data(genres_directory, parsed_directory):

    save_directory_name = "NT-" + str(NUM_TRACKS) + "-NB-" + str(NUM_BARS) + "-BPB-" + str(BEATS_PER_BAR) + "-NN-" + str(NUM_NOTES)
    save_directory_path = join(parsed_directory, save_directory_name)
    os.makedirs(save_directory_path, exist_ok=True)

    for genre in os.listdir(genres_directory):
        if genre in GENRE_LIST:
            print("\n\n\n\n")
            print(genre)
            print("\n\n\n\n")
            genre_directory = join(genres_directory, genre)
            for song in os.listdir(genre_directory):
                print(song)
                song_multitrack = pypianoroll.load(join(genre_directory, song))
                song_multitrack.pad_to_same()
                song_multitrack.pad_to_multiple(BEATS_PER_SET)
                song_divisions = int(((song_multitrack.tracks[0].pianoroll.size)/128)/(BEATS_PER_SET))

                for division in range(0, song_divisions):
                    track_list = []

                    for track in song_multitrack.tracks:
                        current_beat = division*(BEATS_PER_SET)
                        bar_list = []

                        for bar in range(0, 4):
                            beat_list = []

                            for beat in range(current_beat, current_beat+BEATS_PER_BAR):
                                beat_list.append(np.asarray(track.pianoroll[beat][LOWEST_NOTE:LOWEST_NOTE+NUM_NOTES]))

                            bar_list.append(np.asarray(beat_list))
                            current_beat += BEATS_PER_BAR

                        track_list.append(np.asarray(bar_list))

                    filename = genre + "-" + song.split(".")[0] + "-" + str(division)
                    filepath = join(save_directory_path, filename)

                    reshaped_track_list = np.reshape(np.asarray(track_list), (4, 96, 84, 5))
                    np.savez_compressed(filepath, data=np.asarray([reshaped_track_list, genre]))


def main():
    genre_directory = abspath(sys.argv[1])
    parsed_directory = abspath(sys.argv[2])
    parse_data(genre_directory, parsed_directory)

if __name__ == '__main__':
    main()
