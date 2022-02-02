# ε-κalibur
This repository contains example code for the following ESORICS 2022 submission:

- [Sebastian Zillien](https://scholar.google.de/citations?user=kdCKry4AAAAJ&hl=de), [Steffen Wendzel](https://scholar.google.de/citations?user=DZqkZ1IAAAAJ&hl=en&oi=ao): *ε-κalibur: Weaknesses of two popular covert channel detection methods and a remedy*.

## Usage
Each script contains the relevant functions and a simple usage example.

Example run:

    python epssim.py

### compress.py
This script expects a list of ascending packet times like Wireshark would record them, and calculates the compressibility scores for a window size of 2,000 packets.

### epssim.py
This script expects a list of ascending packet times like Wireshark would record them, and calculates the epsilon-similarity scores for a window size of 2,000 packets for 6 different epsilon-thresholds.

### inject_fuzzy.py
This script expects a list of inter-arrival times (IATs) and calculates the modified IATs for ε-κalibur.

### Example Files
- `iat.csv` contains a list of IATs as they would be produced by the original IAT covert channel.
- `timings.csv` contains a list of ascending packet times of legitimate traffic, recorded with Wireshark.

### IAT Traffic Generation

For generating network traffic, one can use [CCEAP](https://github.com/cdpxe/CCEAP/) together with its `iat_encode` tool. Afterwards, `wireshark` can be applied to record the traffic and extract the IAT values.
