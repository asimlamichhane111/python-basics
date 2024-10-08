import numpy as np
surname=('Luffy','Law','Newgate')
first_name=('Monkey D','Trafalgar','Edward')
ind= np.lexsort((first_name,surname))
print(ind)
out_arr=[first_name[i]+" "+surname[i] for i in ind]
print(out_arr)
