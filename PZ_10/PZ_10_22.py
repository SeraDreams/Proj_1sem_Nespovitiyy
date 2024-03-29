"""
В N колхозах выращивают некоторые сельскохозяйственные культуры из имеющегося перечня.
Определить культуры, выращиваемые во всех колхозах, и культуры, выращиваемые только в
некоторых из них.
"""

# Список колхозов и выращиваемых культур
farms = {
    'Колхоз_1': {'пшеница', 'кукуруза', 'ячмень', 'гречка'},
    'Колхоз_2': {'пшеница', 'ячмень', 'овес'},
    'Колхоз_3': {'пшеница', 'ячмень', 'гречка'},
    'Колхоз_4': {'пшеница', 'ячмень', 'овес', 'гречка'},
    'Колхоз_5': {'пшеница', 'кукуруза', 'ячмень'},
}

# Культуры, выращиваемые во всех колхозах
all_culture = set.intersection(*farms.values())

# Культуры, выращиваемые только в некоторых колхозах
some_culture = set.union(*farms.values())

# Выводим результат
print("Культуры, выращиваемые во всех колхозах:")
for culture in all_culture:
    print(culture)

print("\nКультуры, выращиваемые только в некоторых колхозах:")
for culture in some_culture:
    print(culture)
