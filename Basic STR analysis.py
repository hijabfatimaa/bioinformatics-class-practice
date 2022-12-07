import re #We are imporating a module named "RegEx" aka Regular Expression in python
DNA_sequence = 'cagcaatcagcaacagcaacagcaacagcaatcagcagcagcagtcagc'
DNA = DNA_sequence.upper()
print(DNA)

pattern_match = re.finditer(r'(CAG|CAA){3,}', DNA)

match_list = []
for match in pattern_match:
    print(match.group())
    