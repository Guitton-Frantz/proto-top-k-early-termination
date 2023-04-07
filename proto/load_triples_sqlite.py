import sqlite3
from rdflib import Graph

# Chemin vers le fichier .nt
file_path = 'proto-top-k-early-termination\data.nt'

# Connexion à la base de données SQLite
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Création de la table pour stocker les triplets RDF
cur.execute('CREATE TABLE triples (subject TEXT, predicate TEXT, object TEXT)')

# Chargement des données RDF depuis le fichier .nt avec RDFLib
g = Graph()
g.parse(file_path, format='nt')

# Insertion des triplets RDF dans la table "triples" de la base de données SQLite
for (s, p, o) in g:
    cur.execute('INSERT INTO triples VALUES (?, ?, ?)', (s.n3(), p.n3(), o.n3()))

# Création des index SPO, POS et OPS
cur.execute('CREATE INDEX spo_index ON triples (subject, predicate, object)')
cur.execute('CREATE INDEX pos_index ON triples (predicate, object, subject)')
cur.execute('CREATE INDEX ops_index ON triples (object, predicate, subject)')

# Fermeture de la connexion à la base de données SQLite
conn.commit()

# Vérification de la création des index
cur.execute('PRAGMA index_list(triples)')
indexes = cur.fetchall()

for index in indexes:
    print(index[1], 'created successfully')

conn.close()
