# vLLM Ray/phi-3-mini Problem

### Synopsis

vLLM has no problem using `multiprocessing` as the backend to host any `phi-3-mini` model. However, as soon as Ray is used, it blows up. In the [Ray Dashboard](http://127.0.0.1:8265/#/actors) you will notice that `_AsyncLLMEngine` is dead. If you look at the "System" logs tab and scroll down a bit, you will see:

```shell
ray.exceptions.RaySystemError: System error: No module named 'transformers_modules'
```

### Setup

1. Download [`Phi-3-mini-128k-instruct`](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct) from HuggingFace
2. Setup the conda environment:
   ```shell
   conda env create -f environment.yml
   ```
   > **NOTE:** This problem was experienced with Python 3.11.9, so that's what the conda env uses.
3. Install Ray and vLLM:
   ```shell
   pip install -r requirements.txt
   ```
4. Activate the environment:
   ```shell
   conda activate vllm_phi_3_ray_problem_env
   ```

### Running

> **Important:** Make sure you have activated your conda env!

#### To run with multiprocessing:

```shell
python ./run_with_mp.py
```

#### To [try] to run with Ray:

```shell
python ./run_with_ray.py
```

### Notes

- The ray script contains a print statement telling you whether or not the `transformers_modules` folder is present in your home dir cache. For me, as I don't have `HF_HOME` or `HF_MOFULES_HOME` set, it is.
- If I delete the HF modules dir in teh cache, it gets re-created when I run the Ray file, and I see a `Phi-3-mini-128k-instruct` folder in it.
