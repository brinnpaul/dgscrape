# Set Up
pip install virtualenv
virtualenv env
. env/bin/activate
pip install -r requirements.txt

Change EMAIL_TO/EMAIL_PASSWORD in config.py to your own email address and password.
Set TIME to desired email update interval in minutes

#While in (env) -> running `. env/bin/activate` enters into a virtural environment

python scrape.py keywords...
  or
python scrape.py -s keywords...
  with the -s flag set you could potentially leave script running indefinitely.

# To leave virtualenv after running the script
deactivate


