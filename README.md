<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** cbaron3, happyness, twitter_handle, carbaro196@gmail.com
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/cbaron3/happyness">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Happyness</h3>

  <p align="center">
    Python bot that scrapes a local donut shop's inventory and notifies a list of contacts via text what options are available.
    <br />
    <a href="https://github.com/cbaron3/happyness"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/cbaron3/happyness">View Demo</a>
    ·
    <a href="https://github.com/cbaron3/happyness/issues">Report Bug</a>
    ·
    <a href="https://github.com/cbaron3/happyness/issues">Request Feature</a>

  </p>
</p>
<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->

## About The Project

<p align="center">
    <a href="https://github.com/cbaron3/happyness">
    <img src="images/donuts.gif" alt="Donuts" width="320" height="320">
  </a>
</p>

Every weekend, my girlfriend's family invites me over for donuts. The problem is that the donut shop we go to only uploads a menu consisting of the types of donuts they CAN make and not the donuts they have in stock. This makes ordering a donut the night before a guessing game because only person goes into order, the donuts in stock change every day, and you never know what they have in stock.

Luckily, they maintain a list of their 6 available donuts for the day including whether each donut is in stock or not on their UberEats page. This bot scrapes that information and sends out a text to all of us the night before and the morning of donut day so we can guarantee our donut order is correct!

### Built With

- [Python3](https://www.python.org/downloads/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [Twilio](https://github.com/twilio/twilio-python)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo

```sh
git clone https://github.com/cbaron3/happyness.git
```

2. Create a virtual environment

```sh
python3 -m venv venv
```

3. Activate the virtual environment

4. Install the required packages

```sh
pip install -r requirements.txt
```

5. Create a .env file and fill in the following variables:

```sh
TWILIO_NUMBER=<twilio number>
TWILIO_SID=<twilio account number>
TWILIO_TOKEN=<twilio account token>
RECEPIENTS=<comma separated list of numbers you want to send too. first number is your phone number so you can debug>
```

<!-- USAGE EXAMPLES -->

## Usage

- To run

```sh
python main.py
```

<!-- LICENSE -->

## License

Distributed under the GNU License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Carl Baron

Project Link: [https://github.com/cbaron3/happyness](https://github.com/cbaron3/happyness)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/cbaron3/happyness.svg?style=flat-square
[contributors-url]: https://github.com/cbaron3/happyness/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/cbaron3/happyness.svg?style=flat-square
[forks-url]: https://github.com/cbaron3/happyness/network/members
[stars-shield]: https://img.shields.io/github/stars/cbaron3/happyness.svg?style=flat-square
[stars-url]: https://github.com/cbaron3/happyness/stargazers
[issues-shield]: https://img.shields.io/github/issues/cbaron3/happyness.svg?style=flat-square
[issues-url]: https://github.com/cbaron3/happyness/issues
[license-shield]: https://img.shields.io/github/license/cbaron3/happyness.svg?style=flat-square
[license-url]: https://github.com/cbaron3/happyness/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/carl-baron3/
