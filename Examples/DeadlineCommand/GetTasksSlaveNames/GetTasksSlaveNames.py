# This script Gets a job, and its tasks then cycles through the tasks 
# displaying which slave is rendering each task.

from Deadline.Scripting import *
from pprint import pprint


def __main__(*args):
	jobs = RepositoryUtils.GetJobs(True)
	for job in jobs:

		get_job(job)

		return job


def get_job(job):
	
	tasks = RepositoryUtils.GetJobTasks(job, True)
	
	for task in tasks:
		print task.TaskSlaveMachineName