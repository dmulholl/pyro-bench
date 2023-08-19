all:
	@pyro --version
	@echo
	@hyperfine --warmup 3 'pyro bench.pyro'

.PHONY: compare
compare:
	@pyro --version
	@echo
	@hyperfine --warmup 3 'pyro compare/bench.pyro'
	@python --version
	@echo
	@hyperfine --warmup 3 'python3 compare/bench.py'
