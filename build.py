import sys
import yaml
import glob
import subprocess

def load(path_to_config):
    print("-------------- LOADING CONFIG FILE --------------")

    with open(path_to_config, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def load_src_files(path_to_src):
    print("-------------- LOADING SRC FILES --------------")

    return glob.glob(f"{path_to_src}/**.cpp", recursive = True)

def compile_to_objs(src_files, include_dir, inter_dir):
    print("-------------- COMPILING SRC FILES --------------")

    subprocess.run(f"emsdk.bat activate latest", shell=True)
    
    for i in src_files:
        file_name = i.split('\\')[-1][0:-4]
        include = " -I".join(include_dir)
        subprocess.run(f"emcc -I{include} {i} -c -o {inter_dir}/{file_name}.o", shell=True)

def load_objs(int_path):
    print("-------------- LOADING OBJ FILES --------------")

    return glob.glob(f"{int_path}/**.o", recursive = True)

def link_to_wasm(objs, output_dir, name, mode):
    print("-------------- LINKING OBJ FILES --------------")

    obj = " ".join(objs)

    if mode == "Release":
        subprocess.run(f"emcc -O3 {obj} -o {output_dir}/{name}.wasm --no-entry -s WASM=1", shell=True)
    else:
        subprocess.run(f"emcc -O1 {obj} -o {output_dir}/{name}.wasm --no-entry -s WASM=1", shell=True)

def main():
    props = load(sys.argv[1])
    src_files = load_src_files(props["SourceDir"])

    compile_to_objs(src_files, props["IncludeDirs"], props["IntBins"])
    objs = load_objs(props["IntBins"])
    link_to_wasm(objs, props["OutputDir"], props["OutputFileName"], props["BuildMode"])

if __name__ == '__main__':
    main()
