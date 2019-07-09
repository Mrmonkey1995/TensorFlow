import tensorflow as tf

x = tf.Variable([1, 2])
a = tf.constant([3, 3])
sub = tf.subtract(x, a)
add = tf.add(x, sub)
# 变量初始化
init = tf.compat.v1.global_variables_initializer()
with tf.compat.v1.Session() as session:
    session.run(init)
    print(session.run(sub))
    print(session.run(add))
