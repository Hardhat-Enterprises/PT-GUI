# Phishing Website Creator Guide

<img src="https://img.shields.io/badge/language-python-brightgreen?logo=python&style=for-the-badge"/>

---
## Overview

#### Phishing Website Creator

This tool functions to automatically host a phishing webpage of a website.

The phishing pages are limited as it is manually edited. At the time of writing, there are 3 webpages available, Google, Instagram, and Facebook. The Google and Instagram pages are taken directly from Zphisher by htr-tech: https://github.com/htr-tech/zphisher while the Facebook one is edited from Facebook. The server is hosted using Python's http.server (or SimpleHTTPServer) and is only available for local network hosting and localhost currently.

---
## How To Use (Terminal)

#### Start
Type in **python3 main.py** to the terminal to start the program.

#### Choose a site
Type in a number based on the list to choose which webpage to phish on.

#### Choose a server
Local Network: Type in your local network IP address which can be found by typing **ipconfig** (in Windows terminal) or **ifconfig** (in Linux terminal)
Localhost: Leave the prompt blank.

---
## Limitations
The phishing pages are currently very limited. Using Python's http.server makes it impossible to host a proper server (e.g. PHP pages cannot be sent to the client).