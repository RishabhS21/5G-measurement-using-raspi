import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime
import json
import re


default_date_format = "%d/%m\n%H:%M"


def extract_ping_data(file_name, left=0, right=1e18):
    timestamps = []
    ping_data = {}

    with open(file_name, "r") as file:
        for line in file:
            match = re.match(r"(\d+) -> (.+)", line.strip())
            if not match:
                continue
            timestamp = int(match.group(1))
            if timestamp < left or timestamp > right:
                continue
            data = json.loads(match.group(2))
            
            timestamps.append(datetime.fromtimestamp(timestamp))
            
            ping_latency = data["Measurements"]["ping_latency"]
            for key, value in ping_latency.items():
                if "rtt_avg_ms" in key:
                    website = key.split("_")[0]
                    if website not in ping_data:
                        ping_data[website] = []
                    ping_data[website].append(value)

    return timestamps, ping_data


def extract_hops_data(file_name, left=0, right=1e18):
    timestamps = []
    hops_data = {}

    with open(file_name, "r") as file:
        for line in file:
            match = re.match(r"(\d+) -> (.+)", line.strip())
            if not match:
                continue

            timestamp = int(match.group(1))
            if timestamp < left or timestamp > right:
                continue

            data = json.loads(match.group(2))
            
            timestamps.append(datetime.fromtimestamp(timestamp))
            
            hops_to_target = data["Measurements"]["hops_to_target"]
            for key, value in hops_to_target.items():
                target = key.split("_to_")[1]  # Extract the target name (e.g., "study.iitm.ac.in")
                if target not in hops_data:
                    hops_data[target] = []
                hops_data[target].append(value)
            
            for target in hops_data:
                if len(hops_data[target]) < len(timestamps):
                    hops_data[target].append(None)  # Fill missing data with None

    return timestamps, hops_data


def extract_dns_data(file_name, left=0, right=1e18):
    timestamps = []
    avg_latency = []
    max_latency = []

    with open(file_name, "r") as file:
        for line in file:
            match = re.match(r"(\d+) -> (.+)", line.strip())
            if not match:
                continue

            timestamp = int(match.group(1))
            if timestamp < left or timestamp > right:
                continue

            data = json.loads(match.group(2))
            timestamps.append(datetime.fromtimestamp(timestamp))
            
            dns_latency = data["Measurements"]["dns_latency"]
            avg_latency.append(dns_latency.get("dns_query_avg_ms", None))
            max_latency.append(dns_latency.get("dns_query_max_ms", None))

    return timestamps, avg_latency, max_latency


def extract_speedtest_data(file_name, left=0, right=1e18):
    timestamps = []
    download_speeds = []
    upload_speeds = []

    with open(file_name, "r") as file:
        for line in file:
            match = re.match(r"(\d+) -> (.+)", line.strip())
            if not match:
                continue
            timestamp = int(match.group(1))
            if timestamp < left or timestamp > right:
                continue
            data = json.loads(match.group(2))
            
            timestamps.append(datetime.fromtimestamp(timestamp))
            
            speedtest_data = data.get("speedtest_ookla", {})
            download_speeds.append(speedtest_data.get("download", None))
            upload_speeds.append(speedtest_data.get("upload", None))

    return timestamps, download_speeds, upload_speeds


def plot_ping(file_name):

    timestamps, ping_data = extract_ping_data(file_name)

    plt.figure(figsize=(12, 6))

    for website, values in ping_data.items():
        plt.plot(timestamps, values, label=f"{website} Avg RTT (ms)", marker='o', markersize=4)

    plt.xlabel("Timestamp")
    plt.ylabel("Ping Latency (ms)")
    plt.title("Ping Latency Over Time for Websites")
    plt.legend()

    date_formatter = DateFormatter(default_date_format)
    plt.gca().xaxis.set_major_formatter(date_formatter)

    plt.grid(True)
    plt.tight_layout()

    plt.show()


def plot_hops(file_name):

    timestamps, hops_data = extract_hops_data(file_name)

    plt.figure(figsize=(12, 6))

    for target, values in hops_data.items():
        plt.plot(timestamps, values, label=f"{target} Hops", marker='o', markersize=4)

    plt.xlabel("Timestamp")
    plt.ylabel("Number of Hops")
    plt.title("Hops to Target Over Time")
    plt.legend()

    date_formatter = DateFormatter(default_date_format)
    plt.gca().xaxis.set_major_formatter(date_formatter)

    plt.grid(True)
    plt.tight_layout()

    plt.show()


def plot_dns_latency(file_name):

    timestamps, avg_latency, max_latency = extract_dns_data(file_name)

    plt.figure(figsize=(12, 6))

    plt.plot(timestamps, avg_latency, label="Average DNS Latency (ms)", marker='o', markersize=4, color='blue')
    plt.plot(timestamps, max_latency, label="Maximum DNS Latency (ms)", marker='x', markersize=4, color='red')

    plt.xlabel("Timestamp")
    plt.ylabel("DNS Latency (ms)")
    plt.title("DNS Latency Over Time")
    plt.legend()

    date_formatter = DateFormatter(default_date_format)
    plt.gca().xaxis.set_major_formatter(date_formatter)

    plt.grid(True)
    plt.tight_layout()

    plt.show()


def plot_speedtest(file_name):

    timestamps, download_speeds, upload_speeds = extract_speedtest_data(file_name)

    plt.figure(figsize=(12, 6))

    plt.plot(timestamps, download_speeds, label="Download Speed (Mbps)", marker='o', markersize=4, color='blue')
    plt.plot(timestamps, upload_speeds, label="Upload Speed (Mbps)", marker='x', markersize=4, color='green')

    plt.xlabel("Timestamp")
    plt.ylabel("Speed (Mbps)")
    plt.title("Speedtest Download and Upload Speeds Over Time")
    plt.legend()

    date_formatter = DateFormatter(default_date_format)
    plt.gca().xaxis.set_major_formatter(date_formatter)

    plt.grid(True)
    plt.tight_layout()

    plt.show()


# plot_ping("ping.txt")
# plot_hops("hops.txt")
# plot_dns_latency("dns_latency.txt")
# plot_speedtest("speedtest.txt")
