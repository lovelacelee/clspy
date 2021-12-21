# -*- encoding: utf-8 -*-

import os
import pytest

if __name__ == '__main__':
    """
    How to run pytest cases:
        cd ..
        python pytest
    """
    pytest.main([
        os.path.join(os.path.dirname(__file__), 'test_clspy.py'),
        #"-q",
        "-v",
        "--capture=sys",
        "--html=pytest/test-report.html",
        "--self-contained-html"
    ])