# Define a dictionary of restriction enzymes and their recognition sequences
restriction_enzymes = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT",
    "SacI": "GAGTC",
    "BstSI": "CGCG",
    "BamHI": "GGATCC",
    "TFI": "GTAC",
    "TI(II)": "CACGTG",
    "BbvI": "GCGC",
    "Sau3AI": "GATC",
    "NlaIII": "CATGC",
    "EcoRI”": "GAATTC",

    # Add more enzymes and sequences as needed
}

# Get user input
user_input = input("Enter a sequence: ")

# Reverse the input sequence
reversed_sequence = user_input[::-1]

# Search for a matching restriction enzyme with the reversed input sequence
matching_enzyme = None
for enzyme, sequence in restriction_enzymes.items():
    if reversed_sequence == sequence:
        matching_enzyme = enzyme
        break

# Output the reversed sequence and matching enzyme (if found)
print("Reversed sequence:", reversed_sequence)
if matching_enzyme:
    print("Matching enzyme:", matching_enzyme)
else:
    print("No matching enzyme found.")
