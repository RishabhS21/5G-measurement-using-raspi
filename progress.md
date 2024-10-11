## Progress Report

### Paper Reference
We referred to a similar study conducted in the US and Europe to get the motivation, [link](https://dl.acm.org/doi/pdf/10.1145/3651890.3672269?casa_token=GB67T6_EHC8AAAAA:qeLermuYy7oD_QQ4_meiz64_3cNygEVIlDFAkTHKe-wcmxrU4kD3hoMwBXZJ7HFOrHbR9sUHnYFclg), which aligns closely with the objectives of our project.

### Application Layer Data
We used the Netrics tool ([repository](https://github.com/internet-equity/netrics)) to collect application layer data, including metrics such as ping, DNS latency, and other measurements for various endpoints. 

### Hardware Selection: LTE Dongle
Since there were no 5G dongles available in the market, we opted for an Amazon Basics LTE dongle featuring the Qualcomm MSM8916 chipset. This dongle was chosen because it had Qualcomm chipset, whose resources are vast on internet. We believe that if we succeed in setting up this device, the process for 5G devices will be smoother in the future.

### Initial Measurements
After connecting the dongle via USB to the Raspberry Pi, we ran Netrics to obtain some basic network performance measurements, [here](./netrics.md). However, for physical layer data collection, we encountered a blocker.

### Physical Layer Measurements: Blocker with qcsuper
To get physical layer measurements, we planned to use the `qcsuper` tool ([link](https://medium.com/@googler_ram/open-source-lte-5g-packet-capture-tool-4bd3d360aa0)). However, we are currently unable to enable diagnostic mode on this device. Here are the methods we have tried so far:

- **Method 1: ttyUSBx Issue**  
  We referred to [this](https://forums.raspberrypi.com/viewtopic.php?t=160400) article from the official discussion forum of raspi which suggest a method to get the ttyUSBx as we are also getting ttyx options only which is unexpected

- **Method 2: Modems not found**  
  Running `mmcli -L` shows "No modems found," indicating that the OS is not detecting the dongle as a modem. We are currently unable to switch it to modem mode. We're following guidance from [this article](https://wiki.archlinux.org/title/Mobile_broadband_modem).

- **Method 3: QMI Interface**  
  We attempted to set up a data connection over the QMI interface using `libqmi`, where we expected the driver to be `qmi_wwan`. However, it is showing up as `rndis_host`. We tried following [this article](https://solidrun.atlassian.net/wiki/spaces/developer/pages/326631427/Setting+up+a+data+connection+over+QMI+interface+using+libqmi), but it did not resolve the issue.

### Next Steps
- **Custom Firmware**  
  We are exploring the option of flashing custom firmware to the modem to gain more control over the device. We are referring to this guide for more information: [Liliputing Article on Hacking LTE Modems](https://liliputing.com/this-dirt-cheap-4g-lte-modem-on-a-usb-stick-can-be-hacked-to-run-mainline-linux/).

- **Exploring Better Dongle Options**  
  Since the current device appears to be difficult to hack, we are also considering alternative dongles that may offer better support and flexibility for our project.
