from pyattck import Attck

attack = Attck()
for tactic in attack.enterprise.actors:
    print((tactic))
