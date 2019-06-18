
from firewater import view, get_resource_url


def test_get_specific_artcle(runner):
    """can get a specific article

    """
    response = runner.invoke(view)
    assert 'Success' in response.output


def test_get_non_existent_article(runner):
    """Returns correct error when resource is unavailable

    """
    response = runner.invoke(view, "--slug clesome")
    assert 'Not Found' in response.output

