import argparse

from deal_finder import __version__


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="deal-finder")
    parser.add_argument("--version", action="version", version=f"deal-finder {__version__}")
    parser.parse_args(argv)
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
