
class GoalThreshold:

    def __init__(self, goal_type, target_value, directional_bool, max_observed_val):
        # Will be either EQUALS, GE (>=), or PROPORTION
        self.goal_type = goal_type

        # If type is any of the comparators, holds the value to compare to
        # If type is PROPORTION, holds the proportion being aimed for
        self.target_value = target_value

        # True if goal is to increase, False if decrease
        self.increasing_goal = directional_bool

        self.max_observed_val = max_observed_val

    # Returns how much progress toward this GoalThreshold is represented by initial_value and final_value,
    # as a percentage (so if the goal is reached, returns value of 1)
    def compute_absolute_status(self, initial_value, final_value):
        if self.goal_type == 'EQUALS':
            # If reached target value, return 1
            if final_value == self.target_value:
                return 1.0
            # If the goal is to increase this value, calculate percent to target value as usual
            if self.increasing_goal:
                return float(final_value) / self.target_value
            # If the goal is to decrease this value, calculate percent to target as progress made toward
            # the desired final value, starting from the max observed value
            print self.max_observed_val
            return (self.max_observed_val - final_value) / self.max_observed_val
        elif self.goal_type == 'GE':
            if final_value >= self.target_value:
                return 1.0
            return float(final_value) / self.target_value
        elif self.goal_type == 'PROPORTION':
            # If the value has increased, no progress has been made
            if final_value > initial_value:
                return 0.0
            proportion_reduced_by = float(initial_value - final_value) / initial_value
            #print 'PROPORTION REDUCED BY: ' + str(proportion_reduced_by)
            #print 'TARGET VALUE: ' + str(self.target_value)
            # If the proportional reduction is greater than the target, then the goal has been fully reached
            if proportion_reduced_by > self.target_value:
                return 1.0
            else:
                return proportion_reduced_by / self.target_value

    def get_target_value(self):
        return self.target_value

    def get_goal_type(self):
        return self.goal_type

