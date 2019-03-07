USAGE: parse_mmaker_data.py <log copied from chimera> <subunit name> <number of models> <color maximum>

log file from chimera is copied from the replylog after running a series of commands like those in mmaker_template.txt
Yes the whole thing could be done in one step with the Chimera python interface, but I am lazy...

Subunit name is the name it uses in the output file

number of models is the number of structures being compared

color maximum is optional - this sets the maximum value used for setting the colors of the correlation matrix - this is useful if you want several matrices to be on same color scale despite different maximum values.  If this is left blank the maximum for that specific dataset is used.


