from sys import argv
from os.path import isfile, basename, dirname
from os import chdir, mkdir, system, rename, remove
from shutil import rmtree
progs = argv[1:]
for prog in progs:
    dir_ = dirname(prog)
    fname = basename(prog)
    fprog = fname.replace(".cpp", "").replace(".c", "")
    if isfile(prog) and (fname.endswith(".cpp") or fname.endswith(".c")):
        print(f"Компиляция с помощью CMake: {fname}")
        chdir(dir_)
        cmakelists = open("CMakeLists.txt", "w", encoding="UTF-8")
        cmakelists.write(f"""cmake_minimum_required(VERSION 3.5)
project({fprog})
add_executable({fprog} {fname})""")
        cmakelists.close()
        mkdir("build")
        chdir("build")
        system("cmake .. > nul")
        system("cmake --build . > nul")
        chdir("Debug")
        rename(f"./{fprog}.exe", f"{dir_}/{fprog}.exe")
        chdir(dir_)
        rmtree("build")
        remove("CMakeLists.txt")
        print(f"Файл {fname} скомпилирован и сохранён под названием {fprog}.exe")
    else:
        print(f"\"{prog}\" не является файлом C (.c) или C++ (.cpp), либо такого файла не существует.")