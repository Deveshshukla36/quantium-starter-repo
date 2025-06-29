#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run test suite
pytest

# Capture exit code
if [ $? -eq 0 ]; then
  echo "✅ All tests passed."
  exit 0
else
  echo "❌ Tests failed."
  exit 1
fi
