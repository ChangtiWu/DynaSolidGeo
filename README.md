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

Here we provide our own code `evaluate/gen_response.py` which is to generate the solutions for close-sourced VLMs by API services. Please run `evaluate/gen_response.py` to generate the `evaluate/response.jsonl`(final answers only) and `evaluate/response_cot.jsonl` (full responses with CoT):

```cmd
python evaluate/gen_response.py
```


### Evaluate

Run `evaluate/evaluate.py` to get the right (res=1) or not (res=0), which is saved to `evaluate/response_with_res.jsonl`.

Run `evaluate/statistics.py` to get the statistics.