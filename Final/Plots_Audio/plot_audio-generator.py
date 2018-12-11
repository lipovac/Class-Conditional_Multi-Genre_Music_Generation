import pypianoroll
from pypianoroll.plot import plot_multitrack
import argparse
import os
import sys
from os.path import join, abspath
from midi2audio import FluidSynth

##REQUIRES FluidR3_GM.sf2 in same directory!! https://osdn.net/frs/g_redir.php?m=kent&f=androidframe%2Fsoundfonts%2FFluidR3_GM.sf2

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('-o', '--output')
    parser.add_argument('-p', '--savepath')

    args = parser.parse_args()

    return args
def main():
    args = parser()
    pypianoroll_file = abspath(args.input_file)
    loaded = pypianoroll.load(pypianoroll_file)

    if args.savepath is None:
        savepath = os.getcwd()
    else:
        savepath = args.savepath
        os.makedirs(savepath, exist_ok=True)

    #Save to plot
    if args.output is None:
        output_filename = os.path.basename(pypianoroll_file).split(".")[0]
        output_filename = join(savepath, output_filename)
    else:
        output_filename = ags.output
        output_filename = join(savepath, output_filename)

    print(output_filename)

    plot_multitrack(loaded, filename=output_filename+".pdf", preset="frame")

    #Save to WAV
    pypianoroll.write(loaded, (output_filename+".mid"))

    fs = FluidSynth('FluidR3_GM.sf2')
    fs.midi_to_audio((output_filename+".mid"), (output_filename+".wav"))


if __name__ == "__main__":
    main()
