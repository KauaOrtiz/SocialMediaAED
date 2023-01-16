import json
import graph
import igraph
import cairo

#pip install python-igraph  
#pip install pycairo

class Search():
    def __init__(self, username, topic = None):
        self.username = username
        self.topic = topic
        self.graph = None
        if self.topic == None:
            self.graphByChoose("family")
            self.graphByChoose("friends")
            self.graphByChoose("someone")
        else:
            self.graphByChoose(self.topic)
        

    def teste(self, list, label, counter):
        eG=igraph.Graph(directed=False)
        eG.add_vertices(counter)
        eG.add_edges(list)

        layout = eG.layout("kk")

        visual_style = {}
        visual_style["vertex_label"] = label
        visual_style["vertex_size"] = 60
        visual_style["bbox"] = (400, 400)


        igraph.plot(eG, "teste.png", **visual_style)

    def formatGraph(self, list, counter):
        listNames = []
        listConvert = []
        aux = open('database.json')
        data = json.load(aux)
        for i in data['users']:
            listNames.append(i["username"])
        print(listNames)

        for a in list:
            listConvert.append((listNames.index(a[0]),listNames.index(a[1])))
        self.teste(listConvert,listNames, counter)


    def graphByChoose(self, topic):
        list = []
        counter = 0
        aux = open('database.json')
        data = json.load(aux)
        for i in data['users']:
            counter +=1
        print(counter)
        self.graphByChooseR(topic, data,graph.Graph(), self.username)
        g = self.graph
        print("Graph {}".format(topic))
        for v in g:
            for w in v.getConnections():
                list.append((v.getId(), w.getId()))
                print("( %s , %s)" % (v.getId(), w.getId()))
        #print(list)
        self.formatGraph(list, counter)
        aux.close()

    def graphByChooseR(self,topic, data, graph, username=None):
        if username == None:
            username = self.username
        else:
            pass
        g = graph

        isExist = False
        for i in data['users']:
            if i["username"] == username:
                g.addVertex(username, username)
                for j in i[topic]:
                    if g.getVertex(j) == None:
                        g.addVertex(j,j)
                        g.addEdge(username,j)
                        self.graphByChooseR(topic, data, g, j)
                    else:
                        if g.addEdge(username,j) == False:
                            return False

                isExist = True
                break
        if isExist == False:
            pass

        self.graph = g