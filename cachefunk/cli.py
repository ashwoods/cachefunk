import click
import click_log

from .funk import Funk


@click.group()
@click_log.simple_verbosity_option()
@click_log.init(__name__)
@click.option('--url', help="Sitemap.xml URL")
@click.option('--concurrent', '-c', default=False, help="Enable concurrency")
@click.option('--timeout', default=30, help="Request timeout")
@click.option('--verify-ssl', default=True, help='Enable SSL verification')
@click.option('--verify-response', default=False, help='Verify the response')
@click.option('--force-https', default=False, help='Force https')
@click.option('--replace', default=None, help="Replace url base")
@click.option('--progress', default=False, help="Show progress")
@click.pass_context
def cli(ctx, **kwargs):
    if ctx.obj is None:
        ctx.obj = {}
    ctx.obj['sitemap_url'] = kwargs.pop('url')
    ctx.obj.update(**kwargs)


@cli.command()
@click.pass_context
def run(ctx):
    """"""
    Funk(**ctx.obj).run()


@cli.command()
@click.pass_context
def dryrun(ctx):
    """Creates the schema if it doesn't exist and copies """
    Funk(ctx.obj['URL']).dry_run()
