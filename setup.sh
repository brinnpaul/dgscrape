#!/bin/bash
pip install virtualenv
DIR=$PWD/env

if [ ! -d $DIR ]; then
  virtualenv env
fi

. env/bin/activate
pip install -r requirements.txt

echo Setup Finished
echo Enter 'python scrape.py keyword_1 keyword_2 ... keyword_n'
echo into the terminal to run the webscraper for dgcoursereview.com.

# To run project only from terminal uncomment out the below code.

# python scrape.py <replace with keywords to search>
# deactivate