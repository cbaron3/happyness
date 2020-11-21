import os
import requests
import time
import datetime
import schedule
import urllib.request

from dotenv import load_dotenv
from twilio.rest import Client
from bs4 import BeautifulSoup


class MessageHandler:
    def __init__(self, token, sid, number):
        self.client = Client(sid, token)
        self.number = number

    def send(self, msg, recepients):
        for recepient in recepients:
            message = self.client.messages.create(body=msg,
                                                  from_=self.number,
                                                  to=recepient)

            print(message.sid)
            print(message.status)

            time.sleep(1)


class HappinessScraper:
    def __init__(self):
        self.url = 'https://www.ubereats.com/ca/london-ont/food-delivery/happiness/QOwmsPH2TNmfejpREzKCFw'

    def run(self, ignore_stock=False):
        # Retrieve contents from page
        response = requests.get(self.url)

        # Find all h4 tags
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.findAll('h4')

        donuts = []

        for result in results:
            # Only consider h4 tags that include the word donut except the donut boxes
            if "donut" in result.string.lower() and "box" not in result.string.lower():
                # Check if donut is sold out
                sold_out = result.parent.findAll(text='Sold out')

                # Consider donuts that are in stock UNLESS the scraper is configured to ignore_stock
                if not sold_out or ignore_stock:
                    donuts.append(result.string[:len(result.string)-1])

        return ', '.join(donuts)


def notify_admin(msg_handler, admin):
    # Notify only the admin that the service is working
    msg_handler.send(
        "Happyness donut bot is active! You will receive happiness donut stock information on Fridays at 6:00 PM and Saturdays at 9:05 AM", [admin])


def stock_notifer(msg_handler, scraper, recepients, ignore_stock=False):
    print("Stock notifier")

    # Scrape page
    donuts = scraper.run(ignore_stock)

    # If there exist donuts in stock, send them to recepients via text
    if donuts:
        msg = "Happiness donuts: {}".format(donuts)
        msg_handler.send(msg, recepients)
    else:
        print("No donuts in stock")


def activity_logger():
    print("Scheduler running... {}".format(datetime.datetime.now()))


if __name__ == "__main__":
    # Load environment variables
    load_dotenv()

    TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
    TWILIO_SID = os.getenv("TWILIO_SID")
    TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
    RECEPIENTS = os.getenv("RECEPIENTS").split(",")

    # Instantiate objects
    msg_handler = MessageHandler(TWILIO_TOKEN, TWILIO_SID, TWILIO_NUMBER)
    scraper = HappinessScraper()

    # Start service by sending text to my phone
    print("Happiness Notifier started...")
    notify_admin(msg_handler, RECEPIENTS)

    # Heart beat
    schedule.every(30).seconds.do(activity_logger)

    # # Test function, grab all donuts regardless of stock
    # schedule.every(45).seconds.do(stock_notifer, msg_handler,
    #                               scraper, [RECEPIENTS[0]], True)

    # Every friday at 6 PM, near the end of dinner, relay donut stock
    # 6PM EST is 23:00 UTC
    schedule.every().friday.at("23:00").do(
        stock_notifer, msg_handler, scraper, RECEPIENTS[0], True)

    # Every saturday at 9:05 AM, right after open, relay donut stock
    # 9:05 AM EST is 2:05 PM UTC (For now, dst screws this up but im lazy for now)
    schedule.every().saturday.at("14:05").do(
        stock_notifer, msg_handler, scraper, RECEPIENTS)

    print("Scheduler configured...")

    while True:
        schedule.run_pending()
        time.sleep(1)
