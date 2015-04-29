#Gets Job Dependency Paths
from Deadline.Scripting import *

assetList = []

def __main__(*args):
	jobs = RepositoryUtils.GetJobs(True)
	
	for job in jobs:
		for asset in job.JobRequiredAssets:
			print asset.FileName
