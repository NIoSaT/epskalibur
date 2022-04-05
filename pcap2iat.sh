#!/usr/bin/env bash

echo "IAT" > $1.csv
tshark -r $1 -e frame.time_delta -Tfields >> $1.csv
