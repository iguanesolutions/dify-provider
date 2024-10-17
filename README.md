# IG1 Dify Provider

This is a model provider for [Dify](https://dify.ai/).
It support LLM, Embeddings and Reranking models.
Tags of this repo are following dify versions.

## Build

In order to build the docker image with the ig1 provider you need to specify the dify image version:

```bash
VERSION=0.10.0-beta2
git checkout v${VERSION}
docker build --build-arg dify_image=langgenius/dify-api:${VERSION} -t dify-api:${VERSION}-ig1 .
```
