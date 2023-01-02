import random
from time import sleep
from rich import print
from thespian.actors import *


class Add(object):
    def __init__(self, val): self.value = val
    def __str__(self): return self.value


class Print(object):
    def __init__(self, val): self.value = val
    def __str__(self): return self.value


class Remove(object):
    def __init__(self, i): self.id = i
    def __str__(self): return self.value


class Reexecute(object):
    def __init__(self, i): self.id = i
    def __str__(self): return self.value


class Greeting(object):
    def __init__(self, i, msg):
        self.id = i
        self.message = msg

    def __str__(self):
        return "id: "+str(self.id)+" ["+self.message+"]"


class Hello(Actor):
    def __init__(self, start_args=None):
        self.count = 0

    def receiveMessage(self, message, sender):
        try:
            self.count += 1
            if isinstance(message, Greeting):
                if (random.uniform(0, 1) > 0.5):
                    raise Exception("break............ id: " +
                                    str(message.id)+" ["+message.message+"]")
                sleep(0.2)
                print("id: "+str(message.id)+" ["+message.message+"]")
                self.send(sender, Remove(message.id))
        except Exception as e:
            print(e)
            self.send(sender, Reexecute(message.id))


class Supervisor(Actor):
    def __init__(self, start_args=None):
        self.hello = None
        self.count = 0
        self.queue = {}
        self.finalValue = ""

    def receiveMessage(self, message, sender):
        if (self.hello == None):
            self.hello = self.createActor(Hello)
        if isinstance(message, Add):
            # send to execute
            self.count += 1
            greeting = Greeting(self.count, message.value)
            print("add: "+str(greeting))
            self.queue[self.count] = greeting
            greeting.sendTo = [self.hello, sender]
            self.send(self.hello, greeting)
        elif isinstance(message, Remove):
            print("Remove: "+str(self.queue.get(message.id)))
            greeting = self.queue.pop(message.id)
            self.finalValue = self.finalValue+" "+str(greeting.message)
        elif isinstance(message, Reexecute):
            print("reexecute: "+str(message.id))
            greeting = Greeting(message.id, str(self.queue.get(message.id)))
            greeting.sendTo = [self.hello, sender]
            self.send(self.hello, greeting)
        elif isinstance(message, Print):
            print(self.finalValue)

    def receiveMsg_ChildActorExited(self, message, sender):
        print("ChildActorExited")
        print(message)


if __name__ == "__main__":
    supervisor = ActorSystem().createActor(Supervisor)
    ActorSystem().tell(supervisor, Add("Hello"))
    ActorSystem().tell(supervisor, Add("World"))
    ActorSystem().tell(supervisor, Add("Actor"))
    ActorSystem().tell(supervisor, Add("in"))
    ActorSystem().tell(supervisor, Add("Python"))
    sleep(5)
    ActorSystem().tell(supervisor, Print(""))
    print("I just sent a hi....")
    # ActorSystem().tell(supervisor, ActorExitRequest())
