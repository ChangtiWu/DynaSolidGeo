import re
import json
from typing import Optional
from tqdm import tqdm
import math
from sympy import Expr

try:
    from math_verify import parse 
except ImportError:
    print("To use Math-Verify, please install it first by running `pip install math-verify`.")


def _to_float(expr):
    if isinstance(expr, Expr):
        return float(expr.evalf())
    return float(expr)

def compute_score(pred: str, gt: str, rel_tol: float = 0.01) -> bool:
    
    
    try:
        p_val = float(pred)
        g_val = float(gt)
        return math.isclose(p_val, g_val, rel_tol=rel_tol)
    except (Exception):
        pass
    
    try:
        p_exprs = parse(pred)
        g_exprs = parse(gt)

        p = p_exprs[0] if p_exprs else None
        g = g_exprs[0] if g_exprs else None
        if p is None or g is None:
            return False

        p_val, g_val = _to_float(p), _to_float(g)
        return math.isclose(p_val, g_val, rel_tol=rel_tol)

    except Exception:
        return False
    
    return False

    

