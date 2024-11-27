# AT Commands Details
Let's analyze each command we ran along with its output and what each means:

1. **[AT^HCSQ?](https://usermanual.wiki/Huawei/HUAWEIME909sSeriesLTEModuleATCommandInterfaceSpecificationV100R00103Englishpdf.267489792.pdf)**  
   - The response format is:  
     ```
     ^HCSQ: <sysmode>[,<value1>[,<value2>[,<value3>[,<value4>]]]]

     OK
     ```  
   - Example Output: `^HCSQ:"LTE",50,48,131,26`  
   - **Explanation:** This command provides critical metrics to assess signal strength. The parameters include:  
     - **System Mode (sysmode):** Indicates the network mode (e.g., LTE in this example).  
     - **Value1 (rssi):** Indicates the Received Signal Strength Indicator (RSSI).  
     - **Value2 (rsrp):** Reference Signal Received Power.  
     - **Value3 (sinr):** Signal-to-Interference-plus-Noise Ratio.  
     - **Value4 (rsrq):** Reference Signal Received Quality.  

   - **RSSI Explanation:**  
     RSSI represents integer values corresponding to the received signal strength. More negative, weak signal.

     | Code | RSSI Range                    |
     |------|-------------------------------|
     | 0    | rssi < -120 dBm               |
     | 1    | -120 dBm ≤ rssi < -119 dBm    |
     | 2    | -119 dBm ≤ rssi < -118 dBm    |
     | ...  |                               |
     | 94   | -27 dBm ≤ rssi < -26 dBm      |
     | 95   | -26 dBm ≤ rssi < -25 dBm      |
     | 96   | -25 dBm ≤ rssi                |
     | 255  | Unknown or undetectable       |
     
   - **RSRP Explanation:**  
     RSRP is a metric used to measure the power of a cell tower's reference signal in LTE networks. It's a key indicator of signal quality and level in modern LTE networks. More negative, weak signal.

     | Code | RSRP Range                    |
     |------|-------------------------------|
     | 0    | rsrp < -140 dBm               |
     | 1    | -140 dBm    |
     | 2    | -139 dBm    |
     | ...  |                               |
     | 95   | -46 dBm       |
     | 96   | -45 dBm |
     | 97   | -44 dBm ≤ rssi                |
     | 255  | Unknown or undetectable       |
     
   - **SINR Explanation:**  
     SINR an integer type value that indicates the signal to interference plus noise ratio. More negative, more the interferance and noise in the signal.
     | Code | SINR Range                     |
     |------|--------------------------------|
     | 0    | sinr < -20 dB                 |
     | 1    | -20 dB ≤ sinr < -19.8 dB      |
     | 2    | -19.8 dB ≤ sinr < -19.6 dB    |
     | ...  |                                |
     | 249  | 29.6 dB ≤ sinr < 29.8 dB      |
     | 250  | 29.8 dB ≤ sinr < 30 dB        |
     | 251  | 30 dB ≤ sinr                  |
     | 255  | Unknown or undetectable       |
     
   - **RSRQ Explanation:**  
     RSRQ an integer type value that indicates the reference signal received quality in dB. More negative, weaker the signal quality.
     | Code | SINR Range                     |
     |------|--------------------------------|
     | 0    | rsrq < -19.5 dB                 |
     | 1    | -19.5 dB ≤ rsrq < -19 dB      |
     | 2    | -19 dB ≤ rsrq < -18.5 dB   |
     | ...  |                                |
     | 32  | -4 dB ≤ rsrq < -3.5 dB      |
     | 33  | -3.5 dB ≤ rsrq < -3 dB        |
     | 34  | -3 dB ≤ rsrq                  |
     | 255  | Unknown or undetectable       |  
   

1. **[AT+CSQ](https://m2msupport.net/m2msupport/atcsq-signal-quality/)**
   - The response looks like:
     ```
     +CSQ: <received signal strength (rssi)>,<channel bit error rate (ber)>
     
     OK
     ```
   - Output: `+CSQ: 24,99`
   - **Explanation:** This command queries the signal quality. The first value (24) is the received signal strength indication (RSSI of -65dBm, Excellent quality) on a scale of 0-31, where higher numbers mean better signal quality. The second value (99) indicates a quality value not known or not detectable.

4. **[AT^U2DIAG](https://m2msupport.net/m2msupport/atu2diag-set-the-device-mode/)**
   - Output: `ERROR`
   - **Explanation:** This command is typically used to set the modem’s diagnostic mode (`0` set for modem only mode, `1` set for modem+cdrom). An `ERROR` response suggests that either this command disabled in our modem's firmware.

11. **[AT^SYSINFO](https://m2msupport.net/m2msupport/atsysinfo-get-the-system-mode/)**
    - Output: `^SYSINFO: 2,3,0,5,1,0,4`
    - **Explanation:** These commands provide system information. The output includes details on network state, mode, and current connection type. For example, "LTE" indicates the modem is connected to an LTE network.

14. **[AT+COPS?](https://onomondo.com/blog/at-command-cops/#at-cops)**
    - The response will have the syntax:
      ```
      +COPS: [selection mode],[operator format],[operator],[radio access technology]
      OK
      ```
    - Output: `+COPS: 0,0,"airtel",7`
    - **Explanation:** This command queries the network operator. The selection mode is 0, which means automatic, and the radio access technology is 7, which means E-UTRAN, the identifier for LTE.

These all have been a few of IMPORTANT AT commands supported by our device (HUAWEI E3372h) but we mainly have focused on HCSQ as it has provided all the crucial metric in single run.
