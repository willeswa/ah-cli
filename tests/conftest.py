import pytest
from click.testing import CliRunner


@pytest.fixture(scope='module')
def runner():
    cli_runner = CliRunner()
    yield cli_runner
