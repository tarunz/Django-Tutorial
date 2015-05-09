from django.db import models

class Question(models.Model):
	def __str__(self):
		return self.qtext

	def is_recent(self):
		now =timezone.now()
		return now -  datetime.timedelta(days=1 )<= self.pdate <= now
	qtext = models.CharField(max_length=250)
	pdate = models.DateTimeField('Date Published')

class Choice(models.Model):
	def __unicode__(self):
		return self.ctext

	Q = models.ForeignKey(Question)
	ctext = models.CharField(max_length=250)
	votes = models.IntegerField(default=0)
#question_text => qtext
#pub_date => pdate
#question => Q
#choice_text => ctext

