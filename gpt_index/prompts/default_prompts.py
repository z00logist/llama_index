"""Set of default prompts."""

from gpt_index.prompts.prompts import (
    KeywordExtractPrompt,
    KnowledgeGraphPrompt,
    PandasPrompt,
    QueryKeywordExtractPrompt,
    QuestionAnswerPrompt,
    RefinePrompt,
    RefineTableContextPrompt,
    SchemaExtractPrompt,
    SimpleInputPrompt,
    SummaryPrompt,
    TableContextPrompt,
    TextToSQLPrompt,
    TreeInsertPrompt,
    TreeSelectMultiplePrompt,
    TreeSelectPrompt,
)

############################################
# Tree
############################################

DEFAULT_SUMMARY_PROMPT_TMPL = (
    "Напиши краткое изложение следующего. Старайся использовать только"
    "предоставленную информацию. "
    "Постарайся использовать как можно больше ключевых деталей.\n"
    "\n"
    "\n"
    "{context_str}\n"
    "\n"
    "\n"
    'ИЗЛОЖЕНИЕ:"""\n'
)

DEFAULT_SUMMARY_PROMPT = SummaryPrompt(DEFAULT_SUMMARY_PROMPT_TMPL)

# insert prompts
DEFAULT_INSERT_PROMPT_TMPL = (
    "Контекстная информация ниже. Предоставляется в виде нумерованного списка "
    "(от 1 до {num_chunks}),"
    "где каждый элемент списка соотносится с кратким изложением.\n"
    "---------------------\n"
    "{context_list}"
    "---------------------\n"
    "Учитывая контекстную информацию, вот новый фрагмент "
    "информации: {new_chunk_text}\n"
    "Ответьте цифрой, соответствующей изложению, которую необходимо обновить. "
    "Ответ должен быть числом, соответствующим "
    "изложению, которое самое релевантное вопросу.\n"
)
DEFAULT_INSERT_PROMPT = TreeInsertPrompt(DEFAULT_INSERT_PROMPT_TMPL)


# # single choice
DEFAULT_QUERY_PROMPT_TMPL = (
    "Некоторые варианты приведены ниже. Они предоставлены в виде пронумерованного списка "
    "(от 1 до {num_chunks}),"
    "где каждый елемент списка соотносится с кратким изложением.\n"
    "---------------------\n"
    "{context_list}"
    "\n---------------------\n"
    "Используя только указанные выше варианты, а не предварительные знания, верни "
    "выбор, наиболее соответствующий вопросу: '{query_str}'\n"
    "Предоставь выбор в следующем формате: 'ОТВЕТ: <number>' и обьясни, почему "
    "это изложение было выбрано в соответсвии с вопросом.\n"
)
DEFAULT_QUERY_PROMPT = TreeSelectPrompt(DEFAULT_QUERY_PROMPT_TMPL)

# multiple choice
DEFAULT_QUERY_PROMPT_MULTIPLE_TMPL = (
    "Некоторые варианты приведены ниже. Они предоставлены в пронумерованном "
    "списке (от 1 до {num_chunks}), "
    "где каждый елемент списка соотносится с кратким изложением.\n"
    "---------------------\n"
    "{context_list}"
    "\n---------------------\n"
    "Используя только указанные выше варианты, а не предварительные знания, верни "
    "(не более чем {branching_factor}, ранжированный от наиболее релевантных к наименее), который "
    "наиболее соответсвует вопросу: '{query_str}'\n"
    "Предоставь выбор в следующем формате: 'ОТВЕТ: <numbers>' и обьясни, почему  "
    "эти изложения были выбраны в соответсвии с вопросом.\n"
)
DEFAULT_QUERY_PROMPT_MULTIPLE = TreeSelectMultiplePrompt(
    DEFAULT_QUERY_PROMPT_MULTIPLE_TMPL
)


DEFAULT_REFINE_PROMPT_TMPL = (
    "Первоначальный вопрос звучит следующим образом:: {query_str}\n"
    "Мы предоставили существующий ответ: {existing_answer}\n"
    "У нас есть возможность уточнить существующий ответ "
    "(только при необходимости) с дополнительным контекстом ниже.\n"
    "------------\n"
    "{context_msg}\n"
    "------------\n"
    "Учитывая новый контекст, уточни исходный ответ, чтобы лучше "
    "ответить на вопрос. "
    "Если контекст бесполезен, верните исходный ответ."
)
DEFAULT_REFINE_PROMPT = RefinePrompt(DEFAULT_REFINE_PROMPT_TMPL)


DEFAULT_TEXT_QA_PROMPT_TMPL = (
    "Контекстная информация ниже. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Учитывая контекстную информацию, а не предварительные знания, "
    "ответь на вопрос: {query_str}\n"
)
DEFAULT_TEXT_QA_PROMPT = QuestionAnswerPrompt(DEFAULT_TEXT_QA_PROMPT_TMPL)


############################################
# Keyword Table
############################################

DEFAULT_KEYWORD_EXTRACT_TEMPLATE_TMPL = (
    "Некоторый текст приведен ниже. Учитывая текст, извлеки до {max_keywords} "
    "ключевых слов из текста. Избегай стоп-слов."
    "---------------------\n"
    "{text}\n"
    "---------------------\n"
    "Укажите ключевые слова в следующем формате, разделенном запятыми: 'КЛЮЧЕВЫЕ СЛОВА: <keywords>'\n"
)
DEFAULT_KEYWORD_EXTRACT_TEMPLATE = KeywordExtractPrompt(
    DEFAULT_KEYWORD_EXTRACT_TEMPLATE_TMPL
)


# NOTE: the keyword extraction for queries can be the same as
# the one used to build the index, but here we tune it to see if performance is better.
DEFAULT_QUERY_KEYWORD_EXTRACT_TEMPLATE_TMPL = (
    "Ниже представлен вопрос. Учитывая вопрос, извлеки до {max_keywords} "
    "ключевых слов из текста. Сосредоточься на извлечении ключевых слов, которые мы можем использовать "
    "для лучшего поиска ответов на вопрос. Избегай стоп-слов.\n"
    "---------------------\n"
    "{question}\n"
    "---------------------\n"
    "Укажите ключевые слова в следующем формате, разделенном запятыми: 'КЛЮЧЕВЫЕ СЛОВА: <keywords>'\n"
)
DEFAULT_QUERY_KEYWORD_EXTRACT_TEMPLATE = QueryKeywordExtractPrompt(
    DEFAULT_QUERY_KEYWORD_EXTRACT_TEMPLATE_TMPL
)


############################################
# Structured Store
############################################

DEFAULT_SCHEMA_EXTRACT_TMPL = (
    "Мы хотим извлечь соответствующие поля из фрагмента неструктурированного текста в "
    "структурированной схеме. Сначала мы предоставляем неструктурированный текст, а затем "
    "wмы предоставляем схему, которую мы хотим извлечь. "
    "-----------text-----------\n"
    "{text}\n"
    "-----------schema-----------\n"
    "{schema}\n"
    "---------------------\n"
    "Учитывая текст и схему, извлеките соответствующие поля из текста в "
    "следующем формате: "
    "поле1: <value>\nполе2: <value>\n...\n\n"
    "Если поле отсутствует в тексте, не включайте его в вывод."
    "Если в тексте нет полей, вернуть пустую строку.\n"
    "Поля: "
)
DEFAULT_SCHEMA_EXTRACT_PROMPT = SchemaExtractPrompt(DEFAULT_SCHEMA_EXTRACT_TMPL)

# NOTE: taken from langchain and adapted
# https://tinyurl.com/b772sd77
DEFAULT_TEXT_TO_SQL_TMPL = (
    "Учитывая входной вопрос, сначала создайте синтаксически правильный {dialect} "
    "запрос для запуска, затем просмотрите результаты запроса и верните ответ. "
    "Ты можешь упорядочить результаты по соответствующему столбцу, чтобы получить наиболее "
    "интересные примеры в базе данных.\n"
    "Никогда не запрашивай все столбцы из определенной таблицы, запрашивай только "
    "несколько релевантных к вопросу столбцов.\n"
    "Обрати внимание на использование только тех имен столбцов, которые ты видишь описании "
    "схемы. "
    "Будь осторожна, чтобы не запрашивать несуществующие столбцы. "
    "Обрати внимание, какой столбец в какой таблице. "
    "Также, уточняй имена столбцов с именем таблицы, когда это необходимо.\n"
    "Используй следующий формат:\n"
    "Вопрос: Вопрос здесь\n"
    "SQLЗапрос: SQL-запрос для запуска\n"
    "SQLРезультат: Результат SQL-запроса\n"
    "Ответ: Финальный результат здесь\n"
    "Используйте только таблицы, перечисленные ниже.\n"
    "{schema}\n"
    "Вопрос: {query_str}\n"
    "SQLЗапрос: "
)

DEFAULT_TEXT_TO_SQL_PROMPT = TextToSQLPrompt(
    DEFAULT_TEXT_TO_SQL_TMPL, stop_token="\nSQLResult:"
)


# NOTE: by partially filling schema, we can reduce to a QuestionAnswer prompt
# that we can feed to ur table
DEFAULT_TABLE_CONTEXT_TMPL = (
    "Мы предоставили схему таблицы ниже. "
    "---------------------\n"
    "{schema}\n"
    "---------------------\n"
    "Мы также предоставили контекстную информацию ниже. "
    "{context_str}\n"
    "---------------------\n"
    "Учитывая контекстную информацию и схему таблицы, "
    "дай ответ на следующее задание: {query_str}"
)

DEFAULT_TABLE_CONTEXT_QUERY = (
    "Дай высокоуровневое описание таблицы, "
    "а также описание каждого столбца в таблице. "
    "Предоставь ответы в следующем формате:\n"
    "ОписаниеТаблицы: <description>\n"
    "ОписаниеСтолбца1: <description>\n"
    "ОписаниеСтолбца2: <description>\n"
    "...\n\n"
)

DEFAULT_TABLE_CONTEXT_PROMPT = TableContextPrompt(DEFAULT_TABLE_CONTEXT_TMPL)

# NOTE: by partially filling schema, we can reduce to a RefinePrompt
# that we can feed to ur table
DEFAULT_REFINE_TABLE_CONTEXT_TMPL = (
    "Мы предоставили схему таблицы ниже. "
    "---------------------\n"
    "{schema}\n"
    "---------------------\n"
    "Мы также предоставили контекстную информацию ниже. "
    "{context_msg}\n"
    "---------------------\n"
    "Учитывая контекстную информацию и схему таблицы, "
    "дай ответ на следующее задание: {query_str}\n"
    "Мы предоставили существующий ответr: {existing_answer}\n"
    "Учитывая новый контекст, уточните исходный ответ, чтобы лучше "
    "ответить на вопрос. "
    "Если контекст бесполезен, верните исходный ответ."
)
DEFAULT_REFINE_TABLE_CONTEXT_PROMPT = RefineTableContextPrompt(
    DEFAULT_REFINE_TABLE_CONTEXT_TMPL
)


############################################
# Knowledge-Graph Table
############################################

DEFAULT_KG_TRIPLET_EXTRACT_TMPL = (
    "Некоторый текст приведен ниже. Учитывая текст, извлеки до "
    "{max_knowledge_triplets} "
    "триплеты знания в формате (субъект, редикат, объект). Избегай стоп-слов.\n"
    "---------------------\n"
    "Пример:"
    "Текст: Алиса - мать Вани."
    "Триплеты:\n(Алиса, мать, Bани)\n"
    "Tекст: Филз — это кофейня, основанная в Беркли в 1982 году..\n"
    "Triplets:\n"
    "(Филз, это, кофейня)\n"
    "(Филз, основана в , Беркли)\n"
    "(Филз, fоснована в, 1982)\n"
    "---------------------\n"
    "Текст: {text}\n"
    "Триплеты:\n"
)
DEFAULT_KG_TRIPLET_EXTRACT_PROMPT = KnowledgeGraphPrompt(
    DEFAULT_KG_TRIPLET_EXTRACT_TMPL
)

############################################
# HYDE
##############################################

HYDE_TMPL = (
    "Пожалуйста, напиши отрывок, чтобы ответить на вопрос\n"
    "Постарайтесь включить как можно больше ключевых деталей.\n"
    "\n"
    "\n"
    "{context_str}\n"
    "\n"
    "\n"
    'Отрывок:"""\n'
)

DEFAULT_HYDE_PROMPT = SummaryPrompt(HYDE_TMPL)


############################################
# Simple Input
############################################

DEFAULT_SIMPLE_INPUT_TMPL = "{query_str}"
DEFAULT_SIMPLE_INPUT_PROMPT = SimpleInputPrompt(DEFAULT_SIMPLE_INPUT_TMPL)


############################################
# Pandas
############################################

DEFAULT_PANDAS_TMPL = (
    "Ты работаешь с датафреймом pandas в Python.\n"
    "Имя датафрейма - `df`.\n"
    "Это результат команты `print(df.head())`:\n"
    "{df_str}\n\n"
    "Вот входной запрос: {query_str}.\n"
    "Учитывая информацию df и входной запрос, следуйте "
    "этим инструкциям:\n"
    "{instruction_str}"
    "Выход:\n"
)

DEFAULT_PANDAS_PROMPT = PandasPrompt(DEFAULT_PANDAS_TMPL)
