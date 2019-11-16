from django.db import models

class Timeslot(models.Model):
    appointment_id = models.IntegerField()
    account_id = models.IntegerField()
    title = models.CharField(max_length=100)

    start_date = models.DateField ()
    end_date = models.DateField ()

    def __str__(self):
        return str(self.end_date)

    def get_start_date(self):
        return self.start_date

    class Meta:
        db_table = "timeslot_test"

class Reports_assessments(models.Model):
    session_id = models.IntegerField()
    provider_id = models.IntegerField()
    patient_id = models.IntegerField()
    icd_id = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "reports_assessments"

# class Timeslot(models.Model):
#     account_id = models.IntegerField()
#     session_id = models.IntegerField()
#     slice_probabilities = models.TextField(max_length=100)
#     response_time = models.CharField(max_length=100)
#     threshold = models.FloatField()
#     PHQ8 = models.IntegerField()
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.account_id)

#     class Meta:
#        



