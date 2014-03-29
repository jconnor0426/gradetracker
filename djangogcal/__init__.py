from django.conf import settings

from djangogcal.adapter import CalendarAdapter, CalendarEventData
from djangogcal.observer import CalendarObserver

from GradeTracker.models import Graded_Activities

class GradedCalendarAdapter(CalendarAdapter):
    """
    A calendar adapter for the Showing model.
    """
    
    def get_event_data(self, instance):
        """
        Returns a CalendarEventData object filled with data from the adaptee.
        """
        return CalendarEventData(
            start=instance.grade_due_date,
            end=instance.grade_due_date,
            title=instance.activity_name
        )

observer = CalendarObserver(email="alexdmail15@gmail.com",
                            password="vpmqesd43")
observer.observe(Graded_Activities, GradedCalendarAdapter())