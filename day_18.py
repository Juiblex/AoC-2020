import parglare

action = parglare.get_collector()

@action
def program(_, nodes):
  return nodes[0]

@action
def paren(_, nodes):
  return nodes[1]

@action
def add(_, nodes):
  return nodes[0] + nodes[2]

@action
def mult(_, nodes):
  return nodes[0] * nodes[2]

@action
def num(_, nodes):
  return int(nodes[0])