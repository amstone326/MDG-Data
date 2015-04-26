import xml.etree.ElementTree as ET
import IndicatorProgressReport as IPR


class IndicatorParser:

    def __init__(self, indicator):
        self.comparison = indicator
        self.indicator_num = indicator.get_num()
        self.filename = "xml_files/" + self.indicator_num + ".xml"

    def parse(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        indicator_description = root.get('name')
        series = root.find('series')
        # map from: country_id --> IndicatorReport  (one for each country that has data for this indicator)
        reports_dict = dict()
        for country in series.findall('country'):
            report = self.parse_country(country)
            if report is not None:
                reports_dict[report.get_country_id()] = report
        return reports_dict

    def parse_country(self, country):
        country_id = country.get('id')
        country_name = country.get('name')
        first_year_found = False
        earliest_year = 0
        earliest_value = 0
        latest_year = 0
        latest_value = 0
        max_value = 0
        for data in country.findall('seriesData'):
            value = data.get('value')
            if value is not None:
                year = data.get('year')
                if first_year_found:
                    latest_year = int(year)
                    latest_value = float(value)
                else:
                    earliest_year = int(year)
                    earliest_value = float(value)
                    first_year_found = True
                if float(value) > max_value:
                    max_value = float(value)

        # Since almost all evaluative metrics being used depend on an initial and final data point,
        # only making progress reports if 2 data points are available
        if latest_year != 0:
            return IPR.IndicatorProgressReport(self.comparison, country_id, country_name, earliest_year,
                                               earliest_value, latest_year, latest_value, max_value)
        else:
            return None