from git import Repo
from directory_tree import DisplayTree
import os

def clone(url):
    folder = url.split("/")[-1].removesuffix(".git")
    Repo.clone_from(url, folder)

    return folder

def Get_Dir_Tree(path):
    dir_tree = DisplayTree(path, header=True,stringRep=True)
    return dir_tree

def Get_File_Table(path):
    file_table = dict()
    current_dir_objects = os.listdir(path=path)

    for i in current_dir_objects:
        if (os.path.isfile(path+i)):
            file_table[i] = path + i
        
        if (os.path.isdir(path + i + "/")):
            if (i[0] == (".")):
                continue
            temp_table = Get_File_Table(path=(path+i+"/"))
            file_table.update(temp_table)
    
    return file_table

def Get_File_Content(path):
    try :
        with open(path,"r+",encoding="utf-8") as f:
            content = f.read()
            return content
    except:
        return ""

def Create_Query(path):
    query = Get_Dir_Tree(path=path)

    table = Get_File_Table(path=path)

    for file,loc in table.items():
        content = Get_File_Content(loc)
        if content != "":
            query += f"contents of file {file} are:\n"
            query += content + "\n"

    query += "Create A professional readme for this project by carefully analyzing the code files. the output should be fully formated in .md , i should able to just copy and paste in a .md file and be done with, dont give any additional responses , just the readme"

    return query

