import sys
import schedule
import time

from config import config
from service.server import Server, Mail
from service.parse import ParseDG


def main():
    args = sys.argv
    schedule_recurring = False
    if '-s' in args:
        args.remove('-s')
        schedule_recurring = True

    keywords = args[1:]
    parser = ParseDG(keywords)
    mail = Mail(config)
    try:
        with Server(config) as server:
            def update_and_send():
                parser.run()
                results = parser.results
                mail.make_sender(server, results)
                mail.send()
                print "Update sent!"

            if schedule_recurring:
                minutes = config.TIME
                print "Email update every {} minute(s)".format(minutes)
                update_and_send()
                schedule.every(minutes).minutes.do(update_and_send)
                while True:
                    schedule.run_pending()
                    time.sleep(1)
            else:
                update_and_send()
    except Exception as e:
        print e
        print "Closing Service"

main()


