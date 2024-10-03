import json
import time
from decimal import Decimal
from typing import Optional
from urllib.parse import urljoin

import numpy as np
import requests

from core.model_runtime.entities.common_entities import I18nObject
from core.model_runtime.entities.model_entities import (
    AIModelEntity,
    FetchFrom,
    ModelPropertyKey,
    ModelType,
    PriceConfig,
    PriceType,
)
from core.model_runtime.entities.text_embedding_entities import EmbeddingUsage, TextEmbeddingResult
from core.model_runtime.errors.validate import CredentialsValidateFailedError
from core.model_runtime.model_providers.__base.text_embedding_model import TextEmbeddingModel
from core.model_runtime.model_providers.openai_api_compatible.text_embedding.text_embedding import OAICompatEmbeddingModel


class IG1EmbeddingModel(OAICompatEmbeddingModel):
    def _invoke(self, model: str, credentials: dict,
            texts: list[str], user: Optional[str] = None) \
        -> TextEmbeddingResult:
        return super()._invoke(model, credentials, texts, user)

    def validate_credentials(self, model: str, credentials: dict) -> None:
        super().validate_credentials(model, credentials)
