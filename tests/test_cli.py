import pytest

from deal_finder.__main__ import main


def test_version_flag_prints_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exit_info:
        main(["--version"])

    assert exit_info.value.code == 0
    assert "deal-finder 0.1.0" in capsys.readouterr().out
