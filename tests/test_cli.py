from cachefunk.cli import cli


def test_simple_spec(cli_runner):
    """Initial test to make sure args at least not breaking app"""
    assert cli_runner.invoke(cli)
