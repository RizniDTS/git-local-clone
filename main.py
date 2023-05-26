import subprocess
from datetime import date
from env import source_dir, target_base_dir

# Set the source and target directory paths

target_dir = target_base_dir + "/{}/".format(str(date.today()))

commands = []

# Give permission
command = ["chmod", "-R", "777", target_base_dir]
commands.append(command)

# Create directory if not exit
command = ["mkdir", "-p", target_dir]
commands.append(command)

# # Build the command to be executed
command = ["cp", "-r", source_dir, target_dir]
commands.append(command)

# Execute the command
for c in commands:
    subprocess.run(c)
print("done")
