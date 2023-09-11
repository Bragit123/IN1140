
## Oppgave 1
"""
I lingvistisk analyse opererer vi på følgende lingvistiske nivåer
Fonetikk: Lyder i seg selv, hvordan de høres ut.
Fonologi: Hvordan lyder fungerer i språket.
Morfologi: Hvordan ord er bygd opp.
Syntaks: Hvordan setninger bygges opp av ord.
Semantikk: Betydningen av ord.
Pragmatikk: Hvordan kontekst påvirker betydningen av ord.
"""

## Oppgave 2
"""
a) Frie morfemer er morfemer som kan stå alene, for eksempel vanlige ord som
  hund, glass eller bord.
  Bundne morfemer må settes sammen med andre morfemer for å gi mening.

b) Bundne morfemer kan deles inn i (blant annet) prefikser og suffikser.
   Prefikser legges til på starten av ord, mens suffikser legges til på slutten.
   For eksempel er "u" i "uekte" og "post" i "postapokalyptisk" prefikser, mens
   "ende" i "kastende" eller "et" i "hoppet" er suffikser.
"""

## Oppgave 3
# a)
filename = "in01.txt"
content = ""
with open(filename, "r") as infile:
    content = infile.read()

# b)
antall_er = content.count("er")

words = content.split(" ")
ends_with_er = 0
for word in words:
    if word.endswith("er"):
        ends_with_er += 1

print(f"'er' forekommer {antall_er} ganger i {filename}.")
print(f"{ends_with_er} ord ender med 'er' i {filename}.")

# c)
two_letter_list = []
for word in words:
    two_letter_list.append(word[-2:])

two_letter_string = " ".join(two_letter_list)


## Oppgave 4
lines = []
all_words = []
num_words = 0
with open(filename, "r") as infile:
    for line in infile:
        lines.append(line)
        words = line.split(" ")
        num_words += len(words)
        all_words.append(words)
        

num_lines = len(lines)
print(f"{filename} består av {num_lines} linjer og {num_words} ord.")


## Oppgave 5
# a)
# Her la jeg også til all_words ovenfor for å slippe å lese filen på nytt.
with open("tokenisering.txt", "w") as outfile:
    for words in all_words:
        for word in words:
            outfile.write(word + "\n")

# b)
"""
Problemer:
- Tegnsetting blir med. Allerede på første linje har jeg ' "A ' i stedet for kun
' A ',
og linje 3 er ' Calls": ' istedet for kun ' Calls '.
- Linjeskift i datafilen blir også regnet med som linjeskift her, i tillegg til
linjeskiftet jeg legger inn manuelt, altså får jeg flere steder tomme linjer.
- På linje 280 får jeg ' spenningsfilms-aktig ' på en linje, men dette burde
kanskje vært på to linjer: ' spenningsfilms ' og ' aktig '.
"""

## OUTPUT FRA KODEN:
"""
Terminal> python oblig1a_brageat.py 
'er' forekommer 8694 ganger i in01.txt.
4773 ord ender med 'er' i in01.txt.
in01.txt består av 356 linjer og 52419 ord.
"""