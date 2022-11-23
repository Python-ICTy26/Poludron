import hashlib
import os
import pathlib
import re
import stat
import typing as tp
import zlib

from pyvcs.refs import update_ref
from pyvcs.repo import repo_find


def hash_object(data: bytes, fmt: str, write: bool = False) -> str:
    # PUT YOUR CODE HERE
    ...


def resolve_object(obj_name: str, gitdir: pathlib.Path) -> tp.List[str]:
    if not 4 <= len(obj_name) <= 40:
        raise Exception(f"Not a valid object name {obj_name}")
    dir_name = obj_name[:2]
    obj_file = obj_name[2:]
    obj_dir = str(gitdir) + "/objects/" + dir_name
    files_list = os.listdir(obj_dir)
    objs = []
    for obj in files_list:
        if obj[: len(obj_file)] == obj_file:
            objs.append(dir_name + obj)

    if not objs:
        raise Exception(f"Not a valid object name {obj_name}")

    return objs


def find_object(obj_name: str, gitdir: pathlib.Path) -> str:
    dir_name = obj_name[:2]
    file_name = obj_name[2:]
    path = str(gitdir) + os.sep + dir_name + os.sep + file_name
    return path


def read_object(sha: str, gitdir: pathlib.Path) -> tp.Tuple[str, bytes]:
    path = gitdir / "objects" / sha[:2] / sha[2:]
    with open(path, "rb") as f:
        data = zlib.decompress(f.read())
    return data.split(b" ")[0].decode(), data.split(b"\00", maxsplit=1)[1]


def read_tree(data: bytes) -> tp.List[tp.Tuple[int, str, str]]:
    tree_entries: tp.List[tp.Tuple[int, str, str]] = []
    while len(data):
        sha = bytes.hex(data[-20:])
        data = data[:-21]
        obj_type, _ = read_object(sha, repo_find())
        space_pos = data.rfind(b" ")
        name = data[space_pos + 1:].decode("ascii")
        data = data[:space_pos]
        if obj_type == "tree":
            mode = "40000"
        else:
            mode = data[-6:].decode("ascii")
        mode_len = -1 * len(mode)
        data = data[:mode_len]
        mode_int = int(mode)
        tree_entries.insert(0, (mode_int, sha, name))
    return tree_entries


def cat_file(obj_name: str, pretty: bool = True) -> None:
    # PUT YOUR CODE HERE
    ...


def find_tree_files(tree_sha: str, gitdir: pathlib.Path) -> tp.List[tp.Tuple[str, str]]:
    # PUT YOUR CODE HERE
    ...


def commit_parse(raw: bytes, start: int = 0, dct=None):
    # PUT YOUR CODE HERE
    ...
