import tensorflow as tf

# input1 = tf.constant(3.0)
# input2 = tf.constant(2.0)
# input3 = tf.constant(5.0)
# add = tf.add(input2, input3)
# mut = tf.multiply(input1, add)
# with tf.compat.v1.Session() as session:
#     # Fetch
#     result = session.run([mut, add])
#     print(result)


# Feed
input1 = tf.placeholder(tf.float32)
input2 = tf.compat.v1.placeholder(tf.float32)
output = tf.multiply(input1, input2)
with tf.compat.v1.Session() as session:
    # Feed的数据以字典形式传入
    print(session.run(output, feed_dict={input1: [7.], input2: [2.]}))
