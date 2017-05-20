import click
import click_log

from .funk import Funk


@click.group()
@click_log.simple_verbosity_option()
@click_log.init(__name__)
@click.option('--url', help="Sitemap.xml URL")
@click.option('--concurrent', '-c', default=False, help="Enable concurrency")
@click.option('--verify-ssl', default=True, help='Enable SSL verification')
@click.option('--force-https', default=False, help='Force https')
@click.pass_context
def cli(ctx, url, concurrent, verify_ssl, force_https):
    if ctx.obj is None:
        ctx.obj = {}
    ctx.obj['URL'] = url
    ctx.obj['CONCURRENT'] = concurrent
    ctx.obj['VERIFY_SSL'] = verify_ssl
    ctx.obj['FORCE_HTTPS'] = force_https


@cli.command()
@click.pass_context
def run(ctx):
    """"""
    Funk(ctx.obj['URL']).run(
        concurrent=ctx.obj['CONCURRENT'],
        verify_ssl=ctx.obj['VERIFY_SSL'],
        force_https=ctx.obj['FORCE_HTTPS']
    )


@cli.command()
@click.pass_context
def dryrun(ctx):
    """Creates the schema if it doesn't exist and copies """
    Funk(ctx.obj['URL']).dry_run()
