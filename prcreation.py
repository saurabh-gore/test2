import os
import shutil
import git 
import requests , json

GITHUB_BUILD_SCRIPT_BASE_OWNER = "Saurabh057"
GITHUB_BUILD_SCRIPT_BASE_REPO = "test"
HOME = os.getcwd()

g = git.cmd.Git(HOME)


package_data = {}
branch="master"

def getdata():
    package_data["package_name"] = input("Enter Package Name")
    package_data["package_version"] = input("Enter Package Version")
    package_data["package_url"] = input("Enter Package URL")
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
    print(g.commit('-m',"Added Build script for "+package_data["package_name"]))
    print(g.push('origin',package_data["package_name"]))
    # print(g.remote())
    
def create_pull_request(title, description, head_branch, base_branch, git_token):
    git_pulls_api = "https://github.com/api/v3/repos/{0}/{1}/pulls".format(
        GITHUB_BUILD_SCRIPT_BASE_OWNER,
        GITHUB_BUILD_SCRIPT_BASE_REPO)

    # headers = {
    #     "Authorization": "token {0}".format(git_token),
    #     "Content-Type": "application/json"}

    payload = {
        "title": title,
        "body": description,
        "head": head_branch,
        "base": base_branch,
    }

    r = requests.post(
        git_pulls_api,
        data=json.dumps(payload))

    if not r.ok:
        print("Request Failed: {0}".format(r.text))


if __name__=="__main__":
    username="Saurabh057"
    print("Pulling Remote Master")
    g.checkout('master')
    print(g.pull('origin','master'))
    getdata()
    print("Creating New Git Branch")
    print(g.checkout('-b',package_data["package_name"]))
    create_folders()
    git_cmds()
    create_pull_request(
        "Added Build script for"+package_data["package_name"], # title
        "Package Name :"+ package_data["package_name"]+"\n" "Package Version :"+ package_data["package_version"]+"\n"  "Package URL :"+ package_data["package_url"]+"\n", # description
        username+":"+package_data["package_name"], # head_branch
        "master", # base_branch
    )
