# hw 4 - Sasha Martynova
from nltk.corpus import wordnet
from nltk.wsd import lesk

# task 1
all_syn = wordnet.synsets('plant')
for syn in all_syn:
    print(syn, syn.definition())
print('\r\n')

# task 2
set1 = wordnet.synset('plant.n.01')
set2 = wordnet.synset('plant.n.02')

# task 3
sent_set1 = 'during this study, the mother was employed at a nearby chicken plant, ' \
            'along with the eldest brother'.split()
sent_set2 = 'looking at a bright bouquet or a plant that can change daily brings life ' \
            'to someone who can not get out into nature'.split()

print('for meaning plant.n.01:', lesk(sent_set1, 'plant'))
print('for meaning plant.n.02:', lesk(sent_set2, 'plant'))
print('алгоритм работает так себе', '\r\n')

# # task 4
print('hypernyms for set1:', set1.hypernyms())
print('hypernyms for set2:', set2.hypernyms(), '\r\n')

# task 5
industrys = wordnet.synsets('industry')
leafs = wordnet.synsets('leaf')
ind_sim = [set1.path_similarity(industry) for industry in industrys]
leaf_sim = [set2.path_similarity(leaf) for leaf in leafs]
ind_rast = [set2.path_similarity(industry) for industry in industrys]
leaf_zavod = [set1.path_similarity(leaf) for leaf in leafs]


print('min расстояние между plant "завод" и industry:', min(x for x in ind_sim if x is not None))
print('min расстояние между plant "растение" и leaf:', min(x for x in leaf_sim if x is not None))
print('Я не очень оняла задание, в котором надо найти минимум между (d(plant: "завод", industry), '
      'd(plant: "завод", leaf)) и т.д....')
print('min (d(plant: "завод", industry), d(plant: "завод", leaf)):', min(x for x in ind_sim+ind_rast if x is not None))
print('min (d(plant: "растение", industry), d(plant: "растение", leaf)):', min(x for x in leaf_sim+leaf_zavod if x
                                                                               is not None), '\r\n')

# task 6
trafka = wordnet.synsets("rattlesnake's_master")
organism = wordnet.synsets('organism')
whole = wordnet.synsets('whole')

# tr_sim1 = min(x for x in [set2.wup_similarity(trava) for trava in trafka] if x is not None)
# tr_sim2 = min(x for x in [set2.lch_similarity(trava) for trava in trafka] if x is not None)

wup_tr = []
path_tr = []
for tr in trafka:
    print(tr, '---', tr.definition())
    sim_wup = set2.wup_similarity(tr)
    sim_path = set2.path_similarity(tr)
    wup_tr.append(sim_wup)
    path_tr.append(sim_path)
    print('wup:', sim_wup, 'path:', sim_path)
print("RESULT! plant: 'растение', rattlesnake's master: ", min(wup_tr), min(path_tr), '\r\n')

wups = []
paths = []
for org in organism:
    print('\r\n', org, ':::', org.definition())
    for wh in whole:
        print(wh, '---', wh.definition())
        sim_wup = org.wup_similarity(wh)
        sim_path = org.path_similarity(wh)
        wups.append(sim_wup)
        paths.append(sim_path)
        print('wup:', sim_wup, 'path:', sim_path)
print('RESULT! d(organism, whole) ---  ', 'wup:', min(x for x in wups if x is not None), 'path:', min(x for x in paths if x
                                                                                              is not None), '\r\n')
print('Разница в расстояниях при вычислении двумя способами есть, но она не сильно различается, если отранжировать все '
      'расстояния внутри одного способа. Но кажется, что wup лучше отражает интуитивное '
      'представление о семантической близости.')
