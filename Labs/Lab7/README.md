I decided to go with carbon. Carbon module adds more automated system admin processes. When normally installing powershell this does not happen, with this way of doing it we wont have to worry about latter changing these settings.

Below are the steps on how to install Carbon using PS:

Install-Module -Name 'Carbon' -AllowClobber Import-Module 'Carbon'
Processes: Here is how to get the permissions of a file, directory, etc. to a specified path. (To test this command yourself, replace the file path with whatever you would like, as I put in my own sample info.)

Get-Permission -Path 'C:\it3038c-scripts\Lab7\file.txt'
Here is how to create a directory. Make sure that this directory does not exist already or it will error out, if it does simply use another name.
It also will create parent directories that didnt exist before running the command. For example in this case "it3038c-scripts\Lab7\".

Install-Directory -Path 'C:\it3038c-scripts\Lab7\NewDirectory'

This is how to get the IPv4 address of the local machine the command is being run on.

Get-IPAddress -V4
