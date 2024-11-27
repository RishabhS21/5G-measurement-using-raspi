import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from extract_phy import extract_phy_data
from extract_net import extract_ping_data, extract_hops_data, extract_dns_data, extract_speedtest_data


def truncate_list(L):
    return L[::5]



def calculate_correlation(timestamps1, timestamps2, values1, values2):
    # Convert timestamps to numpy datetime64 for easy manipulation
    np_timestamps1 = np.array(timestamps1, dtype='datetime64')
    np_timestamps2 = np.array(timestamps2, dtype='datetime64')

    interpolated_values = np.interp(
        np_timestamps2.astype('float'),
        np_timestamps1.astype('float'),  # Convert datetime64 to float for interpolation
        values1
    )

    correlation, p_value = pearsonr(interpolated_values, values2)

    return correlation, p_value


time_start = 1731788826 # start Unix timestamps in seconds
time_end = 1731987952 # end Unix timestamps in seconds
folder = "."


phy_timestamps, rssi_values, rsrp_values, sinr_values, rsrq_values = extract_phy_data(f"{folder}/hcsq.txt", time_start, time_end)
ping_timestamps, ping_data = extract_ping_data(f"{folder}/ping.txt", time_start, time_end)
hops_timestamps, hops_data = extract_hops_data(f"{folder}/hops.txt", time_start, time_end)
dns_timestamps, avg_latency, max_latency = extract_dns_data(f"{folder}/dns_latency.txt", time_start, time_end)
speed_timestamps, download_speeds, upload_speeds = extract_speedtest_data(f"{folder}/speedtest.txt", time_start, time_end)

small_marker = 2
medium_marker = 4

# phy_timestamps = truncate_list(phy_timestamps)
# rssi_values = truncate_list(rssi_values)
# rsrp_values = truncate_list(rsrp_values)
# sinr_values = truncate_list(sinr_values)
# rsrq_values = truncate_list(rsrq_values)

plt.plot(phy_timestamps, rssi_values, label="RSSI", color="blue", marker='o', markersize=small_marker)
plt.plot(phy_timestamps, rsrp_values, label="RSRP", color="green", marker='x', markersize=small_marker)
plt.plot(phy_timestamps, sinr_values, label="SINR", color="red", marker='s', markersize=small_marker)
plt.plot(phy_timestamps, rsrq_values, label="RSRQ", color="purple", marker='d', markersize=small_marker)

target_website = 'study.iitm.ac.in'
ping_latencies = ping_data[target_website]
# plt.plot(ping_timestamps, ping_latencies, label=f"{target_website} Avg RTT (ms)", marker='o', markersize=small_marker)
# plt.plot(ping_timestamps, ping_data['psl.eu'], label="psl.eu Avg RTT (ms)", marker='o', markersize=small_marker)

for website, values in ping_data.items():
    plt.plot(ping_timestamps, values, label=f"{website} Avg RTT (ms)", marker='o', markersize=small_marker)

for target, values in hops_data.items():
    plt.plot(hops_timestamps, values, label=f"{target} Hops", marker='o', markersize=small_marker)

plt.plot(dns_timestamps, avg_latency, label="Average DNS Latency (ms)", marker='o', markersize=small_marker)
plt.plot(dns_timestamps, max_latency, label="Maximum DNS Latency (ms)", marker='x', markersize=small_marker)

plt.plot(speed_timestamps, download_speeds, label="Download Speed (Mbps)", marker='v', markersize=medium_marker)
plt.plot(speed_timestamps, upload_speeds, label="Upload Speed (Mbps)", marker='^', markersize=medium_marker)

# Calculate the correlation, change as per your requirement
# ps_correlation, ps_p_value = calculate_correlation(ping_timestamps, speed_timestamps, ping_latencies, download_speeds)
# print(f"Correlation between ping and download speed: {ps_correlation:.3f}")
# print(f"P-value: {ps_p_value:.3e}")

# rs_correlation, rs_p_value = calculate_correlation(phy_timestamps, speed_timestamps, rssi_values, download_speeds)
# print(f"Correlation between RSSI and download speed: {rs_correlation:.3f}")
# print(f"P-value: {rs_p_value:.3e}")

# rp_correlation, rp_p_value = calculate_correlation(phy_timestamps, ping_timestamps, rssi_values, ping_latencies)
# print(f"Correlation between RSSI and ping: {rp_correlation:.3f}")
# print(f"P-value: {rp_p_value:.3e}")

# correlation, p_value = calculate_correlation(phy_timestamps, phy_timestamps, rssi_values, sinr_values)
# print(f"Correlation between RSSI and SINR: {correlation:.3f}")
# print(f"P-value: {p_value:.3e}")

# correlation, p_value = calculate_correlation(phy_timestamps, speed_timestamps, sinr_values, download_speeds)
# print(f"Correlation between SINR and download speed: {correlation:.3f}")
# print(f"P-value: {p_value:.3e}")

# correlation, p_value = calculate_correlation(phy_timestamps, ping_timestamps, sinr_values, ping_latencies)
# print(f"Correlation between SINR and ping: {correlation:.3f}")
# print(f"P-value: {p_value:.3e}")


plt.xlabel("Timestamp")
plt.ylabel("Metric Values")
plt.title("Static Scenario")
plt.legend()

date_formatter = DateFormatter("%d/%m\n%H:%M")
plt.gca().xaxis.set_major_formatter(date_formatter)

plt.grid(True)
plt.tight_layout()

plt.show()
