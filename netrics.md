# Netrics: Overview and Use Case

[Netrics](https://github.com/internet-equity/netrics) is a network measurement execution framework designed to log and analyze network-layer metrics efficiently. Using Netrics, we can perform various network diagnostics such as ping tests, DNS latency checks, hop analysis, and speed tests. 

To install Netrics on a Raspberry Pi, we utilized the `pip` method from the repository, combined with a Python virtual environment (`venv`) to prevent version conflicts. This setup allowed us to use commands like `netrics-ping`, `netrics-hops`, etc. However, the default destinations for measurements were set to `google.com`, `facebook.com`, and `nytimes.com`. We updated these destinations in the file located at `src/netrics/measurement/common/connectivity/default.py` to `study.iitm.ac.in` and `psl.eu`, corresponding to servers located in Chennai (India) and Paris (France), respectively. Among these, the focus was placed on `study.iitm.ac.in` as it is geographically closer and relevant to our use case in India.

---

## Utilities Used

1. **netrics-ping:**  
   Measures network latency to a specified destination by sending ICMP packets and analyzing the response time.  

2. **netrics-dns-latency:**  
   Evaluates the time taken to resolve DNS queries for a given domain.  

3. **netrics-hops:**  
   Identifies the number of intermediate nodes (hops) and measures latency across the path to the destination.  

4. **netrics-speed-ookla:**  
   Conducts network speed tests (upload and download speeds) using the Ookla framework.  

---

## Data Collection

- Installed essential network utilities that were not pre-installed on the Raspberry Pi, ensuring compatibility with Netrics.  
- Developed a [shell script](/script/net_script.sh) to automate the execution of network measurement commands across various scenarios, including:  
  - **Static environments:** When the device was stationary.  
  - **Moving environments:** While the device was mobile.  
  - **Crowded environments:** In locations with high network congestion.  

This ensured comprehensive data collection across different conditions.

---

## Data Analysis

- Gathered data from Netrics commands across all scenarios and conducted an in-depth analysis.  
- Focused on understanding correlations between network-layer metrics (like latency and throughput) and physical-layer conditions (like RSSI, SINR, RSRP and RSRQ).  
- Generated plots to visualize trends and relationships. The visualizations are available [here](/plots).

---

## Challenges Faced

1. **Gateway Inaccessibility Error:**  
   - While using the dongle, an error stating `network gateway inaccessible` occurred. This issue stemmed from the `check_requirements` function in `src/netrics/measurement/common/connectivity/decorator.py`.  
   - To resolve this, we temporarily commented out lines 97-115 in the file, which contained gateway checks causing the failure.  

2. **Running netrics-speed-ookla:**  
   - The Ookla speed test required specific prerequisites to be met. The documentation in the Netrics README was insufficient, so we had to manually inspect the file `src/netrics/measurement/ookla.py` to ensure proper configuration.  

3. **Missing traceroute.py:**  
   - The `traceroute` functionality was non-operational as the `traceroute.py` file was missing from `src/netrics/measurement`. This issue has been reported in the [Netrics repository](https://github.com/internet-equity/netrics/issues/57).
