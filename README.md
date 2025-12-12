# Addcmd

`addcmd` creates python command file in an existing project.

This tool is built with [`chef`](https://github.com/kkibria/chef) which uses
[`prj-gen`](https://github.com/kkibria/prj-gen) library to perform generation.

## Install
Recommended way is to install `addcmd` globally and you will
have to install in administrative mode.

### Using uv
```
uv tool -n install git+https://github.com/kkibria/addcmd.git
```

### Using pip
```
pip install addcmd@git+https://github.com/kkibria/addcmd.git
```

Without the administrative privilege, you can install it in a virtual
environment as well.

## Running
It can be executed directly from command line,
```
addcmd <path> <cmdname>
```

You can also run this as a python module,
```
python -m addcmd <path> <cmdname>
```