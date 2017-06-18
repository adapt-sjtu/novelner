import sys
filename = sys.argv[1]
#filename = 'train'
f = open(filename)
mapping = dict()
mapping['B-company'] = 'B-corporation'
mapping['I-company'] = 'I-corporation'

mapping['B-geo-loc'] = 'B-location'
mapping['I-geo-loc'] = 'I-location'

mapping['B-facility'] = 'B-location'
mapping['I-facility'] = 'I-location'

mapping['B-other'] = 'B-group' # Group (subsuming music band, sports team, and non-corporate organisations)
mapping['I-other'] = 'I-group' # other Non-ProfitOrganisation, Event, SportsLeague, PoliticalParty, MilitaryUnit

mapping['B-sportsteam'] = 'B-group'
mapping['I-sportsteam'] = 'I-group'

mapping['B-movie'] = 'B-creativework'
mapping['I-movie'] = 'I-creativework'

mapping['B-tvshow'] = 'B-creativework'
mapping['I-tvshow'] = 'I-creativework'

mapping['B-musicartist'] = 'B-person'
mapping['I-musicartist'] = 'I-person'

for line in f.readlines():
    line = line.rstrip()
    if len(line) == 0:
        print line
        continue
    token = line.split('\t')[0]
    tag = line.split('\t')[1]
    if tag in mapping:
        print token+'\t'+mapping[tag]
    else:
        print line

