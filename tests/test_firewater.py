import os
from firewater import view, list, export_to_json


def test_get_specific_artcle(runner):
    """can get a specific article

    """
    response = runner.invoke(view, "new_ah")
    assert 'Success' in response.output


def test_get_list_of_article(runner):
    """Returns correct error when resource is unavailable

    """
    response = runner.invoke(list)
    assert 'Success' in response.output


def test_non_existant_article(runner):
    """correct response for no artucle
    """
    response = runner.invoke(view, "new")
    assert 'Not Found' in response.output


def test_possible_to_export_file(runner):
    """tests that a file can be created
    """

    export_to_json(
        {
            "some": "data about nothing"
        },
        'test_file')
    assert os.path.isfile('test_file.json')
    os.remove('test_file.json')
