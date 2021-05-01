---
layout: page
title: Using Python to Interface with RedPocket Mobile
---

RedPocket has been a great budget option for those who don't need unlimited data. The one piece missing was a better way to track data usage to understand how much of a hit that 2 minute 4K YouTube video really took on your 3GB monthly limit. So I built a quick python package to do it.

The source code is located [here](https://github.com/ronnie-llamado/pyRedPocket). If there are any blaring issues or you feel the code is atrocious, please feel free to let me know. 


## Installation

Install with `pip`:

```python
pip install pyredpocket
```

## Usage





```python
from configparser import ConfigParser
from pyredpocket import RedPocket

# read in username/password from local conf file
config = ConfigParser()
config.read('conf/redpocket.conf')
username = config.get('DEFAULT', 'username')
password = config.get('DEFAULT', 'password')

# create RedPocket object, pulls information on 
client = RedPocket(username=username, password=password)
data = client.details[0]

# mask personal details
data.phone_number = 'XXXXXXXXXX'
data.hash = 'XXXXXXXX'

print(data)
```

    LineDetails(phone_number='XXXXXXXXXX', voice_balance=-1, messaging_balance=-1, data_balance=2271, timestamp=1619899162.0668604, start_date=datetime.date(2021, 4, 2), end_date=datetime.date(2021, 5, 4), hash='XXXXXXXX')

## Future Applications

If I don't switch away from RedPocket Mobile (looking likely for other reasons), there are a few more tools I'd like to build using this package. 

1. Jupyter dashboard to track data to explore if I can lower my monthly plan
2. Email/text alerts when data dips below specific points (1GB, 0.5GB)
3. Easily deployable application for users to pull data locally
