import numpy as np
from thespian.actors import *
from time import sleep
from supervisior_actor_monad import Add, Print
from expression.collections import seq, Seq
from rich import print

from supervisior_actor_monad import Supervisor
from maybe_monad import MaybeMonad
from sequence_monad import custom

print("[bold red]\nMaybe: [/bold red]\n")
value = 100
m1 = MaybeMonad(value)
print(m1.value)  # 100
print(m1.contains_value)  # True

m2 = m1.bind(np.sqrt)
print(m2.value)  # 10.0

m3 = m2.bind(lambda x: x / 0)
print(m3.contains_value)  # True
print(m3.value)


def exc(x):
	raise Exception('Failed')


m4 = m3.bind(exc)
print(m4.contains_value)  # False

print("[bold red]\nSupervisior/actor: [/bold red]\n")
supervisor = ActorSystem().createActor(Supervisor)
ActorSystem().tell(supervisor, Add("Hello"))
ActorSystem().tell(supervisor, Add("World"))
ActorSystem().tell(supervisor, Add("Actor"))
ActorSystem().tell(supervisor, Add("in"))
ActorSystem().tell(supervisor, Add("Python"))
sleep(2)
ActorSystem().tell(supervisor, Print(""))
print("I just sent a hi....")
ActorSystem().tell(supervisor, ActorExitRequest())


print("[bold red]\nSequence: [/bold red]\n")
xs = Seq.of(2, 1, 11)
ys = custom(xs)
print(f"xs = {xs}, ys = {ys}")

xs = Seq.of(10, 123, 5)
ys = custom(xs)
print(f"xs = {xs}, ys = {ys}")

xs = Seq.of(81, 2, 13)
ys = custom(xs)
print(f"xs = {xs}, ys = {ys}")

xs = Seq.of(15, 34, 122)
ys = custom(xs)
print(f"xs = {xs}, ys = {ys}")

xs = Seq.of(0, 0, 0)
ys = custom(xs)
print(f"xs = {xs}, ys = {ys}")