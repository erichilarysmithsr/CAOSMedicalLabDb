from rdflib import Graph, Namespace

# Create a namespace for the ontology
ns = Namespace("http://www.semanticweb.org/owl/ontologies/2023/05/muscle-recovery-time-ontology#")

# Create a graph to store the ontology
g = Graph()

# Add the ontology's namespace to the graph
g.namespace_manager.bind("owl", ns)

# Add the ontology's axioms to the graph
g.add((ns.Ontology, rdf.type, owl.Ontology))
g.add((ns.Muscle, rdf.type, owl.Class))
g.add((ns.recoveryTime, rdf.type, owl.DatatypeProperty))
g.add((ns.recoveryTime, rdfs.domain, ns.Muscle))
g.add((ns.recoveryTime, rdfs.range, xsd.integer))
g.add((ns.Biceps, rdf.type, ns.Muscle))
g.add((ns.Biceps, ns.recoveryTime, xsd.int("0")))
g.add((ns.Triceps, rdf.type, ns.Muscle))
g.add((ns.Triceps, ns.recoveryTime, xsd.int("0")))
g.add((ns.Quadriceps, rdf.type, ns.Muscle))
g.add((ns.Quadriceps, ns.recoveryTime, xsd.int("0")))
g.add((ns.Hamstrings, rdf.type, ns.Muscle))
g.add((ns.Hamstrings, ns.recoveryTime, xsd.int("0")))
g.add((ns.Calves, rdf.type, ns.Muscle))
g.add((ns.Calves, ns.recoveryTime, xsd.int("0")))

# Save the ontology to a file
g.serialize("muscle-recovery-time-ontology.rdf")
