### DICTIONARY


# ICS 31, Thursday 19 November 2015, 8am

"""
DICTIONARY (in Python, dict)
    Also called map or table.
    Key-value pairs:  Look up an item's value by/with its key, using indexing.
    d[k] gives you the VALUE associated with the key k.
    -- Better lookup performance than lists
    -- Indexing is more flexible:  Keys can be anything immutable, not just numbers

Dictionary requirements/characteristics:
    -- Keys must be an immutable type (i.e., not lists)
    -- Values can be anything
    -- Keys must be unique:  NOT {'x': 17, 'x': 23}
    -- Order isn't specified; Python gets to choose the order it stores things in.
        (a characteristic of HASH TABLES, the underlying mechanism behind dicts).
        But you can say (sorted(list(d))
"""
'''
dd = {'x': 17, 'x': 23}
print(dd['x'])
d = {'Donald Duck': 16, 'Daisy Duck': 17, 'Dewey Duck': 23,
     'Louie Duck': 34, 'Scrooge McDuck': 55, 'Huey Duck': 40}
print(d)
print(sorted(list(d)))
print("Dewey's age is:", d['Dewey Duck'])
print(len(d), "ducks in our dictionary")
"""
We also have:
    d.pop(key)    Remove and return the designated item
"""
print(d)
print(d.pop('Huey Duck'))
print(d)
"""
    d.update(d2)    Combine values in two dictionaries (later one prevails)
"""
print()
print(d)
d.update({'Dorothy Duck': 25, 'Daffy Duck': 23, 'Dewey Duck': 39})
print(d)

"""
Three more dict methods:
    d.keys()
    d.values()
    d.items()
    These extract data from a dictionary in a special form called a VIEW
"""
print()
print(d.keys())
for k in d.keys():
    print("Next key is:", k)
duck_keys = d.keys()
print(duck_keys)
#print(duck_keys[2])   # Can't index into a dict_keys thing, a view

# Why do we have this oddball dict_keys thing?  Why not just return a plain list?
# Because views are self-updating!

print()
print(d.values())
print()
print(d.items())
print()

print("Views vs. lists:")
print("View version:")
vals = d.values()    # This is a VIEW, a dict_values object
print(vals)
print()
print("List version:")
vals_list = list(d.values())  # This is a LIST
print(vals_list)

# print(vals[2])    # Can't index into a view
print(vals_list[2])

print('Average value:', sum(list(vals))/len(vals))
print('Average value:', sum(vals_list)/len(vals_list))

d['Donald Duck'] = 9999999
print(d)

print('Average value:', sum(list(vals))/len(vals))
print('Average value:', sum(vals_list)/len(vals_list))
print()

print(vals)
print(vals_list)
'''

short_text = '''
A STUDY IN SCARLET.

PART I.

(_Being a reprint from the reminiscences of_ JOHN H. WATSON, M.D., _late
of the Army Medical Department._) [2]

CHAPTER I. MR. SHERLOCK HOLMES.

IN the year 1878 I took my degree of Doctor of Medicine of the
University of London, and proceeded to Netley to go through the course
prescribed for surgeons in the army. Having completed my studies there,
I was duly attached to the Fifth Northumberland Fusiliers as Assistant
Surgeon. The regiment was stationed in India at the time, and before
I could join it, the second Afghan war had broken out. On landing at
Bombay, I learned that my corps had advanced through the passes, and
was already deep in the enemy's country. I followed, however, with many
other officers who were in the same situation as myself, and succeeded
in reaching Candahar in safety, where I found my regiment, and at once
entered upon my new duties.
'''

long_text = '''
A STUDY IN SCARLET.

PART I.

(_Being a reprint from the reminiscences of_ JOHN H. WATSON, M.D., _late
of the Army Medical Department._) [2]

CHAPTER I. MR. SHERLOCK HOLMES.

IN the year 1878 I took my degree of Doctor of Medicine of the
University of London, and proceeded to Netley to go through the course
prescribed for surgeons in the army. Having completed my studies there,
I was duly attached to the Fifth Northumberland Fusiliers as Assistant
Surgeon. The regiment was stationed in India at the time, and before
I could join it, the second Afghan war had broken out. On landing at
Bombay, I learned that my corps had advanced through the passes, and
was already deep in the enemy's country. I followed, however, with many
other officers who were in the same situation as myself, and succeeded
in reaching Candahar in safety, where I found my regiment, and at once
entered upon my new duties.

The campaign brought honours and promotion to many, but for me it had
nothing but misfortune and disaster. I was removed from my brigade and
attached to the Berkshires, with whom I served at the fatal battle of
Maiwand. There I was struck on the shoulder by a Jezail bullet, which
shattered the bone and grazed the subclavian artery. I should have
fallen into the hands of the murderous Ghazis had it not been for the
devotion and courage shown by Murray, my orderly, who threw me across a
pack-horse, and succeeded in bringing me safely to the British lines.

Worn with pain, and weak from the prolonged hardships which I had
undergone, I was removed, with a great train of wounded sufferers, to
the base hospital at Peshawar. Here I rallied, and had already improved
so far as to be able to walk about the wards, and even to bask a little
upon the verandah, when I was struck down by enteric fever, that curse
of our Indian possessions. For months my life was despaired of, and
when at last I came to myself and became convalescent, I was so weak and
emaciated that a medical board determined that not a day should be lost
in sending me back to England. I was dispatched, accordingly, in the
troopship "Orontes," and landed a month later on Portsmouth jetty, with
my health irretrievably ruined, but with permission from a paternal
government to spend the next nine months in attempting to improve it.

I had neither kith nor kin in England, and was therefore as free as
air--or as free as an income of eleven shillings and sixpence a day will
permit a man to be. Under such circumstances, I naturally gravitated to
London, that great cesspool into which all the loungers and idlers of
the Empire are irresistibly drained. There I stayed for some time at
a private hotel in the Strand, leading a comfortless, meaningless
existence, and spending such money as I had, considerably more freely
than I ought. So alarming did the state of my finances become, that
I soon realized that I must either leave the metropolis and rusticate
somewhere in the country, or that I must make a complete alteration in
my style of living. Choosing the latter alternative, I began by making
up my mind to leave the hotel, and to take up my quarters in some less
pretentious and less expensive domicile.

On the very day that I had come to this conclusion, I was standing at
the Criterion Bar, when some one tapped me on the shoulder, and turning
round I recognized young Stamford, who had been a dresser under me at
Barts. The sight of a friendly face in the great wilderness of London is
a pleasant thing indeed to a lonely man. In old days Stamford had never
been a particular crony of mine, but now I hailed him with enthusiasm,
and he, in his turn, appeared to be delighted to see me. In the
exuberance of my joy, I asked him to lunch with me at the Holborn, and
we started off together in a hansom.

"Whatever have you been doing with yourself, Watson?" he asked in
undisguised wonder, as we rattled through the crowded London streets.
"You are as thin as a lath and as brown as a nut."

I gave him a short sketch of my adventures, and had hardly concluded it
by the time that we reached our destination.

"Poor devil!" he said, commiseratingly, after he had listened to my
misfortunes. "What are you up to now?"

"Looking for lodgings." [3] I answered. "Trying to solve the problem
as to whether it is possible to get comfortable rooms at a reasonable
price."

"That's a strange thing," remarked my companion; "you are the second man
to-day that has used that expression to me."

"And who was the first?" I asked.

"A fellow who is working at the chemical laboratory up at the hospital.
He was bemoaning himself this morning because he could not get someone
to go halves with him in some nice rooms which he had found, and which
were too much for his purse."

"By Jove!" I cried, "if he really wants someone to share the rooms and
the expense, I am the very man for him. I should prefer having a partner
to being alone."

Young Stamford looked rather strangely at me over his wine-glass. "You
don't know Sherlock Holmes yet," he said; "perhaps you would not care
for him as a constant companion."

"Why, what is there against him?"

"Oh, I didn't say there was anything against him. He is a little queer
in his ideas--an enthusiast in some branches of science. As far as I
know he is a decent fellow enough."

"A medical student, I suppose?" said I.

"No--I have no idea what he intends to go in for. I believe he is well
up in anatomy, and he is a first-class chemist; but, as far as I know,
he has never taken out any systematic medical classes. His studies are
very desultory and eccentric, but he has amassed a lot of out-of-the way
knowledge which would astonish his professors."

"Did you never ask him what he was going in for?" I asked.

"No; he is not a man that it is easy to draw out, though he can be
communicative enough when the fancy seizes him."

"I should like to meet him," I said. "If I am to lodge with anyone, I
should prefer a man of studious and quiet habits. I am not strong
enough yet to stand much noise or excitement. I had enough of both in
Afghanistan to last me for the remainder of my natural existence. How
could I meet this friend of yours?"

"He is sure to be at the laboratory," returned my companion. "He either
avoids the place for weeks, or else he works there from morning to
night. If you like, we shall drive round together after luncheon."

"Certainly," I answered, and the conversation drifted away into other
channels.

As we made our way to the hospital after leaving the Holborn, Stamford
gave me a few more particulars about the gentleman whom I proposed to
take as a fellow-lodger.

"You mustn't blame me if you don't get on with him," he said; "I know
nothing more of him than I have learned from meeting him occasionally in
the laboratory. You proposed this arrangement, so you must not hold me
responsible."

"If we don't get on it will be easy to part company," I answered. "It
seems to me, Stamford," I added, looking hard at my companion, "that you
have some reason for washing your hands of the matter. Is this fellow's
temper so formidable, or what is it? Don't be mealy-mouthed about it."

"It is not easy to express the inexpressible," he answered with a laugh.
"Holmes is a little too scientific for my tastes--it approaches to
cold-bloodedness. I could imagine his giving a friend a little pinch of
the latest vegetable alkaloid, not out of malevolence, you understand,
but simply out of a spirit of inquiry in order to have an accurate idea
of the effects. To do him justice, I think that he would take it himself
with the same readiness. He appears to have a passion for definite and
exact knowledge."

"Very right too."

"Yes, but it may be pushed to excess. When it comes to beating the
subjects in the dissecting-rooms with a stick, it is certainly taking
rather a bizarre shape."

"Beating the subjects!"

"Yes, to verify how far bruises may be produced after death. I saw him
at it with my own eyes."

"And yet you say he is not a medical student?"

"No. Heaven knows what the objects of his studies are. But here we
are, and you must form your own impressions about him." As he spoke, we
turned down a narrow lane and passed through a small side-door, which
opened into a wing of the great hospital. It was familiar ground to me,
and I needed no guiding as we ascended the bleak stone staircase and
made our way down the long corridor with its vista of whitewashed
wall and dun-coloured doors. Near the further end a low arched passage
branched away from it and led to the chemical laboratory.

This was a lofty chamber, lined and littered with countless bottles.
Broad, low tables were scattered about, which bristled with retorts,
test-tubes, and little Bunsen lamps, with their blue flickering flames.
There was only one student in the room, who was bending over a distant
table absorbed in his work. At the sound of our steps he glanced round
and sprang to his feet with a cry of pleasure. "I've found it! I've
found it," he shouted to my companion, running towards us with a
test-tube in his hand. "I have found a re-agent which is precipitated
by hoemoglobin, [4] and by nothing else." Had he discovered a gold mine,
greater delight could not have shone upon his features.

"Dr. Watson, Mr. Sherlock Holmes," said Stamford, introducing us.

"How are you?" he said cordially, gripping my hand with a strength
for which I should hardly have given him credit. "You have been in
Afghanistan, I perceive."

"How on earth did you know that?" I asked in astonishment.

"Never mind," said he, chuckling to himself. "The question now is about
hoemoglobin. No doubt you see the significance of this discovery of
mine?"

"It is interesting, chemically, no doubt," I answered, "but
practically----"

"Why, man, it is the most practical medico-legal discovery for years.
Don't you see that it gives us an infallible test for blood stains. Come
over here now!" He seized me by the coat-sleeve in his eagerness, and
drew me over to the table at which he had been working. "Let us have
some fresh blood," he said, digging a long bodkin into his finger, and
drawing off the resulting drop of blood in a chemical pipette. "Now, I
add this small quantity of blood to a litre of water. You perceive that
the resulting mixture has the appearance of pure water. The proportion
of blood cannot be more than one in a million. I have no doubt, however,
that we shall be able to obtain the characteristic reaction." As he
spoke, he threw into the vessel a few white crystals, and then added
some drops of a transparent fluid. In an instant the contents assumed a
dull mahogany colour, and a brownish dust was precipitated to the bottom
of the glass jar.

"Ha! ha!" he cried, clapping his hands, and looking as delighted as a
child with a new toy. "What do you think of that?"

"It seems to be a very delicate test," I remarked.

"Beautiful! beautiful! The old Guiacum test was very clumsy and
uncertain. So is the microscopic examination for blood corpuscles. The
latter is valueless if the stains are a few hours old. Now, this appears
to act as well whether the blood is old or new. Had this test been
invented, there are hundreds of men now walking the earth who would long
ago have paid the penalty of their crimes."

"Indeed!" I murmured.

"Criminal cases are continually hinging upon that one point. A man is
suspected of a crime months perhaps after it has been committed. His
linen or clothes are examined, and brownish stains discovered upon them.
Are they blood stains, or mud stains, or rust stains, or fruit stains,
or what are they? That is a question which has puzzled many an expert,
and why? Because there was no reliable test. Now we have the Sherlock
Holmes' test, and there will no longer be any difficulty."

His eyes fairly glittered as he spoke, and he put his hand over his
heart and bowed as if to some applauding crowd conjured up by his
imagination.

"You are to be congratulated," I remarked, considerably surprised at his
enthusiasm.

"There was the case of Von Bischoff at Frankfort last year. He would
certainly have been hung had this test been in existence. Then there was
Mason of Bradford, and the notorious Muller, and Lefevre of Montpellier,
and Samson of new Orleans. I could name a score of cases in which it
would have been decisive."

"You seem to be a walking calendar of crime," said Stamford with a
laugh. "You might start a paper on those lines. Call it the 'Police News
of the Past.'"

"Very interesting reading it might be made, too," remarked Sherlock
Holmes, sticking a small piece of plaster over the prick on his finger.
"I have to be careful," he continued, turning to me with a smile, "for I
dabble with poisons a good deal." He held out his hand as he spoke, and
I noticed that it was all mottled over with similar pieces of plaster,
and discoloured with strong acids.

"We came here on business," said Stamford, sitting down on a high
three-legged stool, and pushing another one in my direction with
his foot. "My friend here wants to take diggings, and as you were
complaining that you could get no one to go halves with you, I thought
that I had better bring you together."

Sherlock Holmes seemed delighted at the idea of sharing his rooms with
me. "I have my eye on a suite in Baker Street," he said, "which would
suit us down to the ground. You don't mind the smell of strong tobacco,
I hope?"

"I always smoke 'ship's' myself," I answered.

"That's good enough. I generally have chemicals about, and occasionally
do experiments. Would that annoy you?"

"By no means."

"Let me see--what are my other shortcomings. I get in the dumps at
times, and don't open my mouth for days on end. You must not think I am
sulky when I do that. Just let me alone, and I'll soon be right. What
have you to confess now? It's just as well for two fellows to know the
worst of one another before they begin to live together."

I laughed at this cross-examination. "I keep a bull pup," I said, "and
I object to rows because my nerves are shaken, and I get up at all sorts
of ungodly hours, and I am extremely lazy. I have another set of vices
when I'm well, but those are the principal ones at present."

"Do you include violin-playing in your category of rows?" he asked,
anxiously.

"It depends on the player," I answered. "A well-played violin is a treat
for the gods--a badly-played one----"

"Oh, that's all right," he cried, with a merry laugh. "I think we may
consider the thing as settled--that is, if the rooms are agreeable to
you."

"When shall we see them?"

"Call for me here at noon to-morrow, and we'll go together and settle
everything," he answered.

"All right--noon exactly," said I, shaking his hand.

We left him working among his chemicals, and we walked together towards
my hotel.

"By the way," I asked suddenly, stopping and turning upon Stamford, "how
the deuce did he know that I had come from Afghanistan?"

My companion smiled an enigmatical smile. "That's just his little
peculiarity," he said. "A good many people have wanted to know how he
finds things out."

"Oh! a mystery is it?" I cried, rubbing my hands. "This is very piquant.
I am much obliged to you for bringing us together. 'The proper study of
mankind is man,' you know."

"You must study him, then," Stamford said, as he bade me good-bye.
"You'll find him a knotty problem, though. I'll wager he learns more
about you than you about him. Good-bye."

"Good-bye," I answered, and strolled on to my hotel, considerably
interested in my new acquaintance.
'''

from random import *
infile = open('words.txt','r')
WORDLIST = []
for line in infile:
    WORDLIST.append(line.strip())
print("We have", len(WORDLIST), "words on our list.")
infile.close()

DICT = { }
for word in WORDLIST:
    DICT[word] = 0
print("We have", len(DICT), "words in our dictionary.")

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def rotate(n: int) -> str:
    return ALPHABET[n:] + ALPHABET[0:n]

DT = []
for n in range(26):
    DT.append(str.maketrans(rotate(n), ALPHABET))

def Caesar_encrypt(s: str, n: int) -> str:
    T = str.maketrans(ALPHABET, rotate(n))
    return s.lower().translate(T)
assert(Caesar_encrypt("Cat",1)=="dbu")
assert(Caesar_encrypt("cat got YOUR tongue?", 26)=="cat got your tongue?")
assert(Caesar_encrypt("cat got YOUR tongue?", 0)=="cat got your tongue?")
assert(Caesar_encrypt("vote",3)=="yrwh")


def Caesar_break0(ciphertext: str, WORDS: 'collection') -> str:
    ''' Return decrypted version of ciphertext; try all possible keys and
        look up words in dictionary
    '''
    plaintext_hits_sofar = 0

    for i in range(26):
        hits = 0
        for word in ciphertext.strip().split():
            if word.translate(DT[i]) in WORDS:
                hits += 1
        if hits > plaintext_hits_sofar:
            plaintext_hits_sofar = hits
            plaintext = ciphertext.translate(DT[i])
    return plaintext

def Caesar_break(ciphertext: str, WORDS: 'collection') -> (str, int):
    ''' Return decrypted version of ciphertext; try all possible keys and
        look up words in dictionary
    '''
    plaintext_hits_sofar = 0

    total_lookups = 0
    for i in range(26):
        hits = 0
        for word in ciphertext.strip().split():
            total_lookups = total_lookups + 1
            if word.translate(DT[i]) in WORDS:
                hits += 1
        if hits > plaintext_hits_sofar:
            plaintext_hits_sofar = hits
            plaintext = ciphertext.translate(DT[i])
    print("Total lookups: ", total_lookups)
    return (plaintext, total_lookups)

from time import *

ciphertext = Caesar_encrypt(short_text, randint(0,26))
print(ciphertext)
'''
### THIS IS THE SHORT TEXT WITH WORDLIST
start = process_time()
print(Caesar_break0(ciphertext, WORDLIST))
end = process_time()
print("Elapsed time WORDLIST:", end - start)

### THIS IS THE SHORT TEXT WITH DICT
start = process_time()
print(Caesar_break0(ciphertext, DICT))
end = process_time()
print("Elapsed time DICT:", end - start)
'''

ciphertext = Caesar_encrypt(long_text, randint(0,26))
print(ciphertext)

### THIS IS THE LONG TEXT WITH DICT
start = process_time()
print(Caesar_break0(ciphertext, DICT))
end = process_time()
print("Elapsed time DICT:", end - start)
print()
print("Waiting for the list version to finish ...")
### THIS IS THE LONG TEXT WITH WORDLIST
start = process_time()
print(Caesar_break0(ciphertext, WORDLIST))
end = process_time()
print("Elapsed time WORDLIST:", end - start)

"""
EFFICIENCY:  It's not one simple question, faster or slower, more or less time.
    Human efficiency:
        End user:  Human-Computer Interaction
        Programmer/developer:  Software Engineering
        "People time is more expensive than computer time"
    Machine efficiency (computational resources:  CPU, memory, disk, i/o, power)
        Today we're talking about CPU (processor) time; the list version
            has to look at average 50,000 words to see if each plaintext word
            is there; the dict version goes right to the right place.
        There are whole different categories of performance.


"""




# ICS 31, Thursday 19 November 2015, 11am

"""
DICTIONARY (in Python, dict)
    Also called map or table or hash tables
    Key-value pair:  Look up an item's value by giving the key (w/ indexing)
        d[k] gives you the value associated with the key k
    We care because:
        -- Much better performance to look up an item, given key (k in d)
        -- More flexible indexing:  Keys can be anything immutable, not just nums

Dictionary requirements/characteristics:
    -- Keys must be an immutable type (not lists)
    -- Values can be anything
    -- Keys must be unique:   NOT:   {'x': 17, 'x':23}
    -- Order isn't specified:  Python gets to choose the order it stores things in.
        (This is a characteristic of HASH TABLES, the underlying mechanism
        behind dicts.)  But you can say (sorted(list(d)))
"""
'''
d = {'Donald Duck': 16, 'Daisy Duck': 17, 'Dewey Duck': 23,
     'Louie Duck': 34, 'Scrooge McDuck': 55, 'Huey Duck': 40}
print(d)
print(sorted(list(d)))
print("Dewey's age is", d['Dewey Duck'])
print(len(d), "ducks in our dictionary")

# We also have d.pop(key):  Both returns the value and removes the item
print()
print(d)
print(d.pop('Huey Duck'))
print(d)
print()

# We have d.update(d2):   Combine values in two dictionaries (later one prevails)
print(d)
d.update({'Dorothy Duck': 25, 'Daffy Duck': 23, 'Dewey Duck':39})
print(d)
print()

"""
Three more dict methods:
    d.keys()
    d.values()
    d.items()
    Each of these extracts data from a dictionary in a special form called a VIEW
"""
print(d.keys())
for k in d.keys():
    print("Next key is:", k)
duck_keys = d.keys()
print(duck_keys)
# print(duck_keys[2])   # Can't do this with a view, a dict_keys object

## Why do we have this oddball dict_keys thing?  Why not just return a plain list?
## Because views are SELF-UPDATING!

print()
print(d.values())
print()
print(d.items())
print()

print("Views vs. lists")
print("View version:")
vals = d.values()   # This is a VIEW, a dict_values object
print(vals)
print()
print("List version:")
vals_list = list(d.values())   # This is a normal LIST
print(vals_list)

# print(vals[2])
print(vals_list[2])

print("Average value:", sum(list(vals))/len(vals))
print("Average value:", sum(vals_list)/len(vals_list))

print()
d['Donald Duck'] = 999999999
print(d)
print()
print("Average value:", sum(list(vals))/len(vals))
print("Average value:", sum(vals_list)/len(vals_list))
print()
print(vals)
print(vals_list)
print()
vals_list = list(d.values())   # This is a normal LIST
print("Average value:", sum(list(vals))/len(vals))
print("Average value:", sum(vals_list)/len(vals_list))

'''

short_text = '''
A STUDY IN SCARLET.

PART I.

(_Being a reprint from the reminiscences of_ JOHN H. WATSON, M.D., _late
of the Army Medical Department._) [2]

CHAPTER I. MR. SHERLOCK HOLMES.

IN the year 1878 I took my degree of Doctor of Medicine of the
University of London, and proceeded to Netley to go through the course
prescribed for surgeons in the army. Having completed my studies there,
I was duly attached to the Fifth Northumberland Fusiliers as Assistant
Surgeon. The regiment was stationed in India at the time, and before
I could join it, the second Afghan war had broken out. On landing at
Bombay, I learned that my corps had advanced through the passes, and
was already deep in the enemy's country. I followed, however, with many
other officers who were in the same situation as myself, and succeeded
in reaching Candahar in safety, where I found my regiment, and at once
entered upon my new duties.
'''

long_text = '''
A STUDY IN SCARLET.
[copy removed to save space]
'''

from random import *
infile = open('words.txt','r')

WORDLIST = []
for line in infile:
    WORDLIST.append(line.strip())
print("We have", len(WORDLIST), "words on our list.")
infile.close()

DICT = { }
for word in WORDLIST:
    DICT[word] = 0
print("We have", len(DICT), "words in our dictionary.")

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def rotate(n: int) -> str:
    return ALPHABET[n:] + ALPHABET[0:n]

DT = []
for n in range(26):
    DT.append(str.maketrans(rotate(n), ALPHABET))

def Caesar_encrypt(s: str, n: int) -> str:
    T = str.maketrans(ALPHABET, rotate(n))
    return s.lower().translate(T)
assert(Caesar_encrypt("Cat",1)=="dbu")
assert(Caesar_encrypt("cat got YOUR tongue?", 26)=="cat got your tongue?")
assert(Caesar_encrypt("cat got YOUR tongue?", 0)=="cat got your tongue?")
assert(Caesar_encrypt("vote",3)=="yrwh")


def Caesar_break0(ciphertext: str, WORDS: 'collection') -> str:
    ''' Return decrypted version of ciphertext; try all possible keys and
        look up words in dictionary
    '''
    plaintext_hits_sofar = 0

    for i in range(26):
        hits = 0
        for word in ciphertext.strip().split():
            if word.translate(DT[i]) in WORDS:
                hits += 1
        if hits > plaintext_hits_sofar:
            plaintext_hits_sofar = hits
            plaintext = ciphertext.translate(DT[i])
    return plaintext

def Caesar_break(ciphertext: str, WORDS: 'collection') -> (str, int):
    ''' Return decrypted version of ciphertext; try all possible keys and
        look up words in dictionary
    '''
    plaintext_hits_sofar = 0

    total_lookups = 0
    for i in range(26):
        hits = 0
        for word in ciphertext.strip().split():
            total_lookups = total_lookups + 1
            if word.translate(DT[i]) in WORDS:
                hits += 1
        if hits > plaintext_hits_sofar:
            plaintext_hits_sofar = hits
            plaintext = ciphertext.translate(DT[i])
    print("Total lookups: ", total_lookups)
    return (plaintext, total_lookups)

from time import *

ciphertext = Caesar_encrypt(short_text, randint(0,26))
print(ciphertext)
'''
### THIS IS THE SHORT TEXT WITH WORDLIST
start = process_time()
print(Caesar_break0(ciphertext, WORDLIST))
end = process_time()
print("Elapsed time WORDLIST:", end - start)

### THIS IS THE SHORT TEXT WITH DICT
start = process_time()
print(Caesar_break0(ciphertext, DICT))
end = process_time()
print("Elapsed time DICT:", end - start)

### THIS IS THE LONG TEXT WITH DICT
ciphertext = Caesar_encrypt(long_text, randint(0,26))
print(ciphertext)
start = process_time()
print(Caesar_break0(ciphertext, DICT))
end = process_time()
print("Elapsed time DICT:", end - start)
'''
### THIS IS THE LONG TEXT WITH WORDLIST
ciphertext = Caesar_encrypt(long_text, randint(0,26))
start = process_time()
print("Waiting for decrypted version ...")
print(Caesar_break0(ciphertext, WORDLIST))
end = process_time()
print("Elapsed time WORDLIST:", end - start)

"""
EFFICIENCY:  There's a lot to say.
    It's not one simple question, faster or slower, more or less time.
    Human Efficiency
        End user:  Human-Computer Interaction
        Programmer/developer:   Software Engineering
    Machine efficiency:  Computational resources (processor time, memory, i/o, power)
        There are whole different categories of efficiency.
"""
