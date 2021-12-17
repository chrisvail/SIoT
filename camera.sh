#!/usr/bin/env bash
TSTAMP=$(date +"%Y%m%d%H%M")
DEVICE="001"
fswebcam -r 1280x720 D${DEVICE}${TSTAMP}.jpg

