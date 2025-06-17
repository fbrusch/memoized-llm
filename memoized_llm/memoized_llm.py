import llm
from typing import Dict, List

from memoizer import memoize


def memoizable_llm(
    model: str, prompt: bytes, options: Dict, attachments: List[bytes]
) -> str:
    model = llm.get_model(model)
    response = model.prompt(
        prompt.decode("utf-8"),
        **options,
        attachments=[llm.Attachment(content=attachment) for attachment in attachments],
    )
    return response.text()


memoized_llm = memoize(memoizable_llm)
