# MNIST 데이터 준비

import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

# CNN 모델 - 2차원 평면
X = tf.placeholder(tf.float32, [None, 28, 28, 1])
Y = tf.placeholder(tf.float32, [None, 10])

#drop out 비율
keep_prob  = tf.placeholder(tf.float32)

# 계층 1 정의
# W1 [3 3 1 32] -> [3 3]: 커널 크기(가로, 세로), 1: 입력값 X 의 특성수(크기), 32: 필터 갯수(채널)
# L1 Conv shape=(?, 28, 28, 32)
# Pool ->(?, 14, 14, 32)

#Convolution
W1 = tf.Variable(tf.random_normal([3,3,1,32], stddev = 0.01))
L1 = tf.nn.conv2d(X, W1, strides = [1,1,1,1], padding='SAME')

#Pooling
L1 = tf.nn.max_pool(L1, ksize=[1,2,2,1], strides = [1,2,2,1], padding='SAME')


# 계층 2 정의
# L2 Conv shape=(?, 14, 14, 64)
# Pool ->(?, 7, 7, 64)

#Convolution
W2 = tf.Variable(tf.random_normal([3,3,32,64], stddev = 0.01))
L2 = tf.nn.conv2d(L1, W2, strides = [1,1,1,1], padding='SAME')
L2 = tf.nn.relu(L2)

#Pooling
L2 = tf.nn.max_pool(L2, ksize=[1,2,2,1], strides = [1,2,2,1], padding='SAME')


# 완전 연결 레이어: 입력값 7x7x64 -> 출력값 256
# 직전의 Pool 사이즈인 (?, 7, 7, 64) 를 참고하여 차원을 줄임
# Reshape ->(?, 256)

W3 = tf.Variable(tf.random_normal([7*7*64, 256], stddev = 0.01))
L3 = tf.reshape(L2, [-1,7*7*64])
L3 = tf.matmul(L3, W3)
L3 = tf.nn.relu(L3)

L3 = tf.nn.dropout(L3, keep_prob)


# 최종 출력값 L3 에서의 출력 256개를 입력값으로 받아서
# 0~9 레이블인 10개의 출력값을 만듭니다.

W4 = tf.Variable(tf.random_normal([256,10], stddev = 0.01))
model = tf.matmul(L3, W4)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits = model, labels=Y))
#optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)
optimizer = tf.train.RMSPropOptimizer(0.001,0.9).minimize(cost) #속도 더 빠름

# 학습 회수 카운트
global_step = tf.Variable(0, trainable = False, name="global_step") 


with tf.Session() as sess:
    
    # 체크포인트가 존재하는지 검사
    ckpt = tf.train.get_checkpoint_state('./model_CNN')
    saver = tf.train.Saver(tf.global_variables())
    
    
    if ckpt and tf.train.checkpoint_exists(ckpt.model_checkpoint_path):
        # 체크포인트가 존재하는 경우, 복원
        # global_step 값도 복원됨
        saver.restore(sess, ckpt.model_checkpoint_path)
    else :
        # 체크포인트가 존재하지 않는 경우, 전역 변수 초기화
        sess.run(tf.global_variables_initializer())


    #신경망 모델 학습
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    batch_size = 100
    total_batch = int(mnist.train.num_examples / batch_size)

    for epoch in range(15):
        total_cost = 0

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            #이미지 데이터를 CNN 모델을 위한 자료 형태 [28 28 1]의 형태로 재구성
            batch_xs = batch_xs.reshape(-1, 28, 28, 1)
            
            _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y:batch_ys, keep_prob: 0.7})

            total_cost += cost_val

            print('Epoch:', '%04d' % (epoch+1),'Avg. cost =', '{:.3f}'.format(total_cost / total_batch))

    
    # 체크포인트 저장
    saver.save(sess, './model_CNN/dnn.ckpt', global_step=global_step)
    print('최적화 완료')

    is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y,1))
    accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
    answer = sess.run(accuracy, feed_dict={X: mnist.test.images.reshape(-1,28,28,1), Y: mnist.test.labels, keep_prob: 1})

    print('정확도: {:.4}%'.format(answer*100))