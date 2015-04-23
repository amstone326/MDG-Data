import Indicator as I
import Target as T
import GoalThreshold as GT
from sets import Set

#Target descriptions
desc_1A = "Halve, between 1990 and 2015, the proportion of people whose income is less than one dollar a day"
desc_1B = "Achieve full and productive employment and decent work for all, including women and young people"
desc_1C = "Halve, between 1990 and 2015, the proportion of people who suffer from hunger"
desc_2A = "Ensure that, by 2015, children everywhere, boys and girls alike, will be able to complete a full " \
          "course of primary schooling"
desc_3A = "Eliminate gender disparity in primary and secondary education, preferably by 2005, and in all levels " \
          "of education no later than 2015"
desc_4A = "Reduce by two-thirds, between 1990 and 2015, the under-five mortality rate"
desc_5A = "Reduce by three quarters, between 1990 and 2015, the maternal mortality ratio"
desc_5B = "Achieve, by 2015, universal access to reproductive health"
desc_6A = "Have halted by 2015 and begun to reverse the spread of HIV/AIDS"
desc_6B = "Achieve, by 2010, universal access to treatment for HIV/AIDS for all those who need it"


def init():
    targets = create_targets_and_indicators()
    all_countries = []
    for target in targets:
        countries_in_target = target.parse_all_indicators()
        all_countries.extend(countries_in_target)
    all_countries = set(all_countries)
    for target in targets:
        target.create_csv_file(all_countries)


def missing_countries(countries_in_mdgs):
    f = open('shapefile_countries.txt', 'r')
    shapefile_countries = set()
    country = f.readline().strip()
    while country != '':
        shapefile_countries.add(country)
        country = f.readline().strip()
    #print shapefile_countries
    #for country in countries_in_mdgs:
     #   if country not in shapefile_countries:
      #      print country
    # Countries not dealt with: French Guiana, Tokelau, Reunion, Martinique, Guadeloupe


def create_targets_and_indicators():
    targets = []

    # Indicator 1.1
    threshold_1_1 = GT.GoalThreshold('PROPORTION', .5, False, -1)
    indicator_1_1 = I.Indicator('1_1', '1A', threshold_1_1, 1.0, False)
    indicator_1_1.set_aggregate_data(46.7, 22, 1990, 2010)

    # CREATE TARGET 1A
    target_1a = T.Target('1A', desc_1A)
    target_1a.set_indicators(Set([indicator_1_1]))
    targets.append(target_1a)

    # Indicator 1.5
    threshold_1_5 = GT.GoalThreshold('EQUALS', 100, True, -1)
    indicator_1_5 = I.Indicator('1_5', '1B', threshold_1_5, .5, True)
    indicator_1_5.set_aggregate_data(64.1, 60.8, 1991, 2013)

    # Indicator 1.6
    threshold_1_6 = GT.GoalThreshold('EQUALS', 0, False, 96.7)
    indicator_1_6 = I.Indicator('1_6', '1B', threshold_1_6, .5, False)
    indicator_1_6.set_aggregate_data(46.9, 14.5, 1991, 2013)

    # CREATE TARGET 1B
    target_1b = T.Target('1B', desc_1B)
    target_1b.set_indicators(Set([indicator_1_5, indicator_1_6]))
    targets.append(target_1b)

    # Indicator 1.9
    threshold_1_9 = GT.GoalThreshold('PROPORTION', .5, False, -1)
    indicator_1_9 = I.Indicator('1_9', '1C', threshold_1_9, 1.0, False)
    indicator_1_9.set_aggregate_data(23.6, 14.3, 1990, 2013)

    # CREATE TARGET 1C
    target_1c = T.Target('1C', desc_1C)
    target_1c.set_indicators(Set([indicator_1_9]))
    targets.append(target_1c)

    # Indicator 2.1
    threshold_2_1 = GT.GoalThreshold('EQUALS', 100, True, -1)
    indicator_2_1 = I.Indicator('2_1', '2A', threshold_2_1, .5, True)
    indicator_2_1.set_aggregate_data(79.8, 90.5, 1991, 2012)

    # Indicator 2.2
    threshold_2_2 = GT.GoalThreshold('EQUALS', 100, True, -1)
    indicator_2_2 = I.Indicator('2_2', '2A', threshold_2_2, .5, True)
    indicator_2_2.set_aggregate_data(67.4, 72.7, 1991, 2011)

    # CREATE TARGET 2A
    target_2a = T.Target('2A', desc_2A)
    target_2a.set_indicators(Set([indicator_2_1, indicator_2_2]))
    targets.append(target_2a)

    # Indicator 3.1 pt. 1 (primary school)
    threshold_3_1a = GT.GoalThreshold('GE', 1, True, -1)
    indicator_3_1a = I.Indicator('3_1a', '3A', threshold_3_1a, 1.0/3, True)
    indicator_3_1a.set_aggregate_data(.87, .97, 1991, 2012)

    # Indicator 3.1 pt 2 (secondary school)
    threshold_3_1b = GT.GoalThreshold('GE', 1, True, -1)
    indicator_3_1b = I.Indicator('3_1b', '3A', threshold_3_1b, 1.0/3, True)
    indicator_3_1b.set_aggregate_data(.77, .96, 1991, 2012)

    # Indicator 3.1 pt 3 (tertiary school)
    threshold_3_1c = GT.GoalThreshold('GE', 1, True, -1)
    indicator_3_1c = I.Indicator('3_1c', '3A', threshold_3_1c, 1.0/3, True)
    indicator_3_1c.set_aggregate_data(.71, .99, 1991, 2012)

    # CREATE TARGET 3A
    target_3a = T.Target('3A', desc_3A)
    target_3a.set_indicators(Set([indicator_3_1a, indicator_3_1b, indicator_3_1c]))
    targets.append(target_3a)

    # Indicator 4.1
    threshold_4_1 = GT.GoalThreshold('PROPORTION', 2.0/3, False, -1)
    indicator_4_1 = I.Indicator('4_1', '4A', threshold_4_1, 1.0, False)
    indicator_4_1.set_aggregate_data(99, 53, 1990, 2012)

    # CREATE TARGET 4A
    target_4a = T.Target('4A', desc_4A)
    target_4a.set_indicators(Set([indicator_4_1]))
    targets.append(target_4a)

    # Indicator 5.1
    threshold_5_1 = GT.GoalThreshold('PROPORTION', .75, False, -1)
    indicator_5_1 = I.Indicator('5_1', '5A', threshold_5_1, 1.0, False)
    indicator_5_1.set_aggregate_data(430, 230, 1990, 2013)

    # CREATE TARGET 5A
    target_5a = T.Target('5A', desc_5A)
    target_5a.set_indicators(Set([indicator_5_1]))
    targets.append(target_5a)

    # Indicator 5.5
    threshold_5_5 = GT.GoalThreshold('EQUALS', 100, True, -1)
    indicator_5_5 = I.Indicator('5_5', '5B', threshold_5_5, .5, True)
    indicator_5_5.set_aggregate_data(65, 83, 1990, 2012)

    # Indicator 5.6
    threshold_5_6 = GT.GoalThreshold('EQUALS', 0, False, 55.9)
    indicator_5_6 = I.Indicator('5_6', '5B', threshold_5_6, .5, False)
    indicator_5_6.set_aggregate_data(16.5, 12.4, 1990, 2012)

    # CREATE TARGET 5B
    target_5b = T.Target('5B', desc_5B)
    target_5b.set_indicators(Set([indicator_5_5, indicator_5_6]))
    targets.append(target_5b)

    # Indicator 6.1
    threshold_6_1 = GT.GoalThreshold('EQUALS', 0, False, 5.95)
    indicator_6_1 = I.Indicator('6_1', '6A', threshold_6_1, 1.0, False)
    indicator_6_1.set_aggregate_data(.1, .06, 2001, 2012)

    # CREATE TARGET 6A
    target_6a = T.Target('6A', desc_6A)
    target_6a.set_indicators(Set([indicator_6_1]))
    targets.append(target_6a)

    # Indicator 6.5
    threshold_6_5 = GT.GoalThreshold('EQUALS', 100, True, -1)
    indicator_6_5 = I.Indicator('6_5', '6B', threshold_6_5, 1.0, True)
    indicator_6_5.set_aggregate_data(46, 61, 2010, 2012)

    # CREATE TARGET 6B
    target_6b = T.Target('6B', desc_6B)
    target_6b.set_indicators(Set([indicator_6_5]))
    targets.append(target_6b)

    return targets

init()