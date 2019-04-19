import unittest

from src.observer import (EmailSubscriber, NewsPublisher, ObserverA, ObserverB,
                          SMSSubscriber, Subject)


class TestObserver(unittest.TestCase):
    def test_observer(self):
        subject = Subject()
        oba = ObserverA(subject)
        obb = ObserverB(subject)

        subject.notify_all("push notification", "email")
    
    def test_news_observer(self):
        publisher = NewsPublisher()
        
        email_sub = EmailSubscriber(publisher)
        sms_sub = SMSSubscriber(publisher)
        
        self.assertSetEqual(set(publisher.subscribers()), {EmailSubscriber.__name__, SMSSubscriber.__name__})

        publisher.add_news("Trump built the wall!")
        publisher.notify_subscribers()

        publisher.detach(email_sub)
        
        self.assertSetEqual(set(publisher.subscribers()), {type(sms_sub).__name__})

        publisher.add_news("Trade war is over!")
        publisher.notify_subscribers()

