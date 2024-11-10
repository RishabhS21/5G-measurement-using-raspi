## Progress Report

In this file we discuss the progress made towards the project, as outlined in the [README](./README.md) file of this repository.

### Paper Reference
We referred to a similar study conducted in the US and Europe to get the motivation, [link](https://dl.acm.org/doi/pdf/10.1145/3651890.3672269?casa_token=GB67T6_EHC8AAAAA:qeLermuYy7oD_QQ4_meiz64_3cNygEVIlDFAkTHKe-wcmxrU4kD3hoMwBXZJ7HFOrHbR9sUHnYFclg), which aligns closely with the objectives of our project.

### USB Dongle Selection
Since, we had no options available for 5G dongles available in the indian market, we opted for an Amazon Basics LTE dongle featuring the Qualcomm MSM8916 chipset. This dongle was chosen because it had Qualcomm chipset, which was supposed to be easily hackable with wide resourecs available to get low level measurements. We believe that if we succeed in setting up this LTE device, the process for 5G devices will be smoother in the future.

### Initial Measurements
While our primary goal is to collect the physical layer measurements but we used a tool called [Netrics](https://github.com/internet-equity/netrics) to collect the application layer data, including metrics such as ping, DNS latency, and other measurements for various endpoints.  This setup was done to initiate the project and get the raspberry setup running and connecting to the internet using dongle. After connecting the dongle via USB to the Raspberry Pi 4, we ran Netrics to obtain some basic network performance measurements, [here](./netrics.md). However, for physical layer data collection, we encountered a major blocker.

### Physical Layer Measurements: Blocker with qcsuper
To get physical layer measurements, we planned to use [QCSuper](https://www.p1sec.com/blog/release-qc-super-v2), a tool which enables, for research purposes, to capture the contents of radio communication exchanges between your phone's antenna and your Mobile Operator's radio network (RAN). However, following the readme file of QCSuper's repository we failed to create the PCAP file with the measurement logs. 
```
qcsuper --usb-modem 05c6:9024 --wireshark-live
> [ERROR @ main.py:125] No Qualcomm Diag interface was found with the specified criteria. Please be more specific.
```
The command above would have created a PCAP file and will have analyzed by wireshark but it failed even after specifying vendor ID:product ID giving the error stated above. Below are the methods we attempted to enable diagnostic mode on this dongle:

- **Method 1: ttyUSBx Issue**  
  In Linux, `/dev/ttyUSBx` represents a USB serial port, crucial for network measurement tools to communicate with and control USB dongles. This access enables sending AT commands and retrieving diagnostic data necessary for accurate measurements. We could have been more specific to qcsuper command by providing it the USB serial port but since our device was not getting detected as ttyUSB we referred to [this](https://forums.raspberrypi.com/viewtopic.php?t=160400) article from the official discussion forum of raspi which suggest a method to get the ttyUSBx created. It didn't work!! Refered to many more discussions found on web but nothing worked.
  
- **Method 2: Modems not found**  
  We observed that our device is identified as a storage device and running `mmcli -L` shows "No modems found", indicating that the OS is not detecting the dongle as a modem. We are currently unable to switch it to modem mode. We followed guidance from [this article](https://wiki.archlinux.org/title/Mobile_broadband_modem) and other resources on using `usb_modeswitch`, including [this guide](https://forums.balena.io/t/using-usb-modeswitch-to-enable-4g-usb-modem/554) and [this thread](https://askubuntu.com/questions/1336221/how-to-use-usb-modeswtich-to-turn-my-4g-dongle-from-mass-storage-mode-to-modem-m) but none were effective with our dongle. These links gave an idea that we may use HUAWEI dongles.

- **Method 3: Data Connection over QMI Interface**  
  While exploring the solutions we found an [article](https://medium.com/slice-of-pi-innovations-hacks/setting-up-a-data-connection-via-qmi-interface-on-raspberry-pi-with-quectel-modem-and-sixfab-shield-aa2b2b3f3d5c) where it had the driver of the dongle as `qmi_wwan` and ultimately using the AT commands, which also could be helpful to get the lower level measurement of network. But since our dongle was showing the driver as `rndis_host`. We tried this [method](https://solidrun.atlassian.net/wiki/spaces/developer/pages/326631427/Setting+up+a+data+connection+over+QMI+interface+using+libqmi) to load the `qmi_wwan` kernel, but it again did not work.

All attempts with this dongle failed; therefore, we concluded that it is designed in a way that prevents hacking. We decided to look for another dongle, and since we had limited options and criteria, we chose a Huawei e3372h-607 HiLink LTE dongle based on the indication above that it could be diagnosed.

### Measurements using HUWAEI Dongle
Running QCSuper directly was ofcourse not working on this dongle as well. Also, it was automatically changing the mode from mass storage to modem a moment after connecting it to raspi, but `ttyUSBx` was still not created. Here are the steps we took to create `ttyUSBx` for communication with the dongle and access AT commands.
- **Step 1:**
  If we look at /lib/udev/rules.d/40-usb_modeswitch.rules, we see the following rules for Huawei comm device we can find the below rule:
  ```
  ATTRS{idVendor}=="12d1", ATTRS{manufacturer}!="Android", ATTR{bInterfaceNumber}=="00", ATTR{bInterfaceClass}=="08", RUN+="usb_modeswitch "%b/%k'"
  ```
  Comment out this rule to prevent the dongle from automatically switching modes.

- **Step 2:**
 Run `lsusb` to find the current vendor and product id of the dongle. Then, run the command below:
  ```
  sudo usb_modeswitch -v 12d1 -p 1f01 -X
  ```
  This command is used to make a USB modem available as a serial or network device instead of appearing as a storage device which will make the device start appearing as usb serial as ttyUSBx and in our case ttyUSB0, ttyUSB1 and ttyUSB0 was created that means now we can can talk to our device. Also, run `lsusb` to see the change in the product id.

- **Step 3:**
  ```
  sudo modprobe cdc_ncm
  ```
  Run the above command and it loads the `cdc_ncm` kernel module, which enables support for **USB network devices** that use the **Communications Device Class - Network Control Model (CDC-NCM)** protocol. This protocol is commonly used by USB modems, dongles, and network adapters to establish a network interface (e.g., `wwan0`) on Linux systems, allowing network communication through the USB device. Now, `mmcli -L` will start detecting the modem.
  
  Note: But after completing all these steps we ran into a problem that we were not able to connect to the internet anymore. So to connect with the internet we ran the below command:
  ```
  sudo nmcli c add type gsm ifname ttyUSB2 con-name my-modem apn "airtelgprs.com"
  > Connection 'my-modem' (2f1a483a-b982-4ecb-b4b3-814489271bc) successfully added.
  ```
  This command configures the modem for connecting to a mobile network and registers the connection within NetworkManager.

Now that we have the USB serial port detected, we can communicate with the dongle using AT commands to start collecting measurements.

