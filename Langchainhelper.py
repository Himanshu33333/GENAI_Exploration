import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("OPEN_API_KEY")
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

print(api_key)


def generate_restaurant_name_and_items(cuisine):
    llm = OpenAI(temperature=0.2, api_key=api_key)
    # name = llm.invoke("I want to open a restraunt for {} food. suggent me a only one fancy name for the same")

    promt_restaurant_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restraunt for {cuisine} food. suggent me a only one fancy name for the same"
    )

    # promt_template_name.format(cuisine="Mexican")

    restaurant_llm_chain = promt_restaurant_template_name | llm

    promt_menu_template_name = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest five menu items for {restaurant_name} and return it as a comma separated list"
    )

    # promt_template_name.format(cuisine="Mexican")

    menu_llm_chain = promt_menu_template_name | llm

    from langchain.schema.runnable import RunnableMap
    fullchain = RunnableMap({
        "restaurant_name": restaurant_llm_chain,
        "menu_items": restaurant_llm_chain | menu_llm_chain
    })
    r = fullchain.invoke(cuisine)
    return r

#if __name__ == '__main__':
#    print(generate_restaurant_name_and_items('Italian'))




