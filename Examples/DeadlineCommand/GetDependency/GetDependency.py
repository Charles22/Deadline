# This script Gets the jobs in monitor and cycles through them retrieving the file paths of
# job dependencies

from Deadline.Scripting import *

def __main__(*args):
	jobs = RepositoryUtils.GetJobs(True)
	
	for job in jobs:
		for asset in job.JobRequiredAssets:
			print asset.FileName