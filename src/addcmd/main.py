import argparse
import sys
from warnings import warn
from pathlib import Path
from mkcmd.cli import build
from tomlkit import toml_file, nl

def do_main(path, cmdname, **kwargs):
    dst = Path(path)
    cfg = dst.joinpath('pyproject.toml')
    if not cfg.exists():
        raise IOError(f'"{cfg}" does not exist, exiting!')
    
    tomlfile = toml_file.TOMLFile(cfg.absolute())
    config = tomlfile.read()

    prj = config['project']
    cmdpy = dst.joinpath("src", prj["name"], cmdname)

    pyf = cmdpy.parent.joinpath(cmdpy.name + '.py')
    if pyf.exists():
        raise IOError(f'"{pyf.name}" already exists, exiting!')

    build({}, cmdpy, False, False, **kwargs)

    ins = 'scripts' not in prj
    if ins:
        prj['scripts'] = {}

    prj['scripts'][cmdname] = f'{prj["name"]}.{cmdname}:main'
 
    if ins:
        prj['scripts'].add(nl())

    tomlfile.write(config)
    pass

def main():
    params = {"app": "addcmd"}

    parser = argparse.ArgumentParser(
        prog=params["app"],
        description='Creates python command file',
        epilog=f'python -m {params["app"]}')

    parser.add_argument('path')
    parser.add_argument('cmdname')

    args = parser.parse_args()
    params = params | vars(args)

    set_warnigs_hook()
    try:
        do_main(**params)
    except Exception as e:
        print(f'{e.__class__.__name__}:', *e.args)
        return 1
    
    return 0

def set_warnigs_hook():
    import sys
    import warnings
    def on_warn(message, category, filename, lineno, file=None, line=None):
        print(f'Warning: {message}', file=sys.stderr)
    warnings.showwarning = on_warn

if __name__ == '__main__':
    sys.exit(main())
