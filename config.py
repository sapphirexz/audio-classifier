FLOW_DATA = {
    "node1": {
        "title": "Node 1: Does the audio have sound?",
        "question": "Can any sound be heard in this audio?",
        "desc": "If it is completely silent, classify it directly as [No Audio].",
        "input_hint": "Please enter: Yes / No",
        "yes": "node2",
        "no": "result_No_Audio"
    },
    "node2": {
        "title": "Node 2: Is there speech (human or synthesized)?",
        "question": "Does the audio contain human speech, dialogue, reading, broadcasting, etc.?",
        "desc": "If there is only background music, ambient sound, mechanical noise, or animal sounds, it does not count as human speech.",
        "input_hint": "Please enter: Yes / No",
        "yes": "node4",
        "no": "node3"
    },
    "node3": {
        "title": "Node 3: Are there other encodable sounds (laughter, human noise, background speech...)?",
        "question": "Does the audio contain laughter, human noise, background speech, excessive background noise, audio static, or distorted audio?",
        "desc": "If there is no human voice, but audible non-speech content exists, classify it as [No Speech].",
        "input_hint": "Please enter: Yes / No",
        "yes": "result_Select_any_existing_sound:[Laughter,Human_noise,Background_speech,Excessive_background_noise,Audio_static,Distorted_audio]",
        "no": "result_No_Speech"
    },
    "node4": {
        "title": "Node 4: Does it contain sensitive content?",
        "question": "Does the speech content involve profanity, illegality, pornography, violence/terror, discrimination, or other sensitive content?",
        "desc": "If there are obvious sensitive or non-compliant expressions, classify it directly as [Sensitive Content].",
        "input_hint": "Please enter: Yes / No",
        "yes": "result_Sensitive_Content",
        "no": "node5"
    },
    "node5": {
        "title": "Node 5: Does it contain synthesized speech?",
        "question": "Are you sure the file contains TTS speech? AI voiceover, robotic broadcasting, or obvious mechanical synthetic voice? Clues: acoustic features + reading errors (mispronounced numbers/abbreviations, strange accents)?",
        "desc": "If it is machine-generated or has an obvious electronic broadcasting style, classify it as [Contains Synthesized Speech].",
        "input_hint": "Please enter: Yes / No",
        "yes": "result_Check_guidelines_to_confirm",
        "no": "node6"
    },
    "node6": {
        "title": "Node 6: Is there audio in the target language?",
        "question": "Is the language in this audio a foreign language, a non-target language, or clearly incomprehensible?",
        "desc": "If it is not the target language required for transcription, classify it as [Non-target Language].",
        "input_hint": "Please enter: Yes / No",
        "yes": "result_Transcribe_the_file_in_spoken_form_do_not_input_any_other_tags",
        "no": "result_Non-target_Language"
    }
}
