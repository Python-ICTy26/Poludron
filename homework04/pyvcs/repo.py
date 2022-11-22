import os
import pathlib
import typing as tp


def repo_find(workdir: tp.Union[str, pathlib.Path] = ".") -> pathlib.Path:
    gitdir = os.getenv("GIT_DIR", ".pyvcs")
    workdir = pathlib.Path(workdir)
    while pathlib.Path("/") != workdir.absolute():
        if (workdir / gitdir).is_dir():
            return workdir / gitdir
        workdir = workdir.parent
    if (workdir / gitdir).is_dir():
        return workdir / gitdir
    else:
        raise Exception("Not a git repository")


def repo_create(workdir: tp.Union[str, pathlib.Path]) -> pathlib.Path:
    # PUT YOUR CODE HERE
    ...
