# -*- coding: utf-8 -*-

"""helper module"""

import sys
import os

from dcm2bids import common
from dcm2bids.dcm2niix import Dcm2niix
from dcm2bids.utils import DEFAULT, assert_dirs_empty


def BuildDcm2niix(**kwargs):
    parser = common._build_arg_parser(key_filter=['-d', '-o', '-f'])

    arg_vals = []
    for key, val in kwargs.items():
        flg = common.GetSupportedArg(key)
        if not flg:
            raise ValueError(f'Unsupported Flag {key} given')
        arg_vals.extend([flg, val])

    ns = parser.parse_args(arg_vals)
    out_folder = os.path.join(ns.output_dir, DEFAULT.tmpDirName, DEFAULT.helperDir)

    assert_dirs_empty(parser, ns, out_folder)
    print(f"Example in: {out_folder}")

    app = Dcm2niix(dicomDirs=ns.dicom_dir, bidsDir=ns.output_dir)
    return app


def main():
    """Let's go"""
    app = BuildDcm2niix()
    return app.run()


if __name__ == "__main__":
    sys.exit(main())
