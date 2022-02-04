false = False
true = True


def f(boolean):
    return str(boolean).lower()


class SettingFile:
    def __init__(self):
        self.data = dict()
        self.data['Formation'] = dict()
        self.data['Formation']['Win'] = "433"
        self.data['Formation']['Lost'] = "433"
        self.data['Formation']['Draw'] = "433"

        self.data['Strategy'] = dict()
        self.data['Strategy']["Is5ForwardWin"] = true
        self.data['Strategy']["Is5ForwardLost"] = true
        self.data['Strategy']["Is5ForwardDraw"] = true
        self.data['Strategy']["TeamTactic"] = "Normal"
        self.data['Strategy']["IsGoalForward"] = false

        self.data['ChainAction'] = dict()
        self.data['ChainAction']["ChainNodeNumber"] = 750
        self.data['ChainAction']['ChainDeph'] = 2
        self.data['ChainAction']['UseShootSafe'] = false
        self.data['ChainAction']['DribblePosCountZ'] = 0.8
        self.data['ChainAction']['DribblePosCountMaxFrontOpp'] = 8
        self.data['ChainAction']['DribblePosCountMaxBehindOpp'] = 4

        self.data['OffensiveMove'] = dict()
        self.data['OffensiveMove']['Is9BrokeOffside'] = false

        self.data['DefenseMove'] = dict()
        self.data['DefenseMove']["PassBlock"] = false
        self.data['DefenseMove']["StartMidMark"] = -30.0
        self.data['DefenseMove']["StaticOffensiveOpp"] = [8, 9, 10, 11]
        self.data['DefenseMove']["MidTh_BackInMark"] = true
        self.data['DefenseMove']["MidTh_BackInBlock"] = true
        self.data['DefenseMove']["MidTh_HalfInMark"] = true
        self.data['DefenseMove']["MidTh_HalfInBlock"] = true
        self.data['DefenseMove']["MidTh_ForwardInMark"] = false
        self.data['DefenseMove']["MidTh_ForwardInBlock"] = true
        self.data['DefenseMove']["MidTh_RemoveNearOpps"] = true
        self.data['DefenseMove']["MidTh_DistanceNearOpps"] = 5.0
        self.data['DefenseMove']["MidTh_XNearOpps"] = 3.0
        self.data['DefenseMove']["MidTh_PosDistZ"] = 1.0
        self.data['DefenseMove']["MidTh_HPosDistZ"] = 0.7
        self.data['DefenseMove']["MidTh_PosMaxDistMark"] = 15.0
        self.data['DefenseMove']["MidTh_HPosMaxDistMark"] = 15.0
        self.data['DefenseMove']["MidTh_HPosYMaxDistMark"] = 12.0
        self.data['DefenseMove']["MidTh_PosMaxDistBlock"] = 20.0
        self.data['DefenseMove']["MidTh_HPosMaxDistBlock"] = 20.0
        self.data['DefenseMove']["MidTh_HPosYMaxDistBlock"] = 20.0
        self.data['DefenseMove']["MidProj_PosMaxDistMark"] = 10.0
        self.data['DefenseMove']["MidProj_HPosMaxDistMark"] = 10.0
        self.data['DefenseMove']["MidProj_PosMaxDistBlock"] = 25.0
        self.data['DefenseMove']["MidProj_HPosMaxDistBlock"] = 25.0
        self.data['DefenseMove']["Mid_UseProjectionMark"] = true
        self.data['DefenseMove']["MidNear_StartX"] = 30.0
        self.data['DefenseMove']["MidNear_BackInMark"] = false
        self.data['DefenseMove']["MidNear_BackInBlock"] = false
        self.data['DefenseMove']["MidNear_HalfInMark"] = true
        self.data['DefenseMove']["MidNear_HalfInBlock"] = true
        self.data['DefenseMove']["MidNear_ForwardInMark"] = true
        self.data['DefenseMove']["MidNear_ForwardInBlock"] = true
        self.data['DefenseMove']["MidNear_OppsDistXToBall"] = 25.0
        self.data['DefenseMove']["MidNear_MarkAgain"] = true
        self.data['DefenseMove']["MidNear_BlockAgain"] = false
        self.data['DefenseMove']["MidNear_MarkAgainMaxDistToChangeCost"] = 5.0
        self.data['DefenseMove']["MidNear_MarkAgainChangeCostZ"] = 1.4
        self.data['DefenseMove']["MidNear_PosMaxDistMark"] = 10.0
        self.data['DefenseMove']["MidNear_HPosMaxDistMark"] = 15.0
        self.data['DefenseMove']["MidNear_PosMaxDistBlock"] = 20.0
        self.data['DefenseMove']["MidNear_HPosMaxDistBlock"] = 20.0
        self.data['DefenseMove']["Goal_ForwardInMark"] = false
        self.data['DefenseMove']["Goal_ForwardInBlock"] = true
        self.data['DefenseMove']["Goal_PosMaxDistMark"] = 10.0
        self.data['DefenseMove']["Goal_HPosMaxDistMark"] = 10.0
        self.data['DefenseMove']["Goal_OffsideMaxDistMark"] = 10.0
        self.data['DefenseMove']["Goal_PosMaxDistBlock"] = 25.0
        self.data['DefenseMove']["Goal_HPosMaxDistBlock"] = 25.0
        self.data['DefenseMove']["Goal_OffsideMaxDistBlock"] = 25.0

    def clone(self):
        out = SettingFile()
        for key in self.data.keys():
            for key2 in self.data[key].keys():
                out.data[key][key2] = self.data[key][key2]
        return out

    def to_string(self):
        return f'''{{
    	"Strategy":	{{
    				"Formation":	{{
    							"Win":"{self.data['Formation']['Win']}",
    							"Lost":"{self.data['Formation']['Lost']}",
    							"Draw":"{self.data['Formation']['Draw']}"
    						}},
    				"Is5ForwardWin":{f(self.data['Strategy']["Is5ForwardWin"])},
    				"Is5ForwardLost":{f(self.data['Strategy']["Is5ForwardLost"])},
    				"Is5ForwardDraw":{f(self.data['Strategy']["Is5ForwardDraw"])},
    				"TeamTactic":"{self.data['Strategy']["TeamTactic"]}",
    				"IsGoalForward":{f(self.data['Strategy']["IsGoalForward"])}
    			}},
    	"ChainAction":	{{
    				"ChainNodeNumber":{self.data['ChainAction']["ChainNodeNumber"]},
    				"ChainDeph":{self.data['ChainAction']['ChainDeph']},
    				"UseShootSafe":{f(self.data['ChainAction']['UseShootSafe'])},
    				"DribblePosCountZ":{self.data['ChainAction']['DribblePosCountZ']},
    				"DribblePosCountMaxFrontOpp":{self.data['ChainAction']['DribblePosCountMaxFrontOpp']},
    				"DribblePosCountMaxBehindOpp":{self.data['ChainAction']['DribblePosCountMaxBehindOpp']}
    			}},
    	"OffensiveMove":{{
    				"Is9BrokeOffside":{f(self.data['ChainAction']['UseShootSafe'])}
    			}},
    	"DefenseMove": {{
    				"PassBlock":{f(self.data['DefenseMove']["PassBlock"])},
    				"StartMidMark":{self.data['DefenseMove']["StartMidMark"]},
    				"StaticOffensiveOpp":{self.data['DefenseMove']["StaticOffensiveOpp"]},
    				"MidTh_BackInMark":{f(self.data['DefenseMove']['MidTh_BackInMark'])},
    				"MidTh_BackInBlock":{f(self.data['DefenseMove']['MidTh_BackInBlock'])},
    				"MidTh_HalfInMark":{f(self.data['DefenseMove']['MidTh_HalfInMark'])},
    				"MidTh_HalfInBlock":{f(self.data['DefenseMove']['MidTh_HalfInBlock'])},
    				"MidTh_ForwardInMark":{f(self.data['DefenseMove']['MidTh_ForwardInMark'])},
    				"MidTh_ForwardInBlock":{f(self.data['DefenseMove']['MidTh_ForwardInBlock'])},
    				"MidTh_RemoveNearOpps":{f(self.data['DefenseMove']['MidTh_RemoveNearOpps'])},
    				"MidTh_DistanceNearOpps":{self.data['DefenseMove']['MidTh_DistanceNearOpps']},
    				"MidTh_XNearOpps":{self.data['DefenseMove']['MidTh_XNearOpps']},
    				"MidTh_PosDistZ":{self.data['DefenseMove']['MidTh_PosDistZ']},
    				"MidTh_HPosDistZ":{self.data['DefenseMove']['MidTh_HPosDistZ']},
    				"MidTh_PosMaxDistMark":{self.data['DefenseMove']['MidTh_PosMaxDistMark']},
    				"MidTh_HPosMaxDistMark":{self.data['DefenseMove']['MidTh_HPosMaxDistMark']},
    				"MidTh_HPosYMaxDistMark":{self.data['DefenseMove']['MidTh_HPosYMaxDistMark']},
    				"MidTh_PosMaxDistBlock":{self.data['DefenseMove']['MidTh_PosMaxDistBlock']},
    				"MidTh_HPosMaxDistBlock":{self.data['DefenseMove']['MidTh_HPosMaxDistBlock']},
    				"MidTh_HPosYMaxDistBlock":{self.data['DefenseMove']['MidTh_HPosYMaxDistBlock']},
    				"MidProj_PosMaxDistMark":{self.data['DefenseMove']['MidProj_PosMaxDistMark']},
    				"MidProj_HPosMaxDistMark":{self.data['DefenseMove']['MidProj_HPosMaxDistMark']},
    				"MidProj_PosMaxDistBlock":{self.data['DefenseMove']['MidProj_PosMaxDistBlock']},
    				"MidProj_HPosMaxDistBlock":{self.data['DefenseMove']['MidProj_HPosMaxDistBlock']},
    				"Mid_UseProjectionMark":{f(self.data['DefenseMove']['Mid_UseProjectionMark'])},
    				"MidNear_StartX":{self.data['DefenseMove']['MidNear_StartX']},
    				"MidNear_BackInMark":{f(self.data['DefenseMove']['MidNear_BackInMark'])},
    				"MidNear_BackInBlock":{f(self.data['DefenseMove']['MidNear_BackInBlock'])},
    				"MidNear_HalfInMark":{f(self.data['DefenseMove']['MidNear_HalfInMark'])},
    				"MidNear_HalfInBlock":{f(self.data['DefenseMove']['MidNear_HalfInBlock'])},
    				"MidNear_ForwardInMark":{f(self.data['DefenseMove']['MidNear_ForwardInMark'])},
    				"MidNear_ForwardInBlock":{f(self.data['DefenseMove']['MidNear_ForwardInBlock'])},
    				"MidNear_OppsDistXToBall":{self.data['DefenseMove']['MidNear_OppsDistXToBall']},
    				"MidNear_MarkAgain":{f(self.data['DefenseMove']['MidNear_MarkAgain'])},
    				"MidNear_BlockAgain":{f(self.data['DefenseMove']['MidNear_BlockAgain'])},
    				"MidNear_MarkAgainMaxDistToChangeCost":{self.data['DefenseMove']['MidNear_MarkAgainMaxDistToChangeCost']},
    				"MidNear_MarkAgainChangeCostZ":{self.data['DefenseMove']['MidNear_MarkAgainChangeCostZ']},
    				"MidNear_PosMaxDistMark":{self.data['DefenseMove']['MidNear_PosMaxDistMark']},
    				"MidNear_HPosMaxDistMark":{self.data['DefenseMove']['MidNear_HPosMaxDistMark']},
    				"MidNear_PosMaxDistBlock":{self.data['DefenseMove']['MidNear_PosMaxDistBlock']},
    				"MidNear_HPosMaxDistBlock":{self.data['DefenseMove']['MidNear_HPosMaxDistBlock']},
    				"Goal_ForwardInMark":{f(self.data['DefenseMove']['Goal_ForwardInMark'])},
    				"Goal_ForwardInBlock":{f(self.data['DefenseMove']['Goal_ForwardInBlock'])},
    				"Goal_PosMaxDistMark":{self.data['DefenseMove']['Goal_PosMaxDistMark']},
    				"Goal_HPosMaxDistMark":{self.data['DefenseMove']['Goal_HPosMaxDistMark']},
    				"Goal_OffsideMaxDistMark":{self.data['DefenseMove']['Goal_OffsideMaxDistMark']},
    				"Goal_PosMaxDistBlock":{self.data['DefenseMove']['Goal_PosMaxDistBlock']},
    				"Goal_HPosMaxDistBlock":{self.data['DefenseMove']['Goal_HPosMaxDistBlock']},
    				"Goal_OffsideMaxDistBlock":{self.data['DefenseMove']['Goal_OffsideMaxDistBlock']}
    			}}
    }}'''

    def write_to_file(self, directory, name):
        if directory[-1] != '/':
            directory += '/'
        with open(f'{directory}{name}.json', 'w') as file:
            file.write(self.to_string())


if __name__ == '__main__':
    test = SettingFile()
    test.write_to_file('example')
