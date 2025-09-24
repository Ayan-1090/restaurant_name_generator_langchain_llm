from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.5)


def generate_restraun_name_menu(cuisine):

    restaurant_prompt = PromptTemplate(input_variables=["cuisine"],
                                       template="I want to open a restaurant that serves {cuisine} food. Suggest me one fancy name for it.")

    restaurant_name_chain = LLMChain(
        llm=llm, prompt=restaurant_prompt, output_key="restaurant_name")

    menu_prompt = PromptTemplate(input_variables=["restaurant_name"],
                                 template="Suggest a fancy menu for a restaurant named {restaurant_name}.Return it in comma seperated values format.")

    restaurant_menu_chain = LLMChain(
        llm=llm, prompt=menu_prompt, output_key="menu_items")

    create_restaurant_chain = SequentialChain(
        chains=[restaurant_name_chain, restaurant_menu_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
        verbose=True)

    response = create_restaurant_chain({"cuisine": cuisine})  # Example usage
    return response
