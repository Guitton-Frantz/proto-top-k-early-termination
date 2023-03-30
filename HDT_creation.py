from pyhdt.converter import HDTConverter

# Set up the converter with the input and output file paths
converter = HDTConverter()
input_file = "data.nt"
output_file = "data.hdt"

# Convert the N-Triples file to HDT
converter.convert(input_file, output_file)

# Print some statistics about the HDT file
hdt_stats = converter.get_stats(output_file)
print("Number of triples:", hdt_stats["triples"])
print("Number of subjects:", hdt_stats["subjects"])
print("Number of predicates:", hdt_stats["predicates"])
print("Number of objects:", hdt_stats["objects"])