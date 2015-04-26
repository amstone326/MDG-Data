
class Indicator:

    def __init__(self, indicator_num, target_measuring, goal_threshold, weight_given, directional_bool, max_val):
        self.indicator_num = indicator_num
        self.target = target_measuring
        self.goal_threshold = goal_threshold
        self.weight_given = weight_given
        self.increasing_goal = directional_bool  # True if goal is to increase, False if decrease
        self.max_overall_value = max_val
        self.aggr_initial = 0
        self.aggr_final = 0
        self.aggr_initial_yr = 0
        self.aggr_final_yr = 0
        self.aggr_rate_of_change = 0
        self.aggr_absolute_status = 0

    def set_aggregate_data(self, aggr_initial, aggr_final, initial_yr, final_yr):
        self.aggr_initial = aggr_initial
        self.aggr_final = aggr_final
        self.aggr_initial_yr = initial_yr
        self.aggr_final_yr = final_yr
        self.aggr_rate_of_change = rate_of_change(aggr_initial, aggr_final, final_yr-initial_yr, self.increasing_goal)
        self.aggr_absolute_status = self.goal_threshold.compute_absolute_status(self.aggr_initial, self.aggr_final,
                                                                                self.max_overall_value)

    def get_num(self):
        return self.indicator_num

    def get_goal_threshold(self):
        return self.goal_threshold

    def get_direction(self):
        return self.increasing_goal

    def get_aggr_rate_of_change(self):
        return self.aggr_rate_of_change

    def get_aggr_status(self):
        return self.aggr_absolute_status

    def get_weight(self):
        return self.weight_given

# Computes rate of change for the aggregate. If the indicator moved in the opposite of desired direction over
# the entire time span, aggregate rate of change is considered 0
def rate_of_change(initial, final, num_years, increasing_goal):
    if initial is None or final is None:
        return None
    if increasing_goal:
        if final <= initial:
            return 0.0
        else:
            return float(final-initial) / num_years
    else:
        if final >= initial:
            return 0.0
        else:
            return float(final-initial) / num_years * -1
