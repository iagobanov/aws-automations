# Get public IP's and DNS from AWS Accounts

Scripts to help retrieve AWS information such as Route53 domains and public IP addresses, and create assets in InsightVM via its API.
- - - - - -

# Installation

```bash
git clone https://git.topfreegames.com/security/insightvm-automations.git
cd insightvm-automations/aws
. venv/bin/activate
pip install -r requirements.txt
```

# Usage
Then Configure your AWS credentials and run aws-mfa to get a session token, then:

```bash
cd aws/
python main.py >> output/domains.txt 
ls output/
```
