import collections
import arff
import re
import string

name, is_sparse, attributes, rows = arff.arffread(open('winners_losers.arff', 'rb'))

#writer = csv.writer(open('winners_losers_augmented.csv', 'wb'))

def character_frequencies(input_string, allowed_character_set):
    frequencies = {}

    for character in allowed_character_set:
    	frequencies[character] = 0

    for character in string.lower(input_string):
    	if(character in allowed_character_set):
        	frequencies[character] += 1
    return frequencies


english_characters = [chr(i) for i in range(ord('a'), ord('z')+1)]

output_rows = []

name_sizes = []

for row in rows:

	full_name = row[0]
	classification = row[1]

	name_chars = full_name.replace(' ', '').replace('.', '')
	name_sizes.append(len(name_chars))

	#
	#letter features
	#
	vowels = consonants = 0
	letter_positions = []
	letter_parities = []
	letter_types = []

	for i in range(len(full_name)):
		char = full_name[i].lower()
		
		#letter positions
		letter_position = ord(char)-ord('a')
		letter_positions.append(letter_position)

		#letter parities
		letter_parities.append(letter_position % 2 == 0)

		#phonetic classes
		if char in 'aeiou':
			vowels += 1
			letter_types.append('v')
		else:
			consonants += 1
			letter_types.append('c')

	#
	#name features
	#
	names = full_name.split(' ')

	#name length parities
	first_name_length_parity = len(names[0]) % 2 == 0
	last_name_length_parity = len(names[-1]) % 2 == 0


	#
	#store the features for output
	#
	output_rows.append([full_name] +
						[vowels, consonants] +
						letter_positions[0:6] +
						letter_parities[0:6] +
						letter_types[0:6] +
						[first_name_length_parity, last_name_length_parity] +
						[classification])

print "shortest name length:"
print min(name_sizes)

attributes = []

attributes.append(('person_name', 0, []))

attributes.append(('total_vowels', 1, []))
attributes.append(('total_consonants', 1, []))

attributes += [("pos_%d" % i, 1, []) for i in range(6)]
attributes += [("par_%d" % i, 0, ['True','False']) for i in range(6)]
attributes += [("type_%d" % i, 0, ['v','c']) for i in range(6)]

attributes.append(('first_name_length_parity', 0, ['True','False']))
attributes.append(('last_name_length_parity', 0, ['True','False']))
attributes.append(('class', 0, ['+','-']))

arff.arffwrite(open('winners_losers_augmented.arff', 'wb'),
				attributes,
				output_rows,
				'winners_losers')
