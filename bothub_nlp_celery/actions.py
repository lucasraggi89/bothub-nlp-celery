from . import settings


ACTION_PARSE = "parse"
ACTION_DEBUG_PARSE = "debug_parse"
ACTION_SENTENCE_SUGGESTION = "sentence_suggestion"
ACTION_TRAIN = "train"
ACTION_EVALUATE = "evaluate"


def queue_name(action, language):
    if settings.BOTHUB_NLP_NLU_AGROUP_LANGUAGE_QUEUE:
        return language
    return "{}:{}".format(action, language)
