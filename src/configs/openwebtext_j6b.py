from src.train import ExperimentConfig
from src.model import GPTConfig

config = ExperimentConfig(
    rundir='',
    data_dir='/scr/ayz/nano/openwebtext',
    learning_rate=6e-4,
    batch_size=4,
    warmup_steps=2000,
    min_lr=6e-5,
    lr_decay_steps=600_000,
    max_steps=600_000,
    beta2=0.95,
    weight_decay=0.1,
    eval_interval=1000,
    policy='params=float32,compute=bfloat16,output=bfloat16',
    g_accum_steps=4,
    shard_model=True,
    model_config=GPTConfig(
        block_size=1024, vocab_size=50304, n_layer=28, n_head=16,
        n_embd=4096, dropout=0.0, bias=False,
    )
)
