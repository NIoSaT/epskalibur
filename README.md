# epskalibur
This repository contains example code for the ESORICS 2022 submission *eps-kalibur: Weaknesses of two popular covert channel detection methods and a remedy* by S. Zillien & S. Wendzel.

## Usage
Each script contains the relevant functions and a simple usage example.

Example run:

    python epssim.py

### compress.py
This script expects a list of inter-arrival times (IATs) like wireshark would generate them, and calculates the compressibility scores for a window size of 2,000 packets.

### epssim.py
This script expects a list of IATs like wireshark would generate them, and calculates the epsilon-similarity scores for a window size of 2,000 packets for 6 different epsilon-thresholds.

### inject_fuzzy.py
This script expects a list of IATs and calculates the modified IATs for eps-kalibur.
