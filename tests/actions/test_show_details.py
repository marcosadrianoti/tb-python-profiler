from pro_filer.actions.main_actions import show_details  # NOQA
import os
from datetime import datetime
from unittest.mock import Mock, patch


def test_show_details_file_not_found(capsys):
    mock_not_found = Mock(return_value=False)
    file_path = {"base_path": "/a/b/c.txt"}
    with patch("os.path.exists", mock_not_found):
        show_details(file_path)
        captured = capsys.readouterr()
        assert captured.out == "File 'c.txt' does not exist\n"


def test_show_details_file_without_extension(capsys, tmp_path):
    content = 'Trybe\n'
    output_path = tmp_path / "out_file"
    output_path.write_text(content)
    context = {"base_path": str(output_path)}
    show_details(context)
    captured = capsys.readouterr()
    assert "File extension: [no extension]" in captured.out


def test_show_details_file_date(capsys, tmp_path):
    content = 'Trybe\n'
    output_path = tmp_path / "out_file.txt"
    output_path.write_text(content)
    modification_time = os.path.getmtime(str(output_path))
    modification_time_dt = datetime.fromtimestamp(modification_time)
    modification_date = modification_time_dt.date()
    context = {"base_path": str(output_path)}
    show_details(context)
    captured = capsys.readouterr()
    assert f"Last modified date: {modification_date}\n" in captured.out
