#!/usr/bin/python
# -*- coding: utf-8 -*-

import IndicatorParser as IP
import TargetProgressReport as TPR
import csv

class Target:

    def __init__(self, number, description):
        self.target_num = number
        self.description = description
        self.indicators = {}
        # A list of the TargetProgressReports for each country that had data available on this target
        self.country_reports = []
        self.aggregate_rate = 0
        self.aggregate_absolute_status = 0

    def set_indicators(self, indicators):
        self.indicators = indicators
        self.compute_aggregate_statistics()


    def get_indicators(self):
        return self.indicators

    def parse_all_indicators(self):
        # (country_id --> {IndicatorProgressReport})
        countries_dict = dict()

        for indicator in self.get_indicators():
            parser = IP.IndicatorParser(indicator)
            # IndicatorParser.parse() returns a dict of type: (country_id --> IndicatorProgressReport)
            country_to_report_dict = parser.parse()
            # Add the report for each country to the growing list of reports for each country
            for country_id in country_to_report_dict:
                if country_id in countries_dict:
                    reports = countries_dict[country_id]
                else:
                    reports = []
                reports.append(country_to_report_dict[country_id])
                countries_dict[country_id] = reports

        # Now calculate aggregate progress for each country on the entire target, based on all indicators
        country_list = []
        for country_id in countries_dict:
            # Will be as many IndicatorReports for each country as indicators being used to evaluate this target,
            # UNLESS the country was missing data for some of the indicators (very possible)
            reports = countries_dict[country_id]
            target_report = TPR.TargetProgressReport(reports, self.target_num)
            country_list.append(target_report.get_country_name())
            self.country_reports.append(target_report)
        return country_list

    def compute_aggregate_statistics(self):
        num_indicators = len(self.indicators)
        for indicator in self.indicators:
            self.aggregate_absolute_status += indicator.get_aggr_status() / num_indicators
            self.aggregate_rate += indicator.get_aggr_rate_of_change() / num_indicators
        #print 'Target num: ' + self.target_num
        #print '    Aggregate absolute status: ' + str(self.aggregate_absolute_status)
        #print '    Aggregate rate: ' + str(self.aggregate_rate)


    def create_csv_file(self, all_countries):
        filename = "csv_files/" + self.target_num + '.csv'
        with open(filename, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(['c_id', 'c_name', 'rate', 'c_rate', 'a_rate', 'status', 'c_status', 'a_status', 'in'])
            countries_with_data = set()
            for report in self.country_reports:
                country_name = sanitize_country_name(report.get_country_name())
                countries_with_data.add(country_name)
                writer.writerow([report.get_country_id(), country_name, report.get_progress_rate(),
                                 report.get_comparative_progress_rate(), self.aggregate_rate,
                                 report.get_absolute_status(), report.get_comparative_absolute_status(),
                                 self.aggregate_absolute_status, 1])
            unrepresented_countries = set()
            for country in all_countries:
                unrepresented_countries.add(sanitize_country_name(country))
            unrepresented_countries = unrepresented_countries.difference(countries_with_data)
            for country in unrepresented_countries:
                writer.writerow([0, country, 0, 0, self.aggregate_rate, 0, 0, self.aggregate_absolute_status, 1])


# Change the names of a few countries so they match up correctly with shapefile later
def sanitize_country_name(country_name):
    if country_name == 'Libyan Arab Jamahiriya':
        return 'Libya'
    if country_name == 'Viet Nam':
        return 'Vietnam'
    if country_name == 'Iran (Islamic Republic of)':
        return 'Iran'
    if country_name == 'Syrian Arab Republic':
        return 'Syria'
    if country_name == 'Micronesia, Federated States of':
        return 'Federated States of Micronesia'
    if country_name == 'Korea, Republic of':
        return 'Republic of Korea'
    if country_name == "Lao People's Democratic Republic":
        return "Lao PDR"
    if country_name == 'Gambia':
        return 'The Gambia'
    if country_name == 'United Republic of Tanzania':
        return 'Tanzania'
    if country_name == 'State of Palestine':
        return 'Palestine'
    if country_name == 'Sudan (former)':
        return 'Sudan'
    if country_name == 'Congo':
        return 'Democratic Republic of the Congo'
    if country_name == "Korea, Democratic People's Republic of":
        return 'Dem. Rep. Korea'
    if country_name == "Cote d'Ivoire":
        return "Côte d'Ivoire"
    if country_name == "Sao Tome and Principe":
        return "São Tomé and Príncipe"
    return country_name