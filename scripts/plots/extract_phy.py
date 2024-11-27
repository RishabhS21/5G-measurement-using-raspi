import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime
import re


# Transformation functions
def transform_rssi(value):
    if value == 255:
        return "unknown"
    return -120 + value


def transform_rsrp(value):
    if value == 255:
        return "unknown"
    return -140 + value


def transform_sinr(value):
    if value == 255:
        return "unknown"
    return -20 + (value * 0.2)


def transform_rsrq(value):
    if value == 255:
        return "unknown"
    return -19.5 + (value * 0.5)


def extract_phy_data(file_name, left=0, right=1e18):

    timestamps = []
    rssi_values = []
    rsrp_values = []
    sinr_values = []
    rsrq_values = []

    with open(file_name, "r") as file:
        for line in file:
            match = re.match(r"(\d+) -> \^HCSQ:\"LTE\",(\d+),(\d+),(\d+),(\d+)", line.strip())
            if not match:
                continue
            timestamp = int(match.group(1))
            if timestamp < left or timestamp > right:
                continue
            timestamps.append(datetime.fromtimestamp(timestamp))
            
            rssi_values.append(transform_rssi(int(match.group(2))))
            rsrp_values.append(transform_rsrp(int(match.group(3))))
            sinr_values.append(transform_sinr(int(match.group(4))))
            rsrq_values.append(transform_rsrq(int(match.group(5))))

    return timestamps, rssi_values, rsrp_values, sinr_values, rsrq_values


def plot_phy_data(file_name):

    plt.figure(figsize=(12, 6))

    small_marker = 2

    timestamps, rssi_values, rsrp_values, sinr_values, rsrq_values = extract_phy_data(file_name)

    plt.plot(timestamps, rssi_values, label="RSSI", color="blue", marker='o', markersize=small_marker)
    plt.plot(timestamps, rsrp_values, label="RSRP", color="green", marker='x', markersize=small_marker)
    plt.plot(timestamps, sinr_values, label="SINR", color="red", marker='s', markersize=small_marker)
    plt.plot(timestamps, rsrq_values, label="RSRQ", color="purple", marker='d', markersize=small_marker)

    plt.xlabel("Timestamp")
    plt.ylabel("Metric Values")
    plt.title("LTE Metrics Over Time")
    plt.legend()

    date_formatter = DateFormatter("%d-%m\n%H:%M")
    plt.gca().xaxis.set_major_formatter(date_formatter)

    plt.grid(True)
    plt.tight_layout()

    plt.show()

# plot_phy_data("hcsq.txt")
