# DynaSolidGeo

<p align="center">
<a href=""><img src="assets/dynasolidgeo-logo.png" alt="logo" width="150px"></a>
</p>

DynaSolidGeo: A Dynamic Benchmark for Genuine Spatial Mathematical Reasoning of VLMs in Solid Geometry

## How to use

### Environment

Generating question instances requires invoking MATLAB to generate images or videos (via the `matlabengine` library in Python). The version of MATLAB used in the paper is MATLAB R2025a (Windows). The version of the `matlabengine` must be compatible with the MATLAB version (refer to https://pypi.org/project/matlabengine/25.1.1/).

To install all dependencies for this project, please ensure that you have `Python ≥ 3.10`.
And then, run:

```bash
pip install -r requirements.txt
```

**Note.** We recommend generating the question instances on a Windows system, with the remaining steps completed on a Linux system. (This is because Windows offers better compatibility with MATLAB, while the `math-verify` tool required for our evaluation need to run on Linux.)

### Generate the question instances

Firstly, run the `utils/json_gen.py` to generate the json of the random-sampled question instances by providing `mode` and `seed`, which is saved to the `data/problem.jsonl`:

```cmd
python utils/json_gen.py --mode=0 --seed=0
```

- mode: 0 means generating images; 1 means generating videos. (default value is 0)
- seed: random seed to sample the question instances. (default value is 0)

Secondly, run the `utils/visual_gen.py` to generate the images/videos of the random-sampled question instances, which is saved to the file `data/images`/`data/videos`:

```cmd
python utils/visual_gen.py
```


### Generate the solutions


Use your VLM to generate the solutions, the generated solution is added to the `data/problem.jsonl` as a new item `response`.

#### For API-based VLM Services

If you want to use API services or vLLM API-style inference, you need to configure environment variables for API access.

<details>
<summary>🔧 Environment Variables Configuration</summary>


##### Required Environment Variables

- `API_KEY`: Your API key for accessing the VLM service
- `BASE_URL` (Optional): Custom API base URL (defaults to `https://api.openai.com/v1`)
- `MODEL_NAME` (Optional): Model name to use (defaults to `gpt-4o`)

##### Setting Environment Variables

**On Windows (PowerShell):**
```powershell
$env:API_KEY="your_api_key_here"
$env:BASE_URL="https://api.openai.com/v1"  # Optional
$env:MODEL_NAME="gpt-4o"  # Optional
```

**On Windows (Command Prompt):**
```cmd
set API_KEY=your_api_key_here
set BASE_URL=https://api.openai.com/v1
set MODEL_NAME=gpt-4o
```

**On Linux/macOS:**
```bash
export API_KEY="your_api_key_here"
export BASE_URL="https://api.openai.com/v1"  # Optional
export MODEL_NAME="gpt-4o"  # Optional
```

</details>

Here we provide our own code `evaluate/gen_response.py` which generates solutions for VLMs using API services with **asynchronous processing** and **smart resume functionality**. 


##### Usage with Custom Parameters
```cmd
# Custom output file and model
python evaluate/gen_response.py \
    --input_file data/seed_0/problem.jsonl \
    --output_file results/my_responses.jsonl \
    --model_name gpt-4o-mini

# Increase concurrent requests for faster processing
python evaluate/gen_response.py \
    --input_file data/seed_0/problem.jsonl \
    --max_concurrent 10
```

#### Command Line Arguments

- `--input_file`: Path to the input JSONL file containing questions
- `--output_file`: Path to the output JSONL file (default: `{input_dir}/response.jsonl`)
- `--model_name`: Model name to use (default: from `MODEL_NAME` environment variable)
- `--max_concurrent`: Maximum concurrent requests (default: 5)

#### Output Format

The script generates a JSONL file where each line contains:
```json
{
    "id": "question_unique_id",
    "response": "model_generated_answer",
    "solution": "ground_truth_solution"
}
```

#### Resume Functionality

- **Automatic Resume**: If you interrupt the process, simply run the same command again
- **ID-based Tracking**: The script tracks completed questions by their unique IDs
- **Safe Interruption**: You can safely stop the process anytime (Ctrl+C) and resume later

### Evaluate

First, run `evaluate/evaluate_solution.py` to get the result of *answer evaluation*:

```cmd
# Custom input file and output file
python evaluate/evaluate_solution.py \
    --response_file data/seed_0/my_responses.jsonl \
    --output_file data/seed_0/dec_my_responses.jsonl \
    --model_name gpt-4o-mini
```

Then, run `evaluate/evaluate_process.py` to get the result of *process evaluation* to update the `dec_my_responses.jsonl`:

```cmd
# Custom input file, output file, and model
python evaluate/evaluate_solution.py \
    --response_dec_file data/seed_0/dec_my_responses.jsonl \
    --model_name gpt-4o-mini \
    --max_concurrent 5 # Maximum number of concurrent requests.
```

Finally, run `evaluate/statistics.py` or `evaluate/statistics_multi.py` to print the overall statistics:

```cmd
# Statistics the single file
python evaluate/statistics.py \
    --response_dec_file data/seed_0/dec_my_responses.jsonl

# Statistics the multi files
python evaluate/statistics_multi.py \
    --response_dec_files data/seed_0/dec_my_responses.jsonl data/seed_1/dec_my_responses.jsonl data/seed_2/dec_my_responses.jsonl
```

