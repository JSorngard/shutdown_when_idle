Simple script made for my own use that shuts down the computer when the cpu usage is below a given percent.  
Should not be used if you need your computer to shut down as soon as this happens, as this scipt only checks the average usage every now and then. The indended use is for if you are running a long running job, and need to leave your computer unattended, but still want it to shut down when done.

By default the script checks if the average usage is below 1\% every ten seconds, but this can be changed using command line arguments. That value is appropriate for my desktop machine, but a laptop or older computer might use more of its cpu when idling.
