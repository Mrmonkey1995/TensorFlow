import tensorflow as tf

input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
add = tf.add(input2, input3)
mut = tf.multiply(input1, add)
with tf.compat.v1.Session() as session:
    result = session.run([mut, add])
    print(result)
