APP_TITLE = "MicroApp Demo App #2"
APP_INTRO = """This app demonstrates all the various AI Prompt configurations that are available to a micro-app. It can be used to understand what kinds of actions a "phase" can accomplish, and how to configure those actions. 
"""

APP_HOW_IT_WORKS = """
 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = """You provide brief 1-2 sentence answers to the instructions you are provided. You never ask questions in your responses. """

PHASES = {
    "phase1": {
        "name": "No Submission",
        "fields": {
            "markdown": {
                "type": "markdown",
                "body": """A phase can be purely informational and have no submission. It simply displays the fields and moves onto the next phase.""",
                "unsafe_allow_html": True
            }
        },
        "no_submission": True
    },
    "phase2": {
        "name": "Basic Feedback",
        "fields": {
            "markdown": {
                "type": "markdown",
                "body": """The most basic phase asks a question, receives a response from the user, and sends that response in a prompt to the AI for feedback.""",
                "unsafe_allow_html": True
            },
            "name": {
                "type": "text_input",
                "label": """What is your name?""",
                "value": "Abe"
            }
        },
        "phase_instructions": "The user will provide their name. Welcome them by name.",
        "user_prompt": "My name is {name}. Hello!",
        "allow_skip": True,
    },
    "phase3": {
        "name": "Skippable Phase",
        "fields": {
            "markdown": {
                "type": "markdown",
                "body": """Phases can be skippable. Since an AI can make mistakes and get confused, it is recommended that phases are skippable whenever possible.""",
                "unsafe_allow_html": True
            },
            "skip_me": {
                "type": "text_area",
                "label": "Write a 2,000 word analysis on The Epistemological Implications of Quantum Entanglement on Post-Structuralist Interpretations of Derrida’s Deconstructionism",
            }
        },
        "phase_instructions": "Analyze the user's essay on The Epistemological Implications of Quantum Entanglement on Post-Structuralist Interpretations of Derrida’s Deconstructionism",
        "user_prompt": "{skip_me}",
        "allow_skip": True,
    },
    "phase4": {
        "name": "Scored Phase",
        "fields": {
            "markdown": {
                "type": "markdown",
                "body": """Phases can be scored according to a rubric. In general, AI provides more accurate scoring when instructions are specific and the criteria are measurable.""",
                "unsafe_allow_html": True
            },
            "animal": {
                "type": "text_input",
                "label": "Provide the name of an animal. Any animal is fine, but it must be an animal.",
                "value": "Monkey"
            }
        },
        "phase_instructions": "The user will provide the name of an animal. Encourage them if they input a valid animal. Explain that they are incorrect if they do not.",
        "user_prompt": "{animal}",
        "allow_skip": True,
        "scored_phase": True,
        "rubric": """
                1. Animal Name
                    1 point - The user provides a valid animal name.
                    0 points - The user provides input that does not include a valid animal name. 
            """,
        "minimum_score": 1
    },
    "phase5": {
        "name": "Hard-Coded Phase",
        "fields": {
            "markdown": {
                "type": "markdown",
                "body": """You can provide hard-coded responses. For example, if you are just collecting some input and you want to provide static feedback for that input.""",
                "unsafe_allow_html": True
            },
            "name2": {
                "type": "text_input",
                "label": "What is another name?",
                "key": "name2",
                "value": "Abe"
            }
        },
        "allow_skip": True,
        "ai_response": False,
        "custom_response": "Hi {name2}! This is a hard-coded response, it is not being generated by AI."
    },
    "phase6": {
        "name": "Phase with Revisions",
        "fields": {
            "markdown": {
                "type": "markdown",
                "body": """Any phase can have the ability to allow revisions, and a limit to the number of revisions available. This is useful if the AI is generating something that the user might want to tweak.""",
                "unsafe_allow_html": True
            },
            "topic": {
                "type": "text_input",
                "label": "Give me a topic to generate a multiple choice question for.",
                "value": "DisneyLand"
            }
        },
        "allow_skip": True,
        "ai_response": True,
        "user_prompt": "Please write me a single multiple choice question with three distractors and one correct answer about the following topic: {topic}",
        "allow_revisions": True,
        "max_revisions": 2,
    },
    "phase7": {
        "name": "Phase with editable prompt",
        "fields": {
            "markdown": {
                "type": "markdown",
                "body": """Any phase can have the ability to view and edit the final prompt. This can be useful when you want the user to have fine-grained control over what is being sent to the AI.""",
                "unsafe_allow_html": True
            },
            "domicile": {
                "type": "radio",
                "label": "Choose one:",
                "options": ['Shoe', 'Fishing Boat', 'Water Park'],
            }
        },
        "allow_skip": True,
        "ai_response": True,
        "user_prompt": "Write a whimsical haiku about {name} who likes {animal}(s) and lives in a {domicile}",
        "show_prompt": True,
        "read_only_prompt": False
    },
    "phase8": {
        "name": "Combining Rules",
        "fields": {
            "markdown": {
                "type": "markdown",
                "body": """Most options can be combined. This is a phase that is skippable, scored, allows revisions, and shows an editable prompt. """,
                "unsafe_allow_html": True
            },
            "haiku": {
                "type": "text_area",
                "height": 200,
                "label": "Write a Haiku about The Industrial Revolution.",
                "value": """Smoke stacks pierce the sky,
Iron and steam reshape life—
Machines hum, men sigh.""",
            }
        },
        "allow_skip": True,
        "ai_response": True,
        "phase_instructions": "The user will write a Haiku about the industrial revolution. You should ensure it is a traditional Haiku and it is about the topic of the industrial revolution.",
        "user_prompt": "Here is my Haiku about the industrial revolution: \n\n {haiku}",
        "scored_phase": True,
        "rubric": """
        1. Haiku:
        2 points - The user has entered a true Haiku poem with traditional Haiku Structure.
        1 point - The user has entered a poem of some sort.
        0 points - The user has not entered a poem of any kind.
        2. Topic
        2 points - The user has mentioned the Industrial Revolution. 
        0 points - The user has NOT mentioned the Industrial Revolution. 
        """,
        "minimum_score": 2,
        "show_prompt": True,
        "read_only_prompt": False
    }

}

def prompt_conditionals(prompt, user_input, phase_name=None):
    #TO-DO: This is a hacky way to make prompts conditional that requires the user to know a lot of python and get the phase and field names exactly right. Future task to improve it. 




    return prompt
    
selected_llm = "gpt-3.5-turbo"


LLM_CONFIGURATIONS = {
    "gpt-3.5-turbo": {
        "model": "gpt-3.5-turbo-0125",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":0.50,
        "price_output_token_1M":1.50
    },
    "gpt-4-turbo": {
        "model": "gpt-4-turbo",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":10,
        "price_output_token_1M":30
    },
    "gpt-4o": {
        "model": "gpt-4o",
        "frequency_penalty": 0,
        "max_tokens": 250,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":5,
        "price_output_token_1M":15
    },
    "gemini-1.0-pro": {
        "model": "gemini-1.0-pro",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":.5,
        "price_output_token_1M":1.5
    },
    "gemini-1.5-flash": {
        "model": "gemini-1.5-flash",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":.35,
        "price_output_token_1M":1.05
    },
    "gemini-1.5-pro": {
        "model": "gemini-1.5-pro",
        "temperature": 1,
        "top_p": 0.95,
        "max_tokens": 1000,
        "price_input_token_1M":3.5,
        "price_output_token_1M":10.50
    },
    "claude-3.5-sonnet": {
        "model": "claude-3-5-sonnet-20240620",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 3,
        "price_output_token_1M": 15
    },
    "claude-opus": {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 15,
        "price_output_token_1M": 75
    },
    "claude-sonnet": {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 3,
        "price_output_token_1M": 15
    },
    "claude-haiku": {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1000,
        "temperature": 1,
        "price_input_token_1M": 0.25,
        "price_output_token_1M": 1.25
    }
}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False
