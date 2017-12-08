#Author:
#Dilpreet Singh Chawla
#Indian Institute of Information Technology Kalyani

#Basic Operations on Graph using Adjacency Matrix

n=int(input("Enter number of vertices: "))
m=[[0 for x in range(n)] for y in range(n)]  #Initialising Adjacency Matrix with 0's
edges=[]

for tup in input("Enter the edges: ").split('),('):  #eg: (1,2),(2,4),(3,5)......
    tup = tup.replace(')','').replace('(','')
    edges.append(tuple(map(int,tup.split(','))))
    
#Making Adjacency Matrix
for tup in edges:
    m[tup[0]-1][tup[1]-1]+=1
    m[tup[1]-1][tup[0]-1]+=1

while True:
    #menu-driven program
    print("Main Menu\n1.Print Degree of each vertex\n2.Check Adjacency of two vertices\n3.Check Adjacency of two edges\n4.Check graph is Regular or not\n5.Check graph is Complete or not\n6.Check graph is Euler or not\n7.Quit")
    ch=int(input())
    
    if ch==1:
        print("Degree of vertices")    
        for row in m:
            print(sum(row))

    elif ch==2:        
        v1,v2=map(int,input("Enter the two vertices to check adjacency: ").split(',')) #eg: 2,5 
        if m[v1-1][v2-1]!=0:
            print("Adjacent Vertices")
        else:
            print("Not Adjacent")

    elif ch==3:        
        two_edge=[]    
        for tup in input("Enter the edges to check adjacency: ").split('),('): #eg: (1,2),(3,2)
            tup = tup.replace(')','').replace('(','')
            two_edge.append(tuple(map(int,tup.split(','))))

        if two_edge[0][1]==two_edge[1][0] or two_edge[0][0]==two_edge[1][1]:
            print("Adjacent Edges")
        else:
            print("Not Adjacent Edjes")

    elif ch==4:
        #For regular graph degree of each vertex should be same
        
        s=sum(m[0])
        f=0
        for row in m:
            if sum(row)!=s:
                f=1
                break
        if f==0:
            print("Regular Graph")
        else:
            print("Irregular Graph")

    elif ch==5:
        #For complete graph degree of each vertex should be n-1 where n is number of vertices
        
        s=n-1
        f=0
        for row in m:
            if sum(row)!=s:
                f=1
                break
        if f==0:
            print("Complete Graph")
        else:
            print("Incomplete Graph")

    elif ch==6:
        #For euler graph degree of all vertices should be even
        
        od=[sum(row) for row in m if sum(row)%2!=0]
        if len(od)==0:
            print("Euler Graph")
        else:
            print("Not Euler Graph")

    elif ch==7:
        exit()
