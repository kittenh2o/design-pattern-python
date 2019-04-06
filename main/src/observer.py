from abc import ABCMeta, abstractmethod


class Subject:
    ''' Subject to be observed'''

    def __init__(self):
        self.__observers = list()

    def register(self, observer):
        self.__observers.append(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class ObserverA:
    def __init__(self, subject: Subject):
        subject.register(self)

    def notify(self, subject, *args, **kwargs):
        print("{0}:: Got {1} from {2}".format(
            type(self).__name__, args, subject))


class ObserverB:
    def __init__(self, subject: Subject):
        subject.register(self)

    def notify(self, subject, *args, **kwargs):
        print("{0}:: Got {1} from {2}".format(
            type(self).__name__, args, subject))


# News Example
class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def unsubscribe(self):
        raise NotImplementedError


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print("Email to {0}, {1}".format(
            type(self).__name__, self.publisher.get_news()))

    def unsubscribe(self):
        self.publisher.detach(self)
        self.publisher = None


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print("SMS to {0}, {1}".format(
            type(self).__name__, self.publisher.get_news()))

    def unsubscribe(self):
        self.publisher.detach(self)
        self.publisher = None


class NewsPublisher:
    def __init__(self):
        self.__subscribers = set()
        self.__latest_news = None

    def attach(self, subscriber: Subscriber):
        self.__subscribers.add(subscriber)

    def detach(self, subscriber: Subscriber):
        self.__subscribers.remove(subscriber)

    def subscribers(self):
        return (type(subscriber).__name__ for subscriber in self.__subscribers)

    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        self.__latest_news = news

    def get_news(self):
        return self.__latest_news
