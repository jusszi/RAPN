
## This is the source code of the RAPN network framework.


### Dateset Soure
We used datasets from the following sources: https://gitlab.com/bottle_shop/safe/prompthate and https://github.com/Social-AI-Studio/Pro-Cap.

### Run RAPN code

```
cd RAPN
pip install -r requirement.txt --extra-index-url https://download.pytorch.org/whl/cu113
bash run_harm_best.sh
bash run_mem_best.sh
```

If you want to run this code, you also need to download the jina-embeddings-v2-small-en model.
