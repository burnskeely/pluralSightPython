acronyms = []

acronyms.append("LOL")
acronyms.append("TBH")
acronyms.append("BFN")

print(acronyms)

acronyms.remove("BFN")

print(acronyms)


word = "LOL"

if word in acronyms:
    print(word + " is in the list")

for acronym in acronyms:
    print(acronym)