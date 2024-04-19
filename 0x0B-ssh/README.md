This is a readme fiel for 0x0B-ssh
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
Tasks
0. Use a private key
mandatory
Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements:

Only use ssh single-character flags
You cannot use -l
You do not need to handle the case of a private key protected by a passphrase
1. Create an SSH key pair
mandatory
Write a Bash script that creates an RSA key pair.

Requirements:

Name of the created private key must be school
Number of bits in the created key to be created 4096
The created key must be protected by the passphrase betty
