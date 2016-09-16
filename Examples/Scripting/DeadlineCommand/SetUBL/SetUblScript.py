from Deadline.Scripting import *

URL = "Replace with URL"
activation = "Replace with Activation Code"

def __main__(*args):

    networkObj = RepositoryUtils.GetNetworkSettings()
    networkObj.UsageBasedURL = URL
    networkObj.UsageBasedActivationCode = activation
    networkObj.UseCloudLicenseServer = True
    networkObj = RepositoryUtils.GetNetworkSettings()
    RepositoryUtils.SaveNetworkSettings(networkObj)