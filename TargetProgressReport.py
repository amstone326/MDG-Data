
#Represents, for one country, its progress on the specified target
class TargetProgressReport:

    def __init__(self, indicator_reports, target_num):
        self.indicator_reports = indicator_reports
        self.target_number = target_num
        self.country_id = indicator_reports[0].get_country_id()
        self.country_name = indicator_reports[0].get_country_name()
        self.num_indicators = len(indicator_reports)
        self.absolute_status = 0
        self.comparative_absolute_status = 0
        self.progress_rate = 0
        self.comparative_progress_rate = 0
        self.compute_metrics()

    # Compute the overall metrics for this target, as the averages over all indicators
    def compute_metrics(self):
        #print 'TARGET NUM in TPR: ' + self.target_number
        #print 'COUNTRY: ' + self.country_name
        num_indicators = len(self.indicator_reports)
        for report in self.indicator_reports:
            #print '    indicator num: ' + report.get_num()
            absolute_status_piece = report.get_absolute_status() / num_indicators
            rate_piece = report.get_progress_rate() / num_indicators
            comparative_rate_piece = report.get_comparative_rate() / num_indicators
            comparative_status_piece = report.get_comparative_status() / num_indicators
            self.absolute_status += absolute_status_piece
            self.progress_rate += rate_piece
            self.comparative_progress_rate += comparative_rate_piece
            self.comparative_absolute_status += comparative_status_piece

    def get_absolute_status(self):
        return self.absolute_status

    def get_progress_rate(self):
        return self.progress_rate

    def get_comparative_progress_rate(self):
        return self.comparative_progress_rate

    def get_comparative_absolute_status(self):
        return self.comparative_absolute_status

    def get_country_name(self):
        return self.country_name

    def get_country_id(self):
        return self.country_id
