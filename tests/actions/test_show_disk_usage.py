from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from unittest.mock import patch
import pytest

GET_SIZE = "pro_filer.actions.main_actions.os.path.getsize"


@pytest.fixture
def context(tmp_path):
    temp_file_one = tmp_path / "temp_file1.txt"
    temp_file_one.write_text("123")

    temp_file_two = tmp_path / "temp_file2.txt"
    temp_file_two.write_text("123123")

    temp_file_three = tmp_path / "temp_file3.txt"
    temp_file_three.write_text("123123123")

    return {
        "all_files": [
            str(temp_file_one),
            str(temp_file_two),
            str(temp_file_three)
        ]
    }


def test_show_disk_usage(context, capsys):
    with patch(
        GET_SIZE, return_value=10
    ):
        show_disk_usage(context)
        captured = capsys.readouterr()
        out_disk_usage = captured.out

        assert "temp_file1.txt':        10 (33%)" in out_disk_usage
        assert "temp_file2.txt':        10 (33%)" in out_disk_usage
        assert "temp_file3.txt':        10 (33%)" in out_disk_usage
        assert "Total size: 30" in out_disk_usage
