all:
	hyperfine --warmup 3 'pyro bench.pyro' 'python3 bench.py'

pyro:
	hyperfine --warmup 3 'pyro bench.pyro'

python:
	hyperfine --warmup 3 'python3 bench.py'
