import numpy
import pandas
from scipy.special import expit

class neuralNetwork:

    #신경망 초기화
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate, path=None):

        #입력, 은닉, 출력 계층의 노드 개수 설정
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        #학습률
        self.lr = learningrate

        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        #활성화 함수로 시그모이드 함수 설정
        self.activation_function = lambda x: expit(x)



    #신경망 학습
    def train(self, inputs_list, targets_list):
        # 입력 리스트를 2차원의 행렬로 변환
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # 은닉 계층으로 들어오는 신호를 계산
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 은닉 계층에서 나가는 신호를 계산
        hidden_outputs = self.activation_function(hidden_inputs)

        # 최종 출력 계층으로 들어오는 신호를 계산
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 최종 출력 계층에서 나가는 신호를 계산
        final_outputs = self.activation_function(final_inputs)

        output_errors = targets - final_outputs

        hidden_errors = numpy.dot(self.who.T, output_errors)

        #은닉 계층과 출력 계층간의 가중치 업데이트
        self.who += self.lr*numpy.dot((output_errors*final_outputs*(1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        #입력 계층과 은닉 계층간의 가중치 업데이트
        self.wih += self.lr*numpy.dot((hidden_errors*hidden_outputs*(1.0 - hidden_outputs)), numpy.transpose(inputs))

        # 2단계 가중치 업데이트
        # 출력 계층의 오차(실제 값 - 계산 값)
        output_errors = targets - final_outputs
        # 은닉 계층의 오차는 가중치 값의 비례로 재조정
        hidden_errors = numpy.dot(self.who.T, output_errors)





    # 신경망 질의하기
    def query(self, inputs_list):
        # 입력 리스트를 2차원 행렬로 변환
        inputs = numpy.array(inputs_list, ndmin=2).T

        # 은닉 계층으로 들어오는 신호를 계산
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 은닉 계층에서 나가는 신호를 계산, sigmoid
        hidden_outputs = self.activation_function(hidden_inputs)

        # 최종 출력 계층으로 들어오는 신호를 계산
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 최종 출력 계층에서 나가는 신호를 계산
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


    def load(self, file_name):
        data_frame= pandas.read_csv(file_name, header=None)
        values = data_frame.values
        labels = values[:,0:1]
        data = values[:,1:]/255.0*0.99 + 0.01
        return labels, data


    def train_from_file(self, file_name):
      
        for label, inputs in zip(*self.load(file_name)):
            targets = numpy.zeros(self.onodes)+0.01
            targets[label] = 0.99
            
            self.train(inputs, targets)


    def query_from_file(self, file_name):
        scorecard = []

        for label, inputs in zip(*self.load(file_name)):
            outputs = self.query(inputs)
            
            answer = numpy.argmax(outputs)
            # 정답 여부 판단
            if(label == answer):
                # 정답인 경우 성적표에 1을 추가
                scorecard.append(1)
            else:
                # 정답이 아닌 경우 성적표에 0을 추가
                scorecard.append(0)
        
        scorecard_array = numpy.asarray(scorecard)
        return scorecard_array.sum() / scorecard_array.size


    def load_weight(self, path):
        self.wih = pandas.read_csv(path+"_wih.csv", header=None)
        self.who = pandas.read_csv(path+"_who.csv", header=None)
        
    

    def save_weight(self, path):
        pandas.DataFrame(self.wih).to_csv(path+"_wih.csv", index=False, header=None)
        pandas.DataFrame(self.who).to_csv(path+"_who.csv", index=False, header=None)



if __name__ == "__main__":
    # 입력, 은닉, 출력 노드의 수
    input_nodes = 3
    hidden_nodes = 3
    output_nodes = 3
    
    # 학습률 0.3 정의
    learning_rate = 0.3

    # 신경망의 인스턴스 생성
    n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    result = n.query([1.0,0.5,-1.5])
    print(result)