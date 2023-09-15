crew_members = ['nika qatamazde', 'alex rajavi', 'vako chxaizde', 'anastasia ferazde', 'vefxvia babajanshvili', 'roba amonashvili']
big_crew_members = []
for crew_members_char in crew_members:
    if len(crew_members_char) >= 17:
        big_crew_members.append(crew_members_char)
print(big_crew_members)