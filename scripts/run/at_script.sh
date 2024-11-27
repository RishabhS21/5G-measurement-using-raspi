#!/bin/bash

timeout_duration=3

sleep_duration=2

# change the path accordingly to save your logs
output_file1="/home/raspi/logs/cerrsi.txt"
output_file2="/home/raspi/logs/hcsq.txt"
output_file3="/home/raspi/logs/csq.txt"
output_file4="/home/raspi/logs/csnr.txt"

while true; do
    timestamp=$(date +%s)

    cerrsi_output=$(timeout "$timeout_duration" bash -c 'echo AT^CERSSI? | sudo socat - /dev/ttyUSB2,crnl' | grep "\^CERSSI")
    if [ -n "$cerrsi_output" ]; then
        echo "$timestamp -> $cerrsi_output" >> "$output_file1"
    fi

    hcsq_output=$(timeout "$timeout_duration" bash -c 'echo AT^HCSQ? | sudo socat - /dev/ttyUSB2,crnl' | grep "\^HCSQ")
    if [ -n "$hcsq_output" ]; then
        echo "$timestamp -> $hcsq_output" >> "$output_file2"
    fi

    csq_output=$(timeout "$timeout_duration" bash -c 'echo AT+CSQ | sudo socat - /dev/ttyUSB2,crnl' | grep "+CSQ")
    if [ -n "$csq_output" ]; then
        echo "$timestamp -> $csq_output" >> "$output_file3"
    fi

    csnr_output=$(timeout "$timeout_duration" bash -c 'echo AT^CSNR? | sudo socat - /dev/ttyUSB2,crnl' | grep "\^CSNR")
    if [ -n "$csnr_output" ]; then
        echo "$timestamp -> $csnr_output" >> "$output_file4"
    fi

    sleep "$sleep_duration"
done
