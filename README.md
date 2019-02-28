# Computational-Sprinting-for-Browsers

[![](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/images/0)](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/links/0)[![](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/images/1)](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/links/1)[![](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/images/2)](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/links/2)[![](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/images/3)](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/links/3)[![](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/images/4)](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/links/4)[![](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/images/5)](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/links/5)[![](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/images/6)](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/links/6)[![](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/images/7)](https://sourcerer.io/fame/indrajeet95/indrajeet95/Computational-Sprinting-for-Browsers/links/7)

This project implements sprinting techniques on the Chrome Browser to speed up page loads and simultaneously improve energy efficiency. The sprinting decisions are based on the observed network activity while pages are loaded.

### Content

This directory contains a Chrome extension that uses a content script to record network activity and sends the data to background.js using Chrome's Message Passing API. Later, this data is stored in a local SQL database that is hosted on a PHP server which listens for GET requests. XHR is used for sending out the GET requests from background.js. We have used the **Web Performance Timing API** to record network activity.

### Multiple URL Opener

A Chrome extension that opens up a seperate tab with space to list the URLs of web pages that we would want to load and also provides a delay timer which is the gap between page loads.

### Zipf

This directory holds the python implementation of mapping Alexa Top 500 Global Sites to the Zipf distribution. It is observed that the list of web pages loaded by an individual over the course of time follows Zipf distribution. For more details: https://www.nngroup.com/articles/zipf-curves-and-website-popularity/

### har_csv

Sample files converted using hartools from HAR to CSV.

### hartools

A small command line application for converting HAR (HTTP Archive) files to CSV (comma seperated values). The usage is as follows:

```
./har2csv --in <source> --out <destination>
```
For help:
```
./har2csv --help
```

NOTE: If an error stating that heap space is not enough in Java occurs, try using a system with higher RAM capacity.

### rapl-tools

A tool used for measuring CPU power in Intel processors. The AppPowerMeter is used for our experiments.

### script.sh

This script is used for running experiments by loading the Google Chrome browser with the extension that has been designed to record the network activity for each web page loaded. The list of web pages to be loaded can be provided in a seperate file such as "Top 50 Pages". We use taskset to launch Google-Chrome on certain cores to eventually measure the power consumption. The usage is as follows:

```
./script.sh Top/ 50/ Pages
```

The Top 50 Pages and The Top 500 Pages are part of [Alexa Top 500 webpages](https://www.alexa.com/topsites)
