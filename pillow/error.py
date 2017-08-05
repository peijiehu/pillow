#!/usr/bin/env python
"""Base class for Pillow errors"""

class PillowError(Exception):
    """Base class for Pillow errors"""

    @property
    def message(self):
        """
        :return: The first argument used to construct this error.
        """
        return self.args[0]
