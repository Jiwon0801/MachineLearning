import tensorflow as tf
from GTSRB_Dataload import load_data

#데이터 준비
dirpath = './GTSRB_IMG/'
data = load_data(dirpath)

#모델 정의
X = tf.placeholder(tf.float32, [None,1024])
Y = tf.placeholder(tf.float32, [None,43])

W1 = tf.Variable(tf.random_normal([1024,256], stddev = 0.01))
L1 = tf.nn.relu(tf.matmul(X, W1))

W2 = tf.Variable(tf.random_normal([256,256], stddev = 0.01))
L2 = tf.nn.relu(tf.matmul(L1, W2))

W3 = tf.Variable(tf.random_normal([256,43], stddev = 0.01))

model = tf.matmul(L2, W3)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

batch_size=100
total_batch  = int(data.train.num_examples/batch_size)

for epoch in range(50):
    total_cost = 0

    for i in range(total_batch):
        batch_xs, batch_ys = data.train.next_batch(batch_size)
        _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y:batch_ys})

        total_cost += cost_val
    
    data.train.reset_batch()

    print('Epoch:', '%04d' % (epoch+1),'Avg. cost =', '{:.3f}'.format(total_cost / total_batch))

print('최적화 완료')

is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y,1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
answer = sess.run(accuracy, feed_dict={X: data.test.images, Y: data.test.labels})

print('정확도: {:.4}%'.format(answer*100))