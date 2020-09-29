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

    def run(self):
        # Retrieve contents from page
        response = requests.get(self.url)

        # Find all h4 tags
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.findAll('h4')

        donuts = []

        for result in results:
            if "donut" in result.string.lower() and "box" not in result.string.lower():
                notInStock = result.parent.findAll(text='Sold out')

                if not notInStock:
                    donuts.append(result.string[:len(result.string)-1])

        return ', '.join(donuts)


def notify_admin(msg_handler, admin):
    # Notify only the admin that the service is working
    msg_handler.send("Service is active", [admin])


def stock_notifer(msg_handler, scraper, recepients):
    # Scraper page
    instock = scraper.run()

    # If there exist donuts in stock, send them to recepients via text
    if instock:
        msg = "Happiness donuts: {}".format(instock)
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
    notify_admin(msg_handler, RECEPIENTS[0])

    # Heart beat
    schedule.every(30).seconds.do(activity_logger)

    # Every friday at 6 PM, near the end of dinner, relay donut stock
    schedule.every().friday.at("18:00").do(
        stock_notifer, msg_handler, scraper, RECEPIENTS[0])

    # # Every friday at 8 PM, near the end of dinner, relay donut stock
    schedule.every().friday.at("20:00").do(
        stock_notifer, msg_handler, scraper, RECEPIENTS)

    # # Every saturday at 8 AM, before donuts are bought, relay donut stock
    schedule.every().saturday.at("08:00").do(
        stock_notifer, msg_handler, scraper, RECEPIENTS)

    print("Scheduler configured...")

    while True:
        schedule.run_pending()
        time.sleep(1)
