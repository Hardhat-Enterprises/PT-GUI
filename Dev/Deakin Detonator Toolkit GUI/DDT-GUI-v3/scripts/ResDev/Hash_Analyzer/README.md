# Hash Analyzer Guide

<img src="https://img.shields.io/badge/language-python-brightgreen?logo=python&style=for-the-badge"/>

---
## Overview

#### Hash Analyzer

This program attempts to identify a given hash's source algorithm through the use of RegEx.

It may not single out a specific algorithm directly as some hashing algorithms share the same properties for their digests (output), but does help to shortlist the amount of possible algorithms.

---
## How To Use

#### Hash
To analyze a single hash, simply copy and paste the hash into the text box and click **Analyze**.

#### File
To analyze multiple hashes in a file, make sure the hashes are formatted in a one-hash-one-line format. Do not forget to change the drop-down list to **File**, browse your file, and click **Analyze**.

#### Base16, Base32, Base64 Decoder
Additionally, the program will attempt to decode single hashes in one of the base-x encoded string. Do note that if the hash is not a base-x encoded string, it may still attempt to decode it inaccurately.

---
## Limitations
This program's hash algorithms library is limited to the user defined functions for each hashing algorithms. However, it is also expandable by adding more functions to check for other hashing algorithms.