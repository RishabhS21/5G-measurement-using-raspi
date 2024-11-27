# BTP Semester Plan

Note: This is a tentative plan of the project. However, you can find the actual work progress [here](./progress.md).

## Project Title
Analyzing 5G Network Performance in Mobility

## Project Overview
The objective of this project is to analyze the performance of 5G networks under mobility conditions using a Raspberry Pi setup. The final goal is to install monitoring devices on a moving vehicle (institute bus) and a stationary location (LHC) to collect and analyze data over a period of two weeks.

## Project Phases and Timeline (tentative)

### Phase 1: Setup and Initial Understanding (Early August - Mid August)
1. **Raspberry Pi Setup**
   - Install Linux on the Raspberry Pi.
   - Ensure the Raspberry Pi is fully functional with necessary peripherals.

2. **Codebase Familiarization**
   - Clone the [nm-exp-active-netrics](https://github.com/internet-equity/nm-exp-active-netrics) repository.
   - Understand the structure of the codebase, including libraries and modules used.
   - Set up the development environment for running and testing the code.

### Phase 2: Modifications and Customization (Mid August - End September)
1. **Radiologs Integration**
   - Work on integrating radiologs into the existing codebase.
   - Modify the codebase to collect radio logs during network performance tests.

2. **Network Performance Metrics**
   - Implement functionalities to collect network details such as throughput, RTT, latency, and other relevant metrics.
   - Ensure data is collected accurately and efficiently.

3. **Application Layer Analysis**
   - Extend the codebase to include analysis at the application layer.
   - Collect and analyze data related to application performance over the network.

### Phase 3: Adaptation for Wireless Networks (Early October - Mid October)
1. **Wireless Network Modifications**
   - Modify the existing wired network codebase to support wireless network performance analysis.
   - Test and validate the modifications to ensure compatibility with wireless networks.

### Phase 4: Data Collection and Analysis (Mid October - Mid November)
1. **Device Installation**
   - Install one monitoring device on the institute bus and maybe another at a fixed location somewhere in LHC.
   - Ensure the devices are securely installed and functioning correctly.

2. **Data Collection**
   - Collect network performance data over a two-week period.
   - Monitor and troubleshoot any issues that arise during data collection.

3. **Data Analysis (If time allows)**
   - Analyze the collected data to draw meaningful insights on 5G network performance under mobility conditions.
   - Prepare a comprehensive report on the findings.

## Deliverables
- Modified codebase with support for radiologs, network performance metrics, and application layer analysis.
- Data collected from the monitoring devices installed on the bus and at LHC.
- Analysis report detailing 5G network performance under mobility conditions (If time allows).

## References
- [nm-exp-active-netrics Codebase](https://github.com/internet-equity/nm-exp-active-netrics)
- Relevant research papers on 5G measurement study
  1. [Uncovering 5G Performance on Public Transit Systems with an
App-based Measurement Study](https://dl.acm.org/doi/10.1145/3618257.3624814)
  2. [Performance of Cellular Networks on the Wheels](https://dl.acm.org/doi/abs/10.1145/3551659.3559040)
