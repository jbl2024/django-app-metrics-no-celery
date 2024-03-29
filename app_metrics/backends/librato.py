from app_metrics.tasks import librato_metric_task


def _get_func(async):
    return librato_metric_task if async else librato_metric_task


def metric(slug, num=1, async=True, **kwargs):
    _get_func(async)(slug, num, type="counter", **kwargs)


def timing(slug, seconds_taken, async=True, **kwargs):
    """not implemented"""


def gauge(slug, current_value, async=True, **kwargs):
    _get_func(async)(slug, current_value, type="gauge", **kwargs)
