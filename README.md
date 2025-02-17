# All-In-One OSINT Tool

This is an Open Source Intelligence (OSINT) tool that combines several tools for cyberspace information retrieval. It uses sherlock, holehe, and theHarvester to search for usernames on social media, emails on websites, and related domains.

## Features
- Sherlock: Search for usernames on various social media platforms.
- Holehe: Search for email-related information on various websites.
- TheHarvester: Collect domain-related information, such as subdomains, emails, and more.

## Requirements
Before you start, make sure you have Python and the following tools installed on your system:

1. Python 3.x: To run Python scripts.
2. Holehe and TheHarvester: Two OSINT tools for email and domain information retrieval. You will install them through the terminal.
3. Sherlock: Tool for searching for usernames on various social media platforms.

## Installation Method

### Step 1: Clone the Repository
Clone this repository to your local system with the following command:

``` bash
git clone https://github.com/XsyCodee/osint-tool.git
cd osint-tool
```

### Step 2: Installing tools
Install the following tools via terminal:

Holehe
``` bash
git clone https://github.com/benchtown/holehe.git
CD holehe
pip install -r requirements.txt
```

Harvester
``` bash
git clone https://github.com/laramies/theHarvester.git
cd the Harvester
pip install -r requirements.txt
```

sherlock
``` bash
pip install sherlock

### Step 3: Environment (optional)
1. Install virtual env
``` bash
pip install virtualenv
```

2. Create and activate virtual environment
``` bash
virtualenv venv
source venv/bin/activate # Linux/Mac
.\venv\Scripts\activate # Windows
```

3. install dependency project
``` bash
pip install -r requirements.txt
```

### How to Use
1. Run file
``` bash
python3 osint.py #If it doesn't work use bash method
bash run.sh #if it doesn't work
```

2. Usage Example
1. find username
Select option 1 to search for username on social media. Enter the username you want to search for, and the tool will show you which platforms the username was found on.

2. Find Email
Select option 2 to search for email on registered websites. Enter the email address you want to search for.

3. Find Domain
Select option 3 to search for domain related information. Enter the domain name you want to search for.

### Troubleshooting
1. Unable to run Holehe or TheHarvester:
Make sure you have the required dependencies installed by running pip install -r requiremen.txt in the respective tool folders.

2. Sherlock issues:
If Sherlock is not found, make sure you have installed Sherlock with pip install sherlock.

### Contributions
If you would like to contribute to this project, you can create a pull request or report an issue on the GitHub page.

### Contribute
usdt/bnb :0xc260b410f8296c81ee39c143e559444a183e3d3c

usdt/sol :F3MHsK3rxtHdqs2azHXCGSsALLGU3DyKvAYsTzpWUWZ2
