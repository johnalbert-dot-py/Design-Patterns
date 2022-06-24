# simple implementation of Observer Pattern


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} got message '{message}'")


class Publisher:

    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


pub = Publisher()

john = Subscriber("John")
finn = Subscriber("Finn")

pub.register(john)
pub.register(finn)

pub.dispatch("Let's eat breakfast")
pub.unregister(john)
pub.dispatch("Let's go for a dinner.")
