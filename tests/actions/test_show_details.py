from pro_filer.actions.main_actions import show_details  # NOQA
import pytest
from unittest.mock import Mock, patch
import os
# from faker import Faker

# fake = Faker()


def test_show_details_file_not_found(capsys):
    mock_not_found = Mock(return_value=False)
    file_path = {"base_path": "/a/b/c.txt"}

    with patch("os.path.exists", mock_not_found):
        show_details(file_path)
        captured = capsys.readouterr()
        assert captured.out == "File 'c.txt' does not exist\n"


# def fake_file_path(extension=''):
#     path = '/' + fake.word() + '/' + fake.word() + '/'
#     file = f"{fake.word()}{extension}"
#     return (path, file)


# @pytest.mark.parametrize(
#     "context",
#     [
#         {"base_path": "/home/marcos/Downloads/pngwing"}
#         # {"base_path": "/home/trybe/Downloads/Trybe_logo"}
#     ],
# )
def test_show_details_file_without_extension(capsys, tmp_path):
    content = 'Trybe\n'
    output_path = tmp_path / "out_file"
    output_path.write_text(content)
    # with open(output_path, "w", encoding="utf-8") as file:
    #     file.write(content)
    # my_tupla = fake_file_path(extension='')
    # mock_file = Mock(return_value=("Trybe_logo", ""))
    # mock_file = Mock(return_value=("out_file", ""))
    # mock_txt = Mock(return_value=(f"{my_tupla[1]}", ""))
    # file_path = {"base_path": "/home/marcos/Downloads/pngwing"}
    # file_path = {"base_path": f"{my_tupla[0]}{my_tupla[1]}"}
    # file_path = context

    # with patch("os.path.splitext", mock_file):
    context = {"base_path": str(output_path)}
    show_details(context)
    captured = capsys.readouterr()
    # assert "File extension: .png" in captured.out
    assert "File extension: [no extension]" in captured.out
