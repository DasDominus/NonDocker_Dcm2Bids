# -*- coding: utf-8 -*-

"""helper module"""

import sys

from dcm2bids import common
from dcm2bids.dcm2niix import Dcm2niix
from dcm2bids.utils import DEFAULT, assert_dirs_empty


def BuildDcm2niix(**kwargs):
    parser = common._build_arg_parser(key_filter=['-d', '-o', '-f'])

    arg_vals = []
    for key, val in kwargs:
        if not common._IsSupportedArg(key):
            raise ValueError(f'Unsupported Key {key}')
        arg_vals.extend([key, val])

    ns = parser.parse_args(arg_vals)
    out_folder = ns.output_dir / DEFAULT.tmpDirName / DEFAULT.helperDir

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
