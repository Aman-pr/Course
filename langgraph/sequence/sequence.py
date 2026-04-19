from  langgraph.graph import StateGraph ,START,END
from typing import TypedDict

class bmi_details(TypedDict):
    weight:float
    height:float
    bmi:float 
    category:str



def main(bmi:bmi_details)->bmi_details:
    height=bmi['height']/100
    weight=bmi['weight']
    bmi_calculated=weight/(height**2)

    bmi['bmi']=bmi_calculated

    return bmi



def bmi_category(state:bmi_details)->bmi_details:
    bmi = state['bmi']

    if bmi < 18.5:
        state["category"] = "Underweight"
    elif 18.5 <= bmi < 25:
        state["category"] = "Normal"
    elif 25 <= bmi < 30:
        state["category"] = "Overweight"
    else:
        state["category"] = "Obese"

    return state




#execution

Grpah=StateGraph(bmi_details)


#Nodes
Grpah.add_node('main',main)
Grpah.add_node('bmi_category',bmi_category)

#Edges
Grpah.add_edge(START,'main')
Grpah.add_edge('main','bmi_category')
Grpah.add_edge('bmi_category',END)
#compile
workflow=Grpah.compile()


inputs={'weight':105.5,'height':190}

result=workflow.invoke(inputs)

print(result)

from IPython.display import Image
Image(workflow.get_graph().draw_mermaid_png())