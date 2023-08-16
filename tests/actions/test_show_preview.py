from pro_filer.actions.main_actions import show_preview  # NOQA
import pytest


long_response = (
    "Found 6 files and 7 directories\n"
    "First 5 files: ['a', 'b', 'c', 'd', 'e']\n"
    "First 5 directories: ['a', 'b', 'c', 'd', 'e']\n"
)
short_response = (
    "Found 0 files and 0 directories\n"
)


@pytest.mark.parametrize(
    'context, response',
    [
      (
          {
            'all_files': ['a', 'b', 'c', 'd', 'e', 'f'],
            'all_dirs': ['a', 'b', 'c', 'd', 'e', 'f', 'g']
          },
          long_response
      ),
      (
          {
            'all_files': [],
            'all_dirs': []
          },
          short_response
      )
    ]
  )
def test_show_preview(capsys, context, response):
    show_preview(context)
    captured = capsys.readouterr()
    assert response == captured.out
