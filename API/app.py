from flask import Flask, jsonify, request
from LCSApi import lcsAlgo
from JobSchedulingApi import jobScheduling
from BacktrackingKnapsackApi import resultHandler
from BranchAndBoundKnapsackApi import bresultHandler
from StrassenMatrixMulApi import getMatrices
from BellmanFordApi import Graph
from DFSApi import GraphDFS


app = Flask(__name__)
@app.route("/")
def home():
    return '''
           <form method="POST " action="/Strassen">
               <input type="submit" value="Strassen">
           </form>
           <form method="POST " action="/LCS">
               <input type="submit" value="LCS">
           </form>
           <form method="POST " action="/JobScheduling">
               <input type="submit" value="Job Scheduling">
           </form>
           '''


@app.route('/Strassen', methods=['GET'])
def Strassen():
    return "this is strassen matrix miltiplication code "

@app.route('/LCS', methods=['GET'])
def LCS():
    seq1 = request.args['seq1']
    seq2 = request.args['seq2']

    return jsonify(lcsAlgo(seq1,seq2))

@app.route('/JobScheduling/<count>', methods=['GET'])
def JobScheduling(count):
    jobs =[ ("job"+str(x) , int(request.args[f"job{x}"])) for x in range(1,int(count)+1) ]
     
    return jsonify(jobScheduling(jobs))

@app.route('/BacktrackKnapsack/<count>', methods=['GET'])
def BacktrackKnapsack(count):
    capacity = int(request.args['c'])
    weights =[ int(request.args[f"w{x}"]) for x in range(1,int(count)+1) ]
    values =[  int(request.args[f"v{x}"]) for x in range(1,int(count)+1) ]
     
    return jsonify(resultHandler(int(count),capacity,weights,values))

@app.route('/BranchAndBoundKnapsack/<count>', methods=['GET'])
def BranchAndBoundKnapsack(count):
    capacity = int(request.args['c'])
    weights =[ int(request.args[f"w{x}"]) for x in range(1,int(count)+1) ]
    values =[  int(request.args[f"v{x}"]) for x in range(1,int(count)+1) ]
     
    return jsonify(bresultHandler(int(count),capacity,weights,values))

@app.route("/strassen",methods=['POST'])
def strassen():
    a = request.json['A']
    b = request.json['B']
    return jsonify({"result":str(getMatrices(a,b))})

@app.route("/DFS",methods=['POST'])
def DFS():
    g = GraphDFS()
    g.edgeHandler(request.json["matrix"])
    result = g.DFS(request.json["startVertex"])
    return jsonify({"result":result})

@app.route("/bellmanFord",methods=['POST'])
def bellmanFord():
    g = Graph(request.json["vertices"])
    g.edgeHandler(request.json["matrix"])
    result = g.bellmanFord(request.json["startVertex"])
    return jsonify({"result":result})



if __name__ == '__main__':
    app.run()