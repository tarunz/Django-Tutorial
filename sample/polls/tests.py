from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

class QMT(TestCase):
	def pdate_future_check(self):
		time = timezone.now() + datetime.timedelta(days=30)
		fques = Question(pdate=time)
		self.assertEqual(fques.is_recent(), False)

	def pdate_past_check(self):
		time = timezone.now() - datetime.timedelta(days=-1)
    		old_question = Question(pdate=time)
    		self.assertEqual(old_question.is_recent(), False)

	def pdate_recent_check(self):
		time = timezone.now() - datetime.timedelta(hours=1)
    		recent_question = Question(pdate=time)
    		self.assertEqual(recent_question.is_recent(), True)
		
