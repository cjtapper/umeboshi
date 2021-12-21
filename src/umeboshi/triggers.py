from django.db import models
from django.utils.translation import gettext_lazy as _


class TriggerBehavior(models.TextChoices):

    """
    Trigger Behaviors govern when to allow an Event to be scheduled.
    """

    DEFAULT = "default", _("Default")

    # Disallow if there is already an event with this name/data waiting to be
    # processed.
    SCHEDULE_ONCE = "schedule-once", _("Schedule once")

    # Disallow if an event with this name/data has run successfully.
    RUN_ONCE = "run-once", _("Run once")

    # Disallow if an event with this name/data has run successfully, or is
    # scheduled to run.
    RUN_AND_SCHEDULE_ONCE = "run-and-schedule-once", _("Run and schedule once")

    # Cancel any waiting events and schedule this one instead.
    LAST_ONLY = "last-only", _("Last only")

    # Delete event after processing
    DELETE_AFTER_PROCESSING = "delete-after-processing", _("Delete after processing")
