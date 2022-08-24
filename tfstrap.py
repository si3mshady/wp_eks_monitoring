import os, sys, subprocess

BOOTSTRAP_FILES = "main.tf outputs.tf providers.tf variables.tf"

def execute_cmd(cmd):
    subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()

def gen_cmd_string(module,filename):
    return  f"touch {get_current_directoy()}/{module}/{filename}"


def create_subdirectory_structure(module_name):

    c = f'mkdir {get_current_directoy()}/{module_name}'
    execute_cmd(c)
    [execute_cmd(c) for c in  [gen_cmd_string(module_name,file) for file in  BOOTSTRAP_FILES.split() if file != 'providers.tf']]
    

def create_root_structure():
    execute_cmd('touch ' + BOOTSTRAP_FILES) 


def get_current_directoy():
    return os.path.dirname(__file__)

if __name__ == "__main__":
    modules = sys.argv[1:]
    create_root_structure()

    for mod in modules:
        create_subdirectory_structure(mod)

#Elliott Arnold  Terraform bootstrapper - for modular tf deployments 
#bootstrap tf module file structure using command line args 
#usage = python3 tf_boilerplate.py  cicd s3
#7-29-22
