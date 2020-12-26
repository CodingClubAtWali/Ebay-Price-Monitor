# Ebay Price Monitor

## Overview
The Ebay Price Monitor monitor's a given Ebay link at a certain time interval which can be set in the config.json file. When a price chance is detected, an email is sent out to the recipient.



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following modules

```bash
pip3 install requests
pip3 install bs4
pip3 install ssl
```

## Usage
You will need to configure the config.json file with appropriate values. You will also need to make sure [Less Secure Apps](https://myaccount.google.com/lesssecureapps?) is enabled on your Gmail account. Once that is done, run the ebayMonitor.py file.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
