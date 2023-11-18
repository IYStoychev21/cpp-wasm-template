import sys
import yaml
import glob
import subprocess

def load(path_to_config):
    with open(path_to_config, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def load_src_files(path_to_src):
    return glob.glob(f"{path_to_src}/**.cpp", recursive = True)

def compile_to_objs(src_files, inter_dir):
    subprocess.run(f"emsdk.bat activate latest", shell=True)
    
    for i in src_files:
        file_name = i.split('\\')[-1][0:-4]
        subprocess.run(f"emcc {i} -c -o {inter_dir}/{file_name}.o", shell=True)

def load_objs(int_path):
    return glob.glob(f"{int_path}/**.o", recursive = True)

def link_to_wasm(objs, output_dir, include_dir, lib_dir, libs):
    obj = " ".join(objs)
    include = " ".join(include_dir)
    lib_dirs = " ".join(lib_dir)
    libs = " ".join(libs)
    
    subprocess.run(f"emcc {obj} -I{include} -o {output_dir}/main.js", shell=True)

def clean_up(output_dir): 
    new_dir = output_dir.replace("/", "\\")
    subprocess.run(f"del {new_dir}\\main.js", shell=True)

def main():
    props = load(sys.argv[1])
    src_files = load_src_files(props["SourceDir"])

    compile_to_objs(src_files, props["IntBins"])
    objs = load_objs(props["IntBins"])
    link_to_wasm(objs, props["OutputDir"], props["IncludeDirs"], props.get("LibDir", ""), props.get("Libs", ""))

    clean_up(props["OutputDir"])

if __name__ == '__main__':
    main()
