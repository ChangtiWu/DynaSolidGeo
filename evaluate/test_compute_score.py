import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from evalute_util import compute_score

def run_tests():
    """运行所有测试案例"""
    # 测试案例集合
    test_cases = [
        # 基本数值匹配测试
        {
            "name": "精确数值匹配",
            "model_output": "42",
            "ground_truth": "42",
            "expected_score": 1.0,
            "description": "测试完全相同的数值"
        },
        {
            "name": "不同数值",
            "model_output": "42",
            "ground_truth": "43",
            "expected_score": 0.0,
            "description": "测试不同的数值"
        },
        
        # 数学表达式测试
        {
            "name": "等价数学表达式",
            "model_output": "2+3",
            "ground_truth": "5",
            "expected_score": 1.0,
            "description": "测试数学上等价的表达式"
        },
        {
            "name": "分数表达式",
            "model_output": "1/2",
            "ground_truth": "0.5",
            "expected_score": 1.0,
            "description": "测试分数与小数的等价性"
        },
        {
            "name": "复杂分数",
            "model_output": "3/4",
            "ground_truth": "0.75",
            "expected_score": 1.0,
            "description": "测试复杂分数转换"
        },
        
        # 包含π的表达式测试
        {
            "name": "π表达式",
            "model_output": "$$2*π$$",
            "ground_truth": "2*3.14159",
            "expected_score": 1.0,
            "description": "测试包含π的表达式"
        },
        {
            "name": "π近似值",
            "model_output": "\\boxed{π}",
            "ground_truth": "3.14159",
            "expected_score": 1.0,
            "description": "测试π的近似值匹配"
        },
        
        # 格式化输出测试（带\\box{}）
        {
            "name": "LaTeX格式输出",
            "model_output": "Step 2: The answer is \\boxed{42}",
            "ground_truth": "42",
            "expected_score": 1.0,
            "description": "测试LaTeX格式的答案提取"
        },
        {
            "name": "复杂LaTeX表达式",
            "model_output": "Step 2: After calculation, \\boxed{\\frac{1}{2}}",
            "ground_truth": "0.5",
            "expected_score": 1.0,
            "description": "测试复杂LaTeX分数表达式"
        },
        
        # 相对误差容忍测试
        {
            "name": "相对误差内的近似值",
            "model_output": "3.141",
            "ground_truth": "3.14159",
            "expected_score": 1.0,
            "description": "测试在相对误差范围内的近似值"
        },
        {
            "name": "超出相对误差的值",
            "model_output": "3.0",
            "ground_truth": "3.14159",
            "expected_score": 0.0,
            "description": "测试超出相对误差范围的值"
        },
        
        # 字符串格式测试
        {
            "name": "带空格的数值",
            "model_output": " 42 ",
            "ground_truth": "42",
            "expected_score": 1.0,
            "description": "测试带前后空格的数值"
        },
        {
            "name": "科学计数法",
            "model_output": "1e2",
            "ground_truth": "100",
            "expected_score": 1.0,
            "description": "测试科学计数法表示"
        },
        
        # 负数测试
        {
            "name": "负数匹配",
            "model_output": "-42",
            "ground_truth": "-42",
            "expected_score": 1.0,
            "description": "测试负数的精确匹配"
        },
        {
            "name": "负数表达式",
            "model_output": "-(2+3)",
            "ground_truth": "-5",
            "expected_score": 1.0,
            "description": "测试负数表达式"
        },
        
        # 复杂数学表达式测试
        {
            "name": "平方根表达式",
            "model_output": "$\\sqrt{4}$",
            "ground_truth": "2",
            "expected_score": 1.0,
            "description": "测试平方根表达式"
        },
        {
            "name": "指数表达式",
            "model_output": "2^3",
            "ground_truth": "8",
            "expected_score": 1.0,
            "description": "测试指数表达式"
        },
        
        # 异常情况测试
        {
            "name": "空字符串输入",
            "model_output": "",
            "ground_truth": "42",
            "expected_score": 0.0,
            "description": "测试空字符串输入"
        },
        {
            "name": "无效数学表达式",
            "model_output": "invalid_math",
            "ground_truth": "42",
            "expected_score": 0.0,
            "description": "测试无效的数学表达式"
        },
        {
            "name": "特殊字符",
            "model_output": "42@#$",
            "ground_truth": "42",
            "expected_score": 1.0,
            "description": "测试包含特殊字符的输入"
        },
        
        # 多种格式混合测试
        {
            "name": "混合格式表达式",
            "model_output": "The answer is 2*3 = 6",
            "ground_truth": "6",
            "expected_score": 1.0,
            "description": "测试从文本中提取数学答案"
        },
        {
            "name": "百分数转换",
            "model_output": "50%",
            "ground_truth": "0.5",
            "expected_score": 1.0,
            "description": "测试百分数到小数的转换"
        },
        
        # 边界值测试
        {
            "name": "零值测试",
            "model_output": "0",
            "ground_truth": "0",
            "expected_score": 1.0,
            "description": "测试零值匹配"
        },
        {
            "name": "很大的数值",
            "model_output": "1000000",
            "ground_truth": "1e6",
            "expected_score": 1.0,
            "description": "测试大数值的不同表示形式"
        },
        {
            "name": "很小的数值",
            "model_output": "0.001",
            "ground_truth": "1e-3",
            "expected_score": 1.0,
            "description": "测试小数值的不同表示形式"
        }
    ]
    
    print("开始运行 compute_score 函数测试...")
    print("=" * 60)
    
    passed_tests = 0
    total_tests = len(test_cases)
    
    for i, test_case in enumerate(test_cases, 1):
        try:
            score, extracted = compute_score(test_case["model_output"], test_case["ground_truth"])
            
            # 判断测试是否通过
            test_passed = (score == test_case["expected_score"])
            
            status = "✓ PASS" if test_passed else "✗ FAIL"
            if test_passed:
                passed_tests += 1
            
            print(f"测试 {i:2d}: {test_case['name']}")
            print(f"    描述: {test_case['description']}")
            print(f"    输入: '{test_case['model_output']}' vs '{test_case['ground_truth']}'")
            print(f"    期望得分: {test_case['expected_score']}, 实际得分: {score}")
            print(f"    提取结果: '{extracted}'")
            print(f"    状态: {status}")
            print("-" * 60)
            
        except Exception as e:
            print(f"测试 {i:2d}: {test_case['name']} - ✗ ERROR")
            print(f"    错误: {str(e)}")
            print("-" * 60)
    
    print(f"\n测试总结:")
    print(f"总测试数: {total_tests}")
    print(f"通过测试: {passed_tests}")
    print(f"失败测试: {total_tests - passed_tests}")
    print(f"通过率: {passed_tests/total_tests*100:.1f}%")

if __name__ == "__main__":
    run_tests()
