# print("Hello Derick")
#
# ------Append data to file------
# # fa = open("text.txt", "a")
# ------END------

# -----------------ADD NEW USER INTO DATABASE-----------------
# with open("database.txt", "r") as file:
#     data = eval(file.read())
#
#     admin1_data = {'username': 'admin1', 'pin': 'admin1', 'login_attempt': 0, 'available_balance': 70000}
#     admin2_data = {'username': 'admin2', 'pin': 'admin2', 'login_attempt': 0, 'available_balance': 80000}
#     data.append(admin1_data)
#     data.append(admin2_data)
#
# with open("database.txt", "w") as file:
#     file.write(str(data))
# -------------------------------

# -------------------------------ADD CATEGORY TO EVERY USER# -------------------------------
# with open("database.txt", "r") as file:
#     data = eval(file.read())
#
#     for user in data:
#         if user["username"] == "user1" or user["username"] == "user2" or user["username"] == "user3" or user["username"] == "user4" or user["username"] == "user5":
#             user.update({"category": "user"})
#         else:
#             user.update({"category": "admin"})
#
# with open("database.txt", "w") as file:
#     file.write(str(data))

# -------------------------------

# -----------------
# with open("database.txt", "w") as f:
#     f.write("[")
#     f.write("\n{'username': 'user1', 'pin': '1111', 'login_attempt': 0, 'available_balance': 10000},")
#     f.write("\n{'username': 'user2', 'pin': '2222', 'login_attempt': 0, 'available_balance': 20000},")
#     f.write("\n{'username': 'user3', 'pin': '3333', 'login_attempt': 0, 'available_balance': 30000},")
#     f.write("\n{'username': 'user4', 'pin': '4444', 'login_attempt': 0, 'available_balance': 40000},")
#     f.write("\n{'username': 'user5', 'pin': '5555', 'login_attempt': 0, 'available_balance': 50000}")
#     f.write("\n]")
# ---------------------

# f = open("fi1.txt", "r")
# print(f.read())

# ------Overwrite any existing Content------
# f.write("Overwrite all")
# f.close()
# ------END------

# ------Open and Read------
# g = open("text.txt", "r")
# print(g.read())
# ------END------

import os

# ------Create Folder------
# newpath = "dddd"
# create folder
# if not os.path.exists(newpath):
#     os.makedirs(newpath)
# ------END------

# ------Remove Existing File------
# if os.path.exists("fi1.txt"):
#     os.remove("fi1.txt")
# else:
#     print("file does not exist")
# ------END------

# ------Remove Folder------
# Remove Folder
# if os.path.exists(newpath):
#     os.rmdir(newpath)
# else:
#     print(f'folder named "{newpath}" does not exist')
# ------END------

# ------creating  folder with a file------
# # Define folder path
# folder_name = "folder1"
#
# # define file path
# file_name = "file1.text"
#
# # create the folder
# os.makedirs(folder_name, exist_ok=True)
#
# # Specify the file path within the folder
# file_path = os.path.join(folder_name, file_name)
#
# # Create and write to the file
# with open(file_path, 'w') as file:
#     file.write("Content added and update for the file")
#
# print(f"Folder {folder_name} and file {file_name} created" )

# ---------END---------