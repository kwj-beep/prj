import pandas as pd
from importlib import resources

def tool_get_doe(id : int):
    return pd.DataFrame({'x':[1,2,3] ,'y':[4,5,6]})



if __name__ == "__main__":
    #print(tool_get_doe(3))
    resources.files('prj')