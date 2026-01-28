# JF Silly Sentences

r=[]
for p in ["adjective", "animal", "past tense verb", "adverb", "exclamation (without the exclamation mark)"]:
    r.append(input(f"Type a(n) {p}: ").strip().lower())
print("Today I went to the zoo. I saw a(n) "+r[0]+" "+r[1]+" jumping up and down in its tree. It "+r[2]+" "+r[3]+". I was so surprised that I shouted, '"+r[4].capitalize()+"!'")