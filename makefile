PYTHON = python3
.PHONY = run clean
.DEFAULT_GOAL = run

run:
	@${PYTHON} rps_run.py

clean:
	@rm -rf __pycache__



