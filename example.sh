pip install virtualenv
DIR=$PWD/env

if [ ! -d $DIR ]; then
  virtualenv env
fi

. env/bin/activate
pip install -r requirements.txt

python scrape.py manufacturer money
# -s flag sets recurring email updates on intervals set in config.py
# python scrape.py -s manufacturer money
deactivate