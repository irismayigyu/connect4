from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)


@task
def test(ctx):
    ctx.run("PYTHONPATH=src pytest", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)


@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src/tests", pty=True)
    ctx.run("coverage html", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)


@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)
