import urllib.request
import os
import subprocess
import fileinput

# Get name user 
current_username = os.getlogin()

path = f"C:\\Users\\{current_username}\\Desktop\\SERVER_MINECRAFT"
path_configuration = path + "\\"
path_bat = path_configuration + "start.bat"
file_path = path_configuration + "eula.txt"

print("""\n
---------------------------------------------------------
|    Creating the 'SERVER_MINECRAFT' folder on Desktop  |
---------------------------------------------------------
    \n
    """)

if os.path.exists(path):
    os.mkdir(path + "38633896339")
else:
    os.mkdir(path)

print("""\n
----------------------------------------------------------
|    minecraft_server.1.19.3.jar file downloads online   |
----------------------------------------------------------
    \n
    """)

url = "https://piston-data.mojang.com/v1/objects/c9df48efed58511cdd0213c56b9013a7b5c9ac1f/server.jar"

file_name = "server.jar"

if os.path.exists(path_configuration + file_name):
    # Remove file_name in path_configuration
    os.remove(path_configuration + file_name)
    # Download file server.jar in url and add server.jar in folder SERVER_MINECRAFT
    urllib.request.urlretrieve(url, path_configuration + file_name)
else:
    # Download file server.jar in url and add server.jar in folder SERVER_MINECRAFT
    urllib.request.urlretrieve(url, path_configuration + file_name)

print("""\n
-----------------------------------------------
|       Creation of the start.bat file        |
-----------------------------------------------
    \n
""")

text = f"java -Xmx1024M -Xms1024M -jar {path_configuration}server.jar nogui"

# Create file start.bat and add text in file start.bat
with open(path_bat, "w") as file:
    file.write(text)
    file.close()

print("""\n
----------------------------------------------------
|           Executing the start.bat file           |
----------------------------------------------------
        \n
        """)


# Executing the start.bat file
subprocess.run(path_bat, cwd=str(path_configuration))

print("""\n\n
-------------------------------------------------
|           Editing the eula.txt file           |
-------------------------------------------------
    \n\n
    """)

# Replace eula=false to eula=true in eula.txt
for line in fileinput.input(file_path, inplace=True):
    print(line.replace("false", "true"), end='')

print(f"""\n\n

   Your server has been created to run it launch the start.bat file in the directory {path_bat}        

    \n
""")
