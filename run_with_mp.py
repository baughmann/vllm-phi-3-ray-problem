from vllm import AsyncEngineArgs, AsyncLLMEngine

# model source: https://huggingface.co/microsoft/Phi-3-mini-128k-instruct

# this config works
mp_args = AsyncEngineArgs(
    model="../models/microsoft/Phi-3-mini-128k-instruct",
    trust_remote_code=True,
    engine_use_ray=False,
    distributed_executor_backend="mp",
    max_model_len=8000,
    disable_sliding_window=True,
)


engine = AsyncLLMEngine.from_engine_args(mp_args)

input("Running engine with `multiprocessing`. Press Enter to close...")
