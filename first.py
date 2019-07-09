import tensorflow as tf

# 创建一个常量,一行两列
m1 = tf.constant([[3, 3]])
# 创建一个常量，两行一列
m2 = tf.constant([[2], [3]])
# 矩阵相乘的结果
product = tf.matmul(m1, m2)
print(product)
# 定义一个会话
with tf.compat.v1.Session() as session:
    result = session.run(product)
    print(result)
