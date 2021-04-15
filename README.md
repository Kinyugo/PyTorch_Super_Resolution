# PyTorch Super Resolution

Single Image Super Resolution in PyTorch

![Comparison of Different Image Resolution Techniques](/samples/flowers.png)

Checkout [colab](https://colab.research.google.com/drive/1QbPXtoZYI3d5MCP_v4-vvbGoC-RCiNgX?usp=sharing) notebook for a visualization of how **_SRGAN_** compares to other methods of: **_Bicubic Interpolation_** and **_SRResNet_** based on [this](https://arxiv.org/pdf/1609.04802.pdf) paper.

## Spectacular Results

This is how **_SRGAN_** compares with the popular **_Bicubic Interpolation_**.

![Comparison with Bicubic Interpolation](/samples/cyberpunk1.png)

![Comparison with Bicubic Interpolation](/samples/cyberpunk2.png)

## Setup

```bash
$ pip install -r requirements.txt
```

## Fetching Checkpoints

```bash
$ python fetch_checkpoints.py
```

## Running

To visualize how **_Bicubic Interpolation_**, **_SRResNet_** and **_SRGAN_** perform, run:

> To change the image used modify the block under `main` in **super_resolve.py**

```bash
$ python super_resolve.py
```

## Citations

```bibtex
@inproceedings{ledig2017photo,
  title     = {Photo-realistic single image super-resolution using a generative adversarial network},
  author    = {Ledig, Christian and Theis, Lucas and Husz{\'a}r, Ferenc and Caballero, Jose and Cunningham, Andrew and Acosta, Alejandro and Aitken, Andrew and Tejani, Alykhan and Totz, Johannes and Wang, Zehan and others},
  booktitle = {Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages     = {4681--4690},
  year      = {2017}
}
```

## References

1. Special thanks to [sgrvinod](https://github.com/sgrvinod/), this repository is forked from his [here](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Super-Resolution).
