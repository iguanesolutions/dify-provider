ARG dify_image=langgenius/dify-api:0.10.0-beta2
FROM ${dify_image} AS dify
WORKDIR /app/api
COPY ig1 /app/api/core/model_runtime/model_providers/ig1
RUN echo "- ig1" >> /app/api/core/model_runtime/model_providers/_position.yaml
