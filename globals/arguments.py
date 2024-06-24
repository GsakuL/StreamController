from typing import Protocol, Sequence, Any, NamedTuple
import argparse


class _PageChangeArg(NamedTuple):
    serial_number: str
    page_name: str


class _DeckArguments(Protocol):
    b: bool
    devel: bool
    skip_load_hardware_decks: bool
    close_running: bool
    data: str | None
    locale: str | None
    change_page : Sequence[_PageChangeArg] | None
    app_args: Any


argparser = argparse.ArgumentParser()
argparser.add_argument("-b", help="Open in background", action="store_true")
argparser.add_argument("--devel", help="Developer mode (disables auto update)", action="store_true")
argparser.add_argument("--skip-load-hardware-decks", help="Skips initilization/use of hardware decks", action="store_true")
argparser.add_argument("--close-running", help="Close running", action="store_true")
argparser.add_argument("--data", help="Data path", type=str)
argparser.add_argument("--locale", help="override locale/language (for debugging or neutral screenshots)", type=str)
argparser.add_argument("--change-page", action="append", nargs=2, help="Change the page for a device", metavar=("SERIAL_NUMBER", "PAGE_NAME"))
argparser.add_argument("app_args", nargs="*")

args: _DeckArguments = argparser.parse_args()

if args.change_page:
    args.change_page = [_PageChangeArg(*nargs) for nargs in args.change_page]
