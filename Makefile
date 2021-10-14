
RUNNER_FILE=huffman.py
TEST_FILES=test_huffman.py
ALL_FILES=$(RUNNER_FILE) $(TEST_FILES)

fmt:
	isort $(ALL_FILES)
	black $(ALL_FILES)

test:
	pytest $(TEST_FILES)
