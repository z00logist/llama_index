"""Prompts for ChatGPT."""

from langchain.prompts.chat import (
    AIMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

from gpt_index.prompts.prompts import RefinePrompt, RefineTableContextPrompt

# Refine Prompt
CHAT_REFINE_PROMPT_TMPL_MSGS = [
    HumanMessagePromptTemplate.from_template("{query_str}"),
    AIMessagePromptTemplate.from_template("{existing_answer}"),
    HumanMessagePromptTemplate.from_template(
        "У нас есть возможность уточнить приведенный выше ответ "
        "(только если нужно) с дополнительным контекстом ниже.\n"
        "------------\n"
        "{context_msg}\n"
        "------------\n"
        "Учитывая новый контекст, уточни исходный ответ, чтобы "
        "лучше ответить на вопрос."
        "Если контекст бесполезен, выйдай исходный ответ. ",
    ),
]


CHAT_REFINE_PROMPT_LC = ChatPromptTemplate.from_messages(CHAT_REFINE_PROMPT_TMPL_MSGS)
CHAT_REFINE_PROMPT = RefinePrompt.from_langchain_prompt(CHAT_REFINE_PROMPT_LC)


# Table Context Refine Prompt
CHAT_REFINE_TABLE_CONTEXT_TMPL_MSGS = [
    HumanMessagePromptTemplate.from_template("{query_str}"),
    AIMessagePromptTemplate.from_template("{existing_answer}"),
    HumanMessagePromptTemplate.from_template(
        "Мы предоставили схему таблицы ниже."
        "---------------------\n"
        "{schema}\n"
        "---------------------\n"
        "Мы также предоставили некоторую контекстную информацию ниже. "
        "{context_msg}\n"
        "---------------------\n"
        "Учитывая контекстную информацию и схему таблицы, "
        "уточни исходный ответ, чтобы лучше "
        "ответить на вопрос. "
        "Если контекст бесполезен, выдай исходный ответ. "
    ),
]
CHAT_REFINE_TABLE_CONTEXT_PROMPT_LC = ChatPromptTemplate.from_messages(
    CHAT_REFINE_TABLE_CONTEXT_TMPL_MSGS
)
CHAT_REFINE_TABLE_CONTEXT_PROMPT = RefineTableContextPrompt.from_langchain_prompt(
    CHAT_REFINE_TABLE_CONTEXT_PROMPT_LC
)
