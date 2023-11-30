# midGPT
A simple and hackable repository for training mid-sized GPTs (language models).  midGPT aims to be the easiest way to pretrain LLMs with billion+ parameters on limited compute resources. Built using Jax+[Equinox](https://github.com/patrick-kidger/equinox). Directly inspired by [NanoGPT](https://github.com/karpathy/nanoGPT/).

Model code is in `src/model.py`, training code is in `src/train.py`. Experiments are configured in `src/configs/*.py`.

## Setup and start
Tested on Python **3.10.12**. From a fresh virtualenv, install Jax according to their [instructions](https://jax.readthedocs.io/en/latest/installation.html), then `pip install -r requirements.txt`. On TPU VMs, the Jax install is:

```bash
pip install jax[tpu] -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
```


Start training:
```bash
python launch.py --config=shakespeare_char
python launch.py --config=openwebtext
# Resume training from existing rundir
python launch.py --config=openwebtext --rundir=<rundir>

# Launch tensorboard
tensorboard --logdir=<parent of rundir>
```

Add a `--debug` if you want to (1) enable jax profiler and (2) skip checkpoint saving.

## Feature list

 - [x] Basic training on OWT
 - [x] Mixed precision
 - [x] Data parallel training
 - [x] FSDP
 - [x] Checkpointing and resuming
 - [x] Logging
 - [x] Grad accumulation


## Debugging
* Testing parallelism in cpu: `JAX_PLATFORM_NAME=cpu XLA_FLAGS=--xla_force_host_platform_device_count=8 python train_shakespeare.py`.
* TB profiler: `pip install tensorflow-cpu tensorboard-plugin-profile`.
