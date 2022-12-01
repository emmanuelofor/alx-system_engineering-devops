su betty- Create a script that switches the current user to the user betty
whoami - Write a script that prints the effective username of the current user
groups - Write a script that prints all the groups the current user is part of
chown betty hello- Write a script that changes the owner of the file hello to the user betty
touch hello -Write a script that creates an empty file called hello
chmod u+x hello- Write a script that adds execute permission to the owner of the file hello
chmod +114 hello - Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello
chmod +111 hello - Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello
chmod 007 hello - Write a script that sets the permission to the file hello as follows: Owner: no permission at all; Group: no permission at all; Other users: all the permissions
chmod 753 hello - Write a script that sets the mode of the file hello to this: The file hello will be in the working directory; You are not allowed to use commas for this script
chmod --reference=olleh hello - Write a script that sets the mode of the file hello the same as olleh’s mode.
chmod -R ugo+X * - Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
mkdir my_dir -m=751- Create a script that creates a directory called my_dir with permissions 751 in the working directory.
chgrp school hello- Write a script that changes the group owner to school for the file hello
chown vincent:staff * - Write a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
chown -h vincent:staff _hello- Write a script that changes the owner and the group owner of _hello to vincent and staff respectively.
chown --from=guillaume betty hello- Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
telnet towel.blinkenlights.nl- Write a script that will play the StarWars IV episode in the terminal
