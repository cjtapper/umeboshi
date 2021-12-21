#!/usr/bin/env python
import os
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    os.environ["CUSTOM_COMPILE_COMMAND"] = "requirements/compile.py"
    os.environ.pop("PIP_REQUIRE_VIRTUALENV", None)
    common_args = [
        "-m",
        "piptools",
        "compile",
        "--generate-hashes",
        "--allow-unsafe",
    ] + sys.argv[1:]
    subprocess.run(
        [
            "python3.6",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-o",
            "py36-django30.txt",
        ],
        check=True,
    )
