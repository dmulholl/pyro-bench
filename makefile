all:
	@pyro --version
	@python --version
	@echo
	@hyperfine --warmup 3 'pyro bench.pyro' 'python3 bench.py'

pyro:
	@pyro --version
	@echo
	@hyperfine --warmup 3 'pyro bench.pyro'

python:
	@python --version
	@echo
	@hyperfine --warmup 3 'python3 bench.py'
