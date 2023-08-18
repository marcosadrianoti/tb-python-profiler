from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


@pytest.fixture
def context(tmp_path):
    temp_file_one = tmp_path / "temp_file1.txt"
    temp_file_one.write_text("123")

    temp_file_two = tmp_path / "temp_file2.txt"
    temp_file_two.write_text("123")

    temp_file_three = tmp_path / "temp_file3.txt"
    temp_file_three.write_text("123123")

    return {
        "all_files": [
            str(temp_file_one),
            str(temp_file_two),
            str(temp_file_three),
        ]
    }


def test_find_duplicates(context):
    duplicates = find_duplicate_files(context)
    assert len(duplicates) == 1
    assert "temp_file1.txt" in duplicates[0][0]
    assert "temp_file2.txt" in duplicates[0][1]


def test_non_existent_file(context):
    all_files = context["all_files"]
    all_files.append("test.txt")
    assert all_files[3] == "test.txt"

    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)
