from pyattck import Attck
Attck.update(self)
attack = Attck()
for tactic in attack.enterprise.techniques:
    print((tactic))
