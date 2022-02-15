class Device:

    def __init__(device, userId, function, metric):
        device.userId = userId
        device.function = function
        device.metric = metric

    def metricRetreive(self):
        return self.metric

    def metricUpdate(self, metric):
        self.metric = metric
