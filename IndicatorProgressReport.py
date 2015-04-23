

class IndicatorProgressReport:

    def __init__(self, comparison_indicator, country_id, country_name, earliest_year, earliest_value,
                 latest_year, latest_value):
        self.comparison_indicator = comparison_indicator  # of type Indicator
        self.country_id = country_id
        self.country_name = country_name
        self.earliest_year = earliest_year
        self.earliest_value = earliest_value
        self.latest_year = latest_year
        self.latest_value = latest_value
        self.progress_rate = 0
        self.comparative_progress_rate = 0
        self.absolute_status = 0
        self.comparative_absolute_status = 0

        # Compute all measures
        self.compute_rate_and_comparative_rate()
        self.compute_status_and_comparative_status()

    # METRICS 1 & 2: Computes the country's rate of progress on this indicator, and also compares
    # it to the aggregate rate of progress over all developing countries
        # --Special Case: If the latest value was farther away from the goal than it's earliest one, sets both to 0
    def compute_rate_and_comparative_rate(self):
        goal_to_increase = self.comparison_indicator.get_direction()
        if goal_to_increase and self.latest_value <= self.earliest_value:
            self.progress_rate = 0.0
            self.comparative_progress_rate = 0.0
        elif (not goal_to_increase) and self.latest_value >= self.earliest_value:
            self.progress_rate = 0.0
            self.comparative_progress_rate = 0.0
        else:
            rate_of_progress = rate_of_change(self.earliest_value, self.latest_value,
                                              self.latest_year - self.earliest_year)
            if not goal_to_increase:
                rate_of_progress *= -1
            self.progress_rate = rate_of_progress
            aggr_rate = self.comparison_indicator.get_aggr_rate_of_change()
            # If the aggregate rate of change was set to 0 because the aggregate moved in the wrong overall direction,
            # then comparative rate is just computed as personal rate
            if aggr_rate == 0:
                self.comparative_progress_rate = rate_of_progress
            else:
                self.comparative_progress_rate = rate_of_progress / aggr_rate

    # METRICS 3 & 4: Computes the country's absolute status for this indicator, based on its goal threshold,
    # and also compares it to the aggregate absolute status over all developing countries
    def compute_status_and_comparative_status(self):
        goal_threshold = self.comparison_indicator.get_goal_threshold()
        self.absolute_status = goal_threshold.compute_absolute_status(self.earliest_value, self.latest_value)
        aggr_status = self.comparison_indicator.get_aggr_status()
        self.comparative_absolute_status = self.absolute_status / aggr_status

    def get_progress_rate(self):
        return self.progress_rate

    def get_comparative_rate(self):
        return self.comparative_progress_rate

    def get_absolute_status(self):
        return self.absolute_status

    def get_comparative_status(self):
        return self.comparative_absolute_status

    def get_country_id(self):
        return self.country_id

    def get_country_name(self):
        return self.country_name

    def get_weight(self):
        return self.comparison_indicator.get_weight()

    def get_num(self):
        return self.comparison_indicator.get_num()

def rate_of_change(initial, final, num_years):
    return float(final-initial) / num_years
