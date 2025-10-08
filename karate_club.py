import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G=nx.karate_club_graph()    #Step1: Loaded dataset
A=nx.to_numpy_array(G)      #Step2: Used adjacency matrix

# print(A)
n=A.shape[1]
print(n)
x=np.ones(n)
x=x/np.linalg.norm(x) #normalization: divides the vector by its magnitude

tol=1e-6
max_iter=100

#Power method to find the eigen vector corresponding to largest eigen value
for _ in range(max_iter):
    x_next=A@x
    x_next=x_next/np.linalg.norm(x_next)
    if np.linalg.norm(x-x_next)<tol:
        break
    x=x_next

#calculate eigen values
lambda_=x.T@(A@x)
#lambda_ is the most dominant eigen value
#x is the eigen vector corresponding to the dominant eigen value

#centrality={node: eigenvector}
centrality={i:float(x[i]) for i in range(n)}
top5=sorted(centrality.items(),
            key=lambda x:x[1], reverse=True)[:5]
top5_nodes=[node for node,_ in top5]


#Visualization
pos=nx.spring_layout(G)
node_sizes=[1000 if node in top5_nodes else 300 for node in G.nodes()]
node_colors=['red' if node in top5_nodes else 'skyblue' for node in G.nodes()]
labels={node: f"{centrality[node]:.2f}" for node in G.nodes()}

plt.figure(figsize=(10,8))
nx.draw(G,pos,node_color=node_colors,node_size=node_sizes,edge_color='gray')
nx.draw_networkx_labels(G, pos, labels, font_size=8)

plt.title("Top 5 influential nodes in karate class")
plt.savefig("karate_centrality.png", dpi=300,bbox_inches='tight')


# for i in range(5):
#     print(f"Node {i}:\n Numpy Centrality: {centrality[i]} \n NetworkX Centrality: {centrality_nx[i]}")









# #returns Zachary's graph

# centrality=nx.eigenvector_centrality(G)
# #returns a dict with node & its evc


# top5=sorted(iterable=centrality.items(), #the sequence to be sorted, items returns a tuple
#             key=lamda evc: evc[1], #iterates over [1] of the iterable
#             reverse=True)[:5] #takes the first 5 elements of the sorted list



