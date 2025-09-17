# DynaSolidGeo

A Dynamic Benchmark for VLM’s Spatial Mathematical Reasoning in Solid Geometry

## How to use

### Generate the questions

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

**Using .env file (Recommended):**
Create a `.env` file in the project root directory:
```
API_KEY=your_api_key_here
BASE_URL=https://api.openai.com/v1
MODEL_NAME=gpt-4o
```

##### Important Notes

- ⚠️ **Never commit your API keys to version control**. Add `.env` to your `.gitignore` file.
- 🔑 If `API_KEY` is not set, the program will raise a `ValueError` with a clear error message.
- 🌐 For OpenAI-compatible services (like vLLM, Ollama, etc.), set the `BASE_URL` to your service endpoint.
- 📦 Make sure to install the required dependencies: `pip install openai tqdm`

</details>

Here we provide our own code `evaluate/gen_response.py` which generates solutions for VLMs using API services with **asynchronous processing** and **smart resume functionality**. 

#### Features

- 🚀 **Concurrent Processing**: Process multiple questions simultaneously (default: 5 concurrent requests)
- 🔄 **Smart Resume**: Automatically skip completed questions based on ID, not line numbers
- 💾 **Real-time Saving**: Results are saved immediately after each completion
- 🎯 **Flexible Output**: Includes both model responses and ground truth solutions

#### Basic Usage

**Process all questions in a dataset:**
```cmd
python evaluate/gen_response.py --input_file data/seed_0/problem.jsonl
```

**Advanced Usage with Custom Parameters:**
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

#### Performance Tips

- **Concurrent Requests**: Increase `--max_concurrent` for faster processing (be mindful of API rate limits)
- **Monitor Progress**: Real-time progress bar shows completion status
- **Error Handling**: Failed requests are logged and can be retried by running the script again

### Evaluate

Run `evaluate/evaluate.py` to get the right (res=1) or not (res=0), which is saved to `evaluate/response_with_res.jsonl`.

Run `evaluate/statistics.py` to get the statistics.