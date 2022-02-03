import GenerateFile
from GenerateFile import SettingFile

false = False
true = True


class SettingGenerator:
    def __init__(self):
        self.data = dict()
        self.data['Formation'] = dict()
        self.data['Formation']['Win'] = ["433"]
        self.data['Formation']['Lost'] = ["433"]
        self.data['Formation']['Draw'] = ["433"]

        self.data['Strategy'] = dict()
        self.data['Strategy']["Is5ForwardWin"] = [true]
        self.data['Strategy']["Is5ForwardLost"] = [true]
        self.data['Strategy']["Is5ForwardDraw"] = [true]
        self.data['Strategy']["TeamTactic"] = ["Normal"]
        self.data['Strategy']["IsGoalForward"] = [false]

        self.data['ChainAction'] = dict()
        self.data['ChainAction']["ChainNodeNumber"] = [750,450]
        self.data['ChainAction']['ChainDeph'] = [2,1]
        self.data['ChainAction']['UseShootSafe'] = [false]
        self.data['ChainAction']['DribblePosCountZ'] = [0.8]
        self.data['ChainAction']['DribblePosCountMaxFrontOpp'] = [8]
        self.data['ChainAction']['DribblePosCountMaxBehindOpp'] = [4]

        self.data['OffensiveMove'] = dict()
        self.data['OffensiveMove']['Is9BrokeOffside'] = [false]

        self.data['DefenseMove'] = dict()
        self.data['DefenseMove']["PassBlock"] = [false]
        self.data['DefenseMove']["StartMidMark"] = [-30.0]
        self.data['DefenseMove']["StaticOffensiveOpp"] = [[8, 9, 10, 11]]
        self.data['DefenseMove']["MidTh_BackInMark"] = [true]
        self.data['DefenseMove']["MidTh_BackInBlock"] = [true]
        self.data['DefenseMove']["MidTh_HalfInMark"] = [true]
        self.data['DefenseMove']["MidTh_HalfInBlock"] = [true]
        self.data['DefenseMove']["MidTh_ForwardInMark"] = [false]
        self.data['DefenseMove']["MidTh_ForwardInBlock"] = [true]
        self.data['DefenseMove']["MidTh_RemoveNearOpps"] = [true]
        self.data['DefenseMove']["MidTh_DistanceNearOpps"] = [5.0]
        self.data['DefenseMove']["MidTh_XNearOpps"] = [3.0]
        self.data['DefenseMove']["MidTh_PosDistZ"] = [1.0]
        self.data['DefenseMove']["MidTh_HPosDistZ"] = [0.7]
        self.data['DefenseMove']["MidTh_PosMaxDistMark"] = [15.0]
        self.data['DefenseMove']["MidTh_HPosMaxDistMark"] = [15.0]
        self.data['DefenseMove']["MidTh_HPosYMaxDistMark"] = [12.0]
        self.data['DefenseMove']["MidTh_PosMaxDistBlock"] = [20.0]
        self.data['DefenseMove']["MidTh_HPosMaxDistBlock"] = [20.0]
        self.data['DefenseMove']["MidTh_HPosYMaxDistBlock"] = [20.0]
        self.data['DefenseMove']["MidProj_PosMaxDistMark"] = [10.0]
        self.data['DefenseMove']["MidProj_HPosMaxDistMark"] = [10.0]
        self.data['DefenseMove']["MidProj_PosMaxDistBlock"] = [25.0]
        self.data['DefenseMove']["MidProj_HPosMaxDistBlock"] = [25.0]
        self.data['DefenseMove']["Mid_UseProjectionMark"] = [true]
        self.data['DefenseMove']["MidNear_StartX"] = [30.0]
        self.data['DefenseMove']["MidNear_BackInMark"] = [false]
        self.data['DefenseMove']["MidNear_BackInBlock"] = [false]
        self.data['DefenseMove']["MidNear_HalfInMark"] = [true]
        self.data['DefenseMove']["MidNear_HalfInBlock"] = [true]
        self.data['DefenseMove']["MidNear_ForwardInMark"] = [true]
        self.data['DefenseMove']["MidNear_ForwardInBlock"] = [true]
        self.data['DefenseMove']["MidNear_OppsDistXToBall"] = [25.0]
        self.data['DefenseMove']["MidNear_MarkAgain"] = [true]
        self.data['DefenseMove']["MidNear_BlockAgain"] = [false]
        self.data['DefenseMove']["MidNear_MarkAgainMaxDistToChangeCost"] = [5.0]
        self.data['DefenseMove']["MidNear_MarkAgainChangeCostZ"] = [1.4]
        self.data['DefenseMove']["MidNear_PosMaxDistMark"] = [10.0]
        self.data['DefenseMove']["MidNear_HPosMaxDistMark"] = [15.0]
        self.data['DefenseMove']["MidNear_PosMaxDistBlock"] = [20.0]
        self.data['DefenseMove']["MidNear_HPosMaxDistBlock"] = [20.0]
        self.data['DefenseMove']["Goal_ForwardInMark"] = [false]
        self.data['DefenseMove']["Goal_ForwardInBlock"] = [true]
        self.data['DefenseMove']["Goal_PosMaxDistMark"] = [10.0]
        self.data['DefenseMove']["Goal_HPosMaxDistMark"] = [10.0]
        self.data['DefenseMove']["Goal_OffsideMaxDistMark"] = [10.0]
        self.data['DefenseMove']["Goal_PosMaxDistBlock"] = [25.0]
        self.data['DefenseMove']["Goal_HPosMaxDistBlock"] = [25.0]
        self.data['DefenseMove']["Goal_OffsideMaxDistBlock"] = [25.0]

    def generate(self):
        output = [SettingFile()]
        for key in self.data.keys():
            for key2 in self.data[key].keys():
                new_output = []
                for setting in output:
                    for value in self.data[key][key2]:
                        new_setting = setting.clone()
                        new_setting.data[key][key2] = value
                        new_output.append(new_setting)
                output = new_output

        return output


if __name__ == '__main__':
    settings = SettingGenerator().generate()
    for i in range(len(settings)):
        settings[i].write_to_file(str(i + 1))
