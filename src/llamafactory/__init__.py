

r"""
Efficient fine-tuning of large language models.

Level:
  api, webui > chat, eval, train > data, model > hparams > extras

Dependency graph:
  main:
    transformers>=4.41.2
    datasets>=2.16.0
    accelerate>=0.30.1
    peft>=0.11.1
    trl>=0.8.6
  attention:
    transformers>=4.42.4 (gemma+fa2)
  longlora:
    transformers>=4.41.2,<=4.42.4
  packing:
    transformers>=4.41.2,<=4.42.4
  patcher:
    transformers==4.41.2 (chatglm)
"""


from .cli import VERSION


__version__ = VERSION
