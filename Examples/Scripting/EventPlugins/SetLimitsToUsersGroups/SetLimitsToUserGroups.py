from System.Diagnostics import *
from System.IO import *
from System import TimeSpan

from Deadline.Events import *
from Deadline.Scripting import *

import re, sys, os

def GetDeadlineEventListener():
	return SetLimit()

def CleanupDeadlineEventListener( eventListener ):
	eventListener.Cleanup()

class SetLimit (DeadlineEventListener):
	def __init__( self ):
		self.OnJobSubmittedCallback += self.OnJobSubmitted

	def Cleanup( self ):
		del self.OnJobSubmittedCallback

	def OnJobSubmitted( self, job ):
		user = job.JobUserName
		groups = RepositoryUtils.GetUserGroupsForUser(user)
		limitgroups = RepositoryUtils.GetLimitGroups()

		for limit in limitgroups:
			print limit
			for group in groups:
				print group
				if group == limit:
					job.SetJobLimitGroups(limit)

		RepositoryUtils.SaveJob(job)
