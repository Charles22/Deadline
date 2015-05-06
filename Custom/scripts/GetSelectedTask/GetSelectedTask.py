# Get selected tasks and print it's Slaves machine name to the console
from System.IO import *
from Deadline.Scripting import *
from DeadlineUI.Controls.Scripting.DeadlineScriptDialog import DeadlineScriptDialog

def __main__():

    global scriptDialog

    # Get the list of selected tasks.
    selectedTasks = MonitorUtils.GetSelectedTasks()

    for task in selectedTasks:
			print task.TaskSlaveMachineName