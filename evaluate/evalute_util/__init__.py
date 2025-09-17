from .prime_math import compute_score as prime_compute_score
from .math_verify_comp import compute_score as math_verify_compute_score
from .math_rel_comp import compute_score as rel_compute_score

def norm_string(string):
    # replace pi
    string = string.replace("π", "\\pi")
    
    # replace tfrac and dfrac with frac
    string = string.replace("tfrac", "frac")
    string = string.replace("dfrac", "frac")

    # remove \left and \right
    string = string.replace("\\left", "")
    string = string.replace("\\right", "")

    # Remove circ (degrees)
    string = string.replace("^{\\circ}", "")
    string = string.replace("^\\circ", "")
    return string

def compute_score(model_output: str, ground_truth: str) -> bool:
    
    extracted_model_output = model_output
    
    try:
        prime_score, _ , extracted_model_output = prime_compute_score(model_output, ground_truth)[0]
        if prime_score:
            return 1.0, extracted_model_output
    except Exception as e:
        prime_score = 0.0
        
    try:
        math_verify_score, math_verify_extracted_model_output = math_verify_compute_score(norm_string(model_output), ground_truth)
        if math_verify_score:
            return 1.0, math_verify_extracted_model_output
    except Exception as e:
        math_verify_score = 0.0
    try:
        rel_score = rel_compute_score(norm_string(extracted_model_output), ground_truth, rel_tol=0.01)
        if rel_score:
            return 1.0, extracted_model_output
    except Exception as e:
        rel_score = 0.0
    return 0.0, extracted_model_output