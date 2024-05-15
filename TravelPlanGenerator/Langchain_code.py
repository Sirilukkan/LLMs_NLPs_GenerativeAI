from langchain_openai import OpenAI #You can use other opensource model from huggingface
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

#set up OpenAI API Key
from sk import my_sk  #sk is the python file that have my_sk = "your OPENAPI Key"
import os
os.environ['OPENAI_API_KEY'] = my_sk

#define function to generate_travel_plan

def gen_travel_plan(country):
    #Chain 1: Find places to go in each country, places_name
    llm = OpenAI(temperature = 0.6)
    prompt_temp_places = PromptTemplate(
        input_variables=['country'],
        template="I want to travel to {country}. Suggest 5 most popular places to go visit. Do not give an explanation of each place"
    )
    places_chain = LLMChain(llm=llm, prompt=prompt_temp_places,output_key="places_name")
    
    #Chain 2: for each places, recommended popular spots and restaurant to visit,
    promp_temp_spots = PromptTemplate(
        input_variables=['places_name'],
        template="Suggest popular spots and restaurants for each {places_name}."
    )

    spots_food_chain = LLMChain(llm=llm, prompt=promp_temp_spots, output_key="spot_food_places")
    
    #chain 3: make one week plan to go to all popular spots and restaurant recommended
    promp_temp_plan = PromptTemplate(
        input_variables=['places_name'],
        template='''
            Suggest one week plans to go to recommended popular spots and restaurants in {places_name}. Start with Day1 until Day 7.
            '''
        )
    plan_chain = LLMChain(llm=llm, prompt=promp_temp_plan, output_key="one_week_plan")
    
    #create chain of all 3 chains combined
    
    chain = SequentialChain(
    chains=[places_chain, spots_food_chain, plan_chain],
        input_variables=['country'],
        output_variables=['places_name', 'spot_food_places', 'one_week_plan']
    )


    response = chain({'country':country})
    return response