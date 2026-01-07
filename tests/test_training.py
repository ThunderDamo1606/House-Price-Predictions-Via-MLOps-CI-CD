import os
import sys
from train import train_model   # noqa: E402

sys.path.append(os.path.abspath("src"))


def test_training_runs():
    result = train_model()
    assert result is None
