# Get public IP's and DNS from AWS Accounts

Scripts to help retrieve AWS information such as Route53 domains and public IP addresses, and create assets in InsightVM via its API.
- - - - - -

# Installation

```bash
cd insightvm-automations/aws
. venv/bin/activate
pip install -r requirements.txt
```

# Usage
```bash
cd aws/
python main.py >> output/domains.txt 
ls output/
```
