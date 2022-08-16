#! /bin/bash

file="skripts/batteryNow"

echo "$(cat /sys/class/power_supply/BAT0/capacity)%" > $file

skripts/today.sh
