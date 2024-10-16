#!/usr/bin/env python3
#
# timecode_renamer
#
# Renames Quicktime .mov file based on embedded SMPTE timecode
#

import os
import argparse
from pathlib import Path
import pathlib
from pymediainfo import MediaInfo

parser = argparse.ArgumentParser()
parser.add_argument('sourcefile', type=pathlib.Path)
args = parser.parse_args()
sourcefile = args.sourcefile
sourcefile_basename = pathlib.Path(sourcefile).stem
sourcefile_ext = pathlib.Path(sourcefile).suffix
outpath = os.path.dirname(sourcefile)
 
mediainfo = MediaInfo.parse(sourcefile)

for track in mediainfo.tracks:
    if track.track_type == "Other":
        start_tc = track.time_code_of_first_frame
        end_tc = track.time_code_of_last_frame

renamed_file = sourcefile_basename + "_" + start_tc.replace(':','') + "-" + end_tc.replace(':','') + sourcefile_ext

os.rename(sourcefile, outpath + "/" + renamed_file)
