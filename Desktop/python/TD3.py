import random 
echec_dim=8
class individu: 
    def __init__(self,val=None):
        
        if val==None:
            self.val=random.sample(list(range(echec_dim)),echec_dim)
        else:
            self.val=val
    def __str__(self):
        return ' '.join(map(str,self.val))
    def fitness(self):
        nbconflict=0
        for i in range(echec_dim-1):
            for j in range(i+1,echec_dim):
                if(individu.conflict([self.val[i],i],[self.val[j],j])):
                    nbconflict+=1
        return nbconflict
    def conflict (p1,p2):
        print(p1,p2)
        if ((p1[0]==p2[0]) or (p1[1]==p2[1]) or (abs(p1[0]-p2[0])==abs(p2[1]-p1[1]))):
            print("ui")
            return True
        else:
            print("n")
            return False
def create_rand_pop(count):
    pop=[]
    for i in range(count):
        pop.append(individu())
    return pop
def evaluate(pop):
    return sorted(pop, key=lambda individu: individu.fitness())

def selection(pop,hcount,lcount):
    return pop[:hcount]+pop[-lcount:]

def croisement(ind1,ind2):
    return [ind1.val[:4]+ind2.val[-4:]],[ind2.val[:4]+ind1.val[-4:]]

def mutation(ind):
    rand=random.randint(0,echec_dim-1)
    ind2=individu(ind.val)
    ind2.val[rand]=random.randint(0,echec_dim-1)
    return ind2

def algoloopSimple():
    pop=create_rand_pop(25)
    solutiontrouvee=False
    nbiteration=0
    while not solutiontrouvee:
        print("iteration numéro: ", nbiteration)
        nbiteration+=1
        evaluation=evaluate(pop)
        if evaluation[0].fitness()==0:
            solutiontrouvee=True
        else:
            select=selection(evaluation,10,4)
            croises=[]
            for i in range(0, len(select),2):
                print("BBBBBBBBBB",select)
                croises+=croisement(select[i],select[i+1])
            mutes=[]
            for i in select:
                print("BBBBBBBBBB",select)
                print("AAAAAAAAAAAAAAAA",i)
                mutes.append(mutation(i))
            newalea=create_rand_pop(5)
            pop=select[:]+croises[:]+mutes[:]+newalea[:]
        print(evaluation[0])

algoloopSimple()



