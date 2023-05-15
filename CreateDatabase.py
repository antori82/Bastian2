from py2neo import Graph

g = Graph(host= "143.225.233.156", password="IAmJason", name='bastian')



print(g.run("MATCH (n) RETURN n LIMIT 1").data())