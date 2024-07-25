from pathlib import Path

import ray
from vllm import AsyncEngineArgs, AsyncLLMEngine

# this config does not work. it just sits at
#   "INFO worker.py:1779 -- Started a local Ray instance. View the dashboard at..."
# The actor dies with a `ray.exceptions.RaySystemError: System error: No module named 'transformers_modules'`
ray_args = AsyncEngineArgs(
    model="../models/microsoft/Phi-3-mini-128k-instruct",
    trust_remote_code=True,
    max_model_len=8000,
    engine_use_ray=True,
    distributed_executor_backend="ray",
)

does_transformers_modules_exist = Path(
    Path.home() / ".cache/huggingface/modules/transformers_modules/"
).exists()
print(f"Does transformers_modules exist in cache? {does_transformers_modules_exist}")

engine = AsyncLLMEngine.from_engine_args(ray_args)

input(
    "Running engine with Ray. \n"
    "Open the local Ray dashboard and inspect the actor's 'System' logs.\n"
    "You will notice that it died with `ray.exceptions.RaySystemError: System error: No module named 'transformers_modules'`\n\n"
    "Press Enter to shutdown Ray..."
)

ray.shutdown()
