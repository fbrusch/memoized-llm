# memoized-llm

A small wrapper for LLM calls using persistent memoization (backed by the [memoizer](https://github.com/francesco/memoizer) library).

## Usage

```python
from memoized_llm import memoized_llm

pdf_content = open("text.pdf", "rb").read()
prompt = b"Translate the attached PDF to English."

response = memoized_llm("gpt-4", prompt, {"temperature": 0.7}, [pdf_content])
```