import pathlib
import typing as tp


def update_ref(gitdir: pathlib.Path, ref: tp.Union[str, pathlib.Path], new_value: str) -> None:
    with open(pathlib.Path(gitdir / ref), "w") as ref_file:
        ref_file.write(new_value)


def symbolic_ref(gitdir: pathlib.Path, name: str, ref: str) -> None:
    with open(gitdir / name, "w") as ref_file:
        ref_file.write(ref)


def ref_resolve(gitdir: pathlib.Path, refname: str) -> str:
    if refname == "HEAD":
        refname = get_ref(gitdir)
    if is_detached(gitdir):
        return refname
    with open(gitdir / pathlib.Path(refname), "r") as ref:
        data = ref.read()
    return data


def resolve_head(gitdir: pathlib.Path) -> tp.Optional[str]:
    refname = get_ref(gitdir)
    if not (gitdir / pathlib.Path(refname)).exists():
        return None
    with open(gitdir / pathlib.Path(refname), "r") as ref:
        data = ref.read()
    return data


def is_detached(gitdir: pathlib.Path) -> bool:
    # PUT YOUR CODE HERE
    ...


def get_ref(gitdir: pathlib.Path) -> str:
    # PUT YOUR CODE HERE
    ...
