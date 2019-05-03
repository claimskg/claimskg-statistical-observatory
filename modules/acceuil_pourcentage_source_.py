import rdflib

#Charger tout le ttl
g = rdflib.Graph()
result = g.parse("claimskg_20_12_2018.ttl", format="turtle")


