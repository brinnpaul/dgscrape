# Set Up
`git clone https://github.com/brinnpaul/dgscrape.git` <br />
`pip install virtualenv` <br />
`virtualenv env` <br />
`. env/bin/activate` <br />
`pip install -r requirements.txt` <br />

Change EMAIL_TO/EMAIL_PASSWORD in config.py to your own email address and password. <br />
Set TIME to desired email update interval in minutes <br />

While in (env) -> running `. env/bin/activate` enters into a virtural environment

`python scrape.py keywords...` <br />
  or <br />
`python scrape.py -s keywords...` <br />
  with the -s flag set you could potentially leave script running indefinitely. <br />

To leave virtualenv after running the script <br />
`deactivate`


