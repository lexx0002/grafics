%matplotlib inline
import pandas as pd
import os

def Ruth_and_Robert():

    PATH = os.getcwd()
    names_by_year = {}
    for year in range(1900, 2000):
        file_path = PATH + '/names/yob{}.txt'.format(year)
        names_by_year[year] = pd.read_csv(file_path,
        names=['Name','Gender','Count'])
        names_all = pd.concat(names_by_year, names=['Year', 'Pos'])

    name_dynamics_cols = (names_all.groupby([names_all.index.get_level_values(0),'Name'])
    .sum()
    .query('Name == ["Ruth", "Robert"]')
    .unstack('Name')
    ).plot()

def Ruth_and_Robert_histogram():

    PATH = os.getcwd()
    names_by_year = {}
    for year in range(1900, 2000, 5):
        file_path = PATH + '/names/yob{}.txt'.format(year)
        names_by_year[year] = pd.read_csv(file_path,
        names = ['Name','Gender','Count'])
        names_all = pd.concat(names_by_year, names = ['Year', 'Pos'])

    name_dynamics_cols = (names_all.groupby([names_all.index.get_level_values(0),'Name'])
    (names_all.groupby([names_all.index.get_level_values(0), 'Name'])
    .sum()
    .query('Name == ["Ruth", "Robert"]')
    .unstack('Name')
    ).plot.bar()

def names_R_circle(number_names_R):
    PATH = os.getcwd()
    year = 1950
    file_path = PATH + '/names/yob{}.txt'.format(year)
    names_by_year = pd.read_csv(file_path, names=['Name','Gender','Count'])
    pattern = 'R.*'
    names_R = names_by_year[names_by_year.Name.str.contains(pattern)]
    (names_R
    .groupby('Name')
    .sum()
    .sort_values(by = 'Count', ascending = False)
    .head(number_names_R)
    ).plot.pie(y = 'Count')

def name_consonant(row):
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z',
                  'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    count_consonants = 0
    for letter in row.Name:
        if letter in consonants:
            count_consonants += 1
    row.Name = count_consonants
    return row

def consonant_in_names_point(interval):
    PATH = os.getcwd()
    names_by_year = {}
    for year in range(1900, 2000, interval):
        file_path = PATH + '/names/yob{}.txt'.format(year)
        names_by_year[year] = pd.read_csv(file_path, names = ['Name', 'Gender', 'Count'])
        names_all = pd.concat(names_by_year, names = ['Year', 'Pos'])
    name_by_consonants = names_all.apply(name_consonant, axis = 1)
    name_by_consonants.plot.scatter(x = 'Name', y = 'Count')

Ruth_and_Robert()

Ruth_and_Robert_histogram()

number_names_R = 7
names_R_circle(number_names_R)

interval = 25
consonant_in_names_point(interval)
