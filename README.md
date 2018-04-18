# Computational-Sprinting-for-Browsers

Implement sprinting techniques on the Chrome Browser to speed up page loads and also improve energy efficiency. The decisions are based on network activity observed.

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
 
### script.sh

This script is used for running experiments by loading the Google Chrome browser with the extension that has been designed to record the network activity for each web page loaded. The list of web pages to be loaded can be provided in a seperate file such as "Top 50 Pages". We use taskset to launch Google-Chrome on certain cores to eventually measure the power consumption. The usage is as follows:

```
./script.sh Top/ 50/ Pages
```

### Zipf

This directory holds the python implementation of mapping Alexa Top 500 Global Sites to the Zipf distribution. It is observed that the list of web pages loaded by an individual over the course of time follows Zipf distribution.

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

