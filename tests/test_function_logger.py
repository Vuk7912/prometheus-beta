import logging
import pytest
import time
from io import StringIO
from src.function_logger import log_execution

class TestFunctionLogger:
    def setup_method(self):
        # Create a string buffer to capture log output
        self.log_capture = StringIO()
        self.log_handler = logging.StreamHandler(self.log_capture)
        self.logger = logging.getLogger()
        self.logger.addHandler(self.log_handler)
        self.logger.setLevel(logging.INFO)

    def teardown_method(self):
        # Remove the handler after each test
        self.logger.removeHandler(self.log_handler)
        self.log_capture.close()

    def test_basic_logging(self):
        @log_execution()
        def sample_function():
            return "Success"

        result = sample_function()
        log_output = self.log_capture.getvalue()

        assert result == "Success"
        assert "Starting execution of sample_function" in log_output
        assert "Finished execution of sample_function" in log_output

    def test_function_with_args(self):
        @log_execution()
        def sample_function(a, b):
            return a + b

        result = sample_function(3, 4)
        log_output = self.log_capture.getvalue()

        assert result == 7
        assert "Starting execution of sample_function" in log_output
        assert "Finished execution of sample_function" in log_output

    def test_function_with_exception(self):
        @log_execution()
        def sample_function():
            raise ValueError("Test error")

        with pytest.raises(ValueError, match="Test error"):
            sample_function()

        log_output = self.log_capture.getvalue()
        assert "Starting execution of sample_function" in log_output
        assert "Exception in sample_function: Test error" in log_output

    def test_execution_time_logging(self):
        @log_execution()
        def slow_function():
            time.sleep(0.1)
            return "Slow operation"

        result = slow_function()
        log_output = self.log_capture.getvalue()

        assert result == "Slow operation"
        assert "Starting execution of slow_function" in log_output
        assert "Finished execution of slow_function" in log_output
        assert "Execution time:" in log_output

    def test_custom_logger(self):
        custom_logger = logging.getLogger('custom')
        custom_logger.setLevel(logging.INFO)
        custom_handler = logging.StreamHandler(self.log_capture)
        custom_logger.addHandler(custom_handler)

        @log_execution(logger=custom_logger)
        def sample_function():
            return "Custom logger test"

        result = sample_function()
        log_output = self.log_capture.getvalue()

        assert result == "Custom logger test"
        assert "Starting execution of sample_function" in log_output
        assert "Finished execution of sample_function" in log_output