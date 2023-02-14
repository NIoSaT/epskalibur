# ε-κalibur
This repository contains instructions on the usage of the tool and includes sample inter-arrival time (IATs) files (CSV format) for the following submission:

- [Sebastian Zillien](https://scholar.google.de/citations?user=kdCKry4AAAAJ&hl=de), [Steffen Wendzel](https://scholar.google.de/citations?user=DZqkZ1IAAAAJ&hl=en&oi=ao): **[Weaknesses of popular and recent covert channel detection methods and a remedy](https://doi.org/10.1109/TDSC.2023.3241451)**, in: IEEE Trans. Dependable and Secure Computing (TDSC), 2023.

## Usage
Each script contains the relevant functions and a simple usage example.

Example run:

    python epssim.py

### compress.py
This script expects a list of ascending packet times like Wireshark would record them, and calculates the compressibility scores for a window size of 2,000 packets.

### epssim.py
This script expects a list of ascending packet times like Wireshark would record them, and calculates the epsilon-similarity scores for a window size of 2,000 packets for 6 different epsilon-thresholds.

### inject_fuzzy.py
This script expects a list of IATs and calculates the modified IATs for ε-κalibur.

### inject_fuzzy_outlier.py
This script expects a list of IATs and calculates the modified IATs for ε-κalibur-O.

### Example Files
- `iat.csv` contains a list of IATs as they would be produced by the original IAT covert channel.
- `timings.csv` contains a list of ascending packet times of legitimate traffic, recorded with Wireshark.

### IAT Traffic Generation

For generating network traffic, one can use [CCEAP](https://github.com/cdpxe/CCEAP/) together with its `iat_encode` tool. Afterwards, `wireshark` can be applied to record the traffic and extract the IAT values.

#### pcap2iat
This script expects a pcap recording with a unidirectional flow (A->B or B->A, not mixed) and calculates the inter arrival times.

    pcap2iat.sh recording.pcap
