import argparse
from pathlib import Path
from typing import Optional, List

from dcm2bids.utils import DEFAULT

_SUPPORTED_ARGS = {
    ('-d', '--dicom_dir'): {
        'type': Path,
        'required': True,
        'nargs': '*',
        'help': 'DICOM directory(ies).'
    },
    ("-p", "--participant"): {
        'type': str,
        'required': True,
        'nargs': '*',
        'help': 'Participant ID.'
    },
    ("-s", "--session"): {
        'type': str,
        'required': False,
        'default': '',
        'help': "Session ID."
    },
    ("-c", "--config"): {
        'type': Path,
        'required': True,
        'help': "JSON configuration file (see example/config.json)."
    },
    ("-o", "--output_dir"): {
        'type': Path,
        'required': False,
        'default': Path.cwd(),
        'help': "Output BIDS directory. (Default: %(default)s)"
    },
    ("-fd", "--forceDcm2niix"): {
        'action': 'store_true',
        'help': "Overwrite previous temporary dcm2niix "
                "output if it exists."
    },
    ("-cl", "--clobber"): {
        'action': 'store_true',
        'help': "Overwrite output if it exists."
    },
    ("-l", "--log_level"): {
        'required': False,
        'default': DEFAULT.cliLogLevel,
        'choices': ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        'help': "Set logging level. [%(default)s]"
    },
    ("-f", "--force"): {
        "dest": 'override',
        'action': 'store_true',
        'help': 'Force command to overwrite existing output files. Only for dcm2bidshelper'
    }
}


def _IsSupportedArg(key: str):
    """Check if given key is supported."""
    return any([key in flag_tuple for flag_tuple in _SUPPORTED_ARGS])


def _build_arg_parser(key_filter: Optional[List[str]] = None):
    p = argparse.ArgumentParser(description=__doc__, epilog=DEFAULT.EPILOG,
                                formatter_class=argparse.RawTextHelpFormatter)

    for flag_tuple, kwargs in _SUPPORTED_ARGS:
        if (key_filter is not None and
                (flag_tuple[0] not in key_filter or flag_tuple[1] not in key_filter)):
            continue
        p.add_argument(*flag_tuple, **kwargs)

    return p
