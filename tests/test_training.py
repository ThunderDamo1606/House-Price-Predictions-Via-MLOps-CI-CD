import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT_DIR, "src"))

from train import train_model  # noqa: E402


def test_training_runs():
    result = train_model()
    assert result is None
