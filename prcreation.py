import os
import shutil
import git 


HOME = os.getcwd()
g = git.cmd.Git(HOME)


package_data = {}


def getdata():
    package_data["package_name"] = input("Enter Package Name")
    # package_data["package_version"] = input("Enter Package Version")
    package_data["distro_name"] = input("Enter Distro Name")
    package_data["distro_version"] = input("Enter Distro Version")


def create_folders():
    package_path=HOME+"/"+ package_data["package_name"][0] + "/"+package_data["package_name"]
    
    if not os.path.exists(package_path):
        os.makedirs(package_path)
    licence_file = "{}/LICENSE".format(package_path)
    if not os.path.exists(licence_file):
        shutil.copyfile(HOME+"/LICENSE", package_path+"/LICENSE")

    filename=package_path+"/"+package_data["package_name"]+"_"+package_data["distro_name"]+"_"+package_data["distro_version"]+".sh"
    
    if not os.path.isfile(filename):
        open(filename, 'w').close()

    print(licence_file)
    print(filename)

def git_cmds():

    print(g.status())
    print(g.add(u=True))
    pass

# getdata()
# create_folders()
git_cmds()
