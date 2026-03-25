from __future__ import annotations

from decimal import Decimal
from enum import Enum
from fnmatch import fnmatch
from json import JSONEncoder
from typing import Literal

import numpy as np
import pandas as pd


class CustomJSONEncoder(JSONEncoder):
    # Number of significant figures
    float_num_sig_fig: int | None = 3
    on_error: Literal[
        "raise",
        "object",
        "class",
    ] = "raise"

    @classmethod
    def make_serializable(cls, o):
        """
        Prepare object for serialization
        """
        if isinstance(o, float):
            # Since decimal is not serializable, this will trigger default
            return Decimal(o)
        if isinstance(o, dict):
            return {k: cls.make_serializable(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return type(o)(map(cls.make_serializable, o))
        if isinstance(o, np.ndarray):
            return cls.make_serializable(o.tolist())
        if isinstance(o, pd.Series):
            return cls.make_serializable(o.to_numpy())
        if isinstance(o, pd.DataFrame):
            return cls.make_serializable(o.to_dict())
        if hasattr(o, "__swig_destroy__"):
            # If SWIG object
            if hasattr(o, "__getitem__") and hasattr(o, "__len__"):
                # If STL container
                if hasattr(o, "__setitem__"):
                    # If mutable
                    if hasattr(o, "keys") and hasattr(o, "values"):
                        return cls.make_serializable(dict(o))
                    else:
                        return cls.make_serializable(list(o))
                else:
                    # If immutable
                    return cls.make_serializable(tuple(o))
            else:
                # If wrapped class
                o_as_dict = {}
                for attr in dir(o):
                    o_attr = getattr(o, attr)
                    if callable(o_attr):
                        continue
                    if attr in ["this", "thisown"] or fnmatch(attr, "_*_"):
                        continue
                    o_as_dict[attr] = cls.make_serializable(o_attr)
                return o_as_dict
        return o

    def default(self, o):
        if isinstance(o, Decimal):
            if self.float_num_sig_fig is not None:
                return float(f"{o:.{self.float_num_sig_fig}g}")
            return float(o)
        if isinstance(o, Enum):
            return o.value
        # Not serializable
        if self.on_error == "raise":
            return super().default(o)
        elif self.on_error == "object":
            return str(o)
        elif self.on_error == "class":
            return str(o.__class__)
        raise ValueError(f"Invalid on error behavior {self.on_error}")

    def encode(self, o):
        return super().encode(self.make_serializable(o))

    def iterencode(self, o, _one_shot=False):
        return super().iterencode(self.make_serializable(o))
